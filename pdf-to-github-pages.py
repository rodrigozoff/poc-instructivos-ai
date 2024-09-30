import streamlit as st
import requests
import io
import os
from PyPDF2 import PdfReader
from PIL import Image
import git
from PyPDF2.errors import PdfReadError
import re
import datetime

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

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

def extract_folder_id(folder_url):
    pattern = r'(?:https?:\/\/)?(?:www\.)?drive\.google\.com\/(?:drive\/folders\/|file\/d\/|open\?id=)([a-zA-Z0-9-_]+)'
    match = re.search(pattern, folder_url)
    if match:
        return match.group(1)
    return None

def convert_pdf_to_markdown(file, output_dir):
    try:
        reader = PdfReader(file)
        markdown_content = ""
        
        images_dir = os.path.join(output_dir, "images")
        os.makedirs(images_dir, exist_ok=True)
        
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            markdown_content += text + "\n\n"
            
            for j, image in enumerate(page.images):
                img = Image.open(io.BytesIO(image.data))
                img_path = os.path.join(images_dir, f"image_{i}_{j}.png")
                img.save(img_path)
                relative_img_path = os.path.relpath(img_path, output_dir)
                markdown_content += f"![Image {j} from page {i}]({relative_img_path})\n\n"
        
        return markdown_content
    except PdfReadError:
        return "Error: The file appears to be corrupted or is not a valid PDF."

def create_github_pages(markdown_content, output_dir, pdf_name):
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate a unique timestamp-based filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{pdf_name}.md"
    
    # Create individual markdown file for each PDF
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        f.write(f"# {pdf_name}\n\n")
        f.write(markdown_content)
    
    return filename

def push_to_github(repo_path, commit_message):
    repo = git.Repo(repo_path)
    repo.git.add(A=True)
    repo.index.commit(commit_message)
    origin = repo.remote(name='origin')
    origin.push()

def main():
    st.title("PDF a GitHub Pages Converter")

    st.write("Esta aplicación convierte archivos PDF de Google Drive a páginas de GitHub.")

    folder_url = st.text_input("Ingrese el enlace compartido de la carpeta de Google Drive:", placeholder="https://drive.google.com/drive/folders/1txe2ghrp6FTPsQecdF9_RnPM9c5Bbv_E?usp=sharing")

    if folder_url:
        folder_id = extract_folder_id(folder_url)
        
        if folder_id and st.button("Procesar PDFs"):
            files = get_file_list(folder_id)
            
            progress_bar = st.progress(0)
            status_text = st.empty()

            ensure_dir('github_pages')

            # Create main index.md
            with open(os.path.join('github_pages', 'index.md'), 'w', encoding='utf-8') as main_index:
                main_index.write("# Índice de PDFs\n\n")

            for i, file in enumerate(files):
                status_text.text(f"Procesando archivo {i+1} de {len(files)}: {file['name']}")
                
                file_content, is_pdf = download_file(file['id'])

                if not is_pdf:
                    st.warning(f"Omitiendo {file['name']}: No es un archivo PDF válido")
                    continue

                pdf_file = io.BytesIO(file_content)
                pdf_name = file["name"].replace(".pdf", "")
                output_dir = os.path.join('github_pages', pdf_name)
                markdown_content = convert_pdf_to_markdown(pdf_file, output_dir)
                
                if markdown_content.startswith("Error:"):
                    st.error(f"Error en {file['name']}: {markdown_content}")
                else:
                    filename = create_github_pages(markdown_content, output_dir, pdf_name)
                    st.success(f"PDF {file['name']} procesado y convertido a Markdown: {filename}")

                # Update main index.md
                with open(os.path.join('github_pages', 'index.md'), 'a', encoding='utf-8') as main_index:
                    main_index.write(f"- [{pdf_name}]({pdf_name}/{filename})\n")

                progress_bar.progress((i + 1) / len(files))

            status_text.text("Procesamiento completado.")

            if st.button("Subir a GitHub"):
                try:
                    push_to_github('github_pages', "Actualización automática de GitHub Pages")
                    st.success("Contenido subido a GitHub con éxito.")
                except Exception as e:
                    st.error(f"Error al subir a GitHub: {str(e)}")

if __name__ == "__main__":
    main()
