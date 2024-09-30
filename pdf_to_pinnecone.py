import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, TokenTextSplitter
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
import io
import tempfile
import markdown
import re
import requests

load_dotenv()

def get_file_list(folder_id):
    url = f"https://drive.google.com/drive/folders/{folder_id}"
    response = requests.get(url)
    file_ids = re.findall(r'"(https://drive\.google\.com/file/d/[^/]+/view[^"]+)"', response.text)
    return [{'id': fid.split('/')[5], 'name': fid.split('/')[-1], 'webViewLink': fid} for fid in file_ids]

def download_file(file_id):
    url = f"https://drive.google.com/uc?id={file_id}&export=download"
    response = requests.get(url)
    content = response.content
    return content, is_valid_pdf(content)


def is_valid_pdf(file_content):
    return file_content.startswith(b'%PDF-')
def pdf_to_pinecone(folder_id, index_name, upload_batch_size=100):
    # Initialize Pinecone
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pinecone_environment = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")
    
    pc = Pinecone(api_key=pinecone_api_key)

    # Create Pinecone index if it doesn't exist
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"), model="text-embedding-3-small")
    
    valid_index_name = re.sub(r'[^a-z0-9-]', '-', index_name.lower())
    
    if valid_index_name not in pc.list_indexes().names():
        pc.create_index(
            name=valid_index_name, 
            dimension=1536, 
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region=pinecone_environment
            )
        )

    index = pc.Index(valid_index_name)

    # Get list of PDF files in the public Google Drive folder
    files = get_file_list(folder_id)

    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, file in enumerate(files):
        status_text.text(f"Processing file {i+1} of {len(files)}: {file['name']}")
        
        # Download the PDF file
        file_content, is_pdf = download_file(file['id'])

        if not is_pdf:
            st.warning(f"Skipping {file['name']}: Not a valid PDF file")
            continue

        # Save the file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
            temp_file.write(file_content)
            temp_file_path = temp_file.name

        try:
            # Load and process the PDF
            loader = PyPDFLoader(temp_file_path)
            documents = loader.load()

            # Split documents into text chunks
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            texts = text_splitter.split_documents(documents)
            text_splitter = TokenTextSplitter(chunk_size=500, chunk_overlap=100, encoding_name="cl100k_base")
            texts = text_splitter.split_documents(texts)

            # Generate embeddings and persist in Pinecone
            vectors = []
            for j, text in enumerate(texts):
                embedding = embeddings.embed_documents([text.page_content])[0]
                markdown_content = markdown.markdown(text.page_content)
                vectors.append((f"{file['id']}_{j}", embedding, {
                    "text": markdown_content,
                    "source": file['webViewLink'],
                    "title": file['name'],
                    "page": text.metadata.get('page', 'Unknown')
                }))

                # Upload to Pinecone in batches
                if len(vectors) >= upload_batch_size:
                    index.upsert(vectors)
                    vectors = []

            # Upload any remaining vectors
            if vectors:
                index.upsert(vectors)

            # Remove the temporary file
            os.unlink(temp_file_path)
        
        except Exception as e:
            st.warning(f"Error processing {file['name']}: {str(e)}")
            continue

        finally:
            # Remove the temporary file
            try:
                os.unlink(temp_file_path)
            except OSError:
                pass

        # Update the progress bar
        progress_bar.progress((i + 1) / len(files))

    status_text.text("Processing completed.")

def extract_folder_id(folder_url):
    pattern = r'(?:https?:\/\/)?(?:www\.)?drive\.google\.com\/(?:drive\/folders\/|file\/d\/|open\?id=)([a-zA-Z0-9-_]+)'
    match = re.search(pattern, folder_url)
    if match:
        return match.group(1)
    return None

def main():
    st.title("PDF to Pinecone")

    index_name = st.text_input("Pinecone index name", "syj-instructivos")
    folder_url = st.text_input("Google Drive folder URL")

    if st.button("Process"):
        if not folder_url:
            st.error("Please enter the Google Drive folder URL.")
            return

        folder_id = extract_folder_id(folder_url)
        if not folder_id:
            st.error("Could not extract folder ID from the provided URL.")
            return

        try:
            pdf_to_pinecone(folder_id, index_name, 10)
            st.success("Processing completed successfully.")
        except Exception as e:
            st.error(f"An error occurred during processing: {str(e)}")

if __name__ == "__main__":
    main()
