# Aplicación Streamlit: PDF de Google Drive a GitHub Pages

Esta aplicación permite convertir archivos PDF almacenados en Google Drive a páginas de GitHub.

## Requisitos previos

Antes de instalar las dependencias de Python, asegúrate de tener instalado:

1. Python 3.7 o superior
2. pip (gestor de paquetes de Python)
3. Git

Para instalar Git:
- En Ubuntu o Debian: `sudo apt-get install git`
- En macOS (usando Homebrew): `brew install git`
- En Windows: Descarga e instala desde [git-scm.com](https://git-scm.com/)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. (Opcional pero recomendado) Crea un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación:
   ```
   streamlit run app.py
   ```

2. Abre tu navegador y ve a la dirección que Streamlit te proporciona (generalmente `http://localhost:8501`).

3. Sigue las instrucciones en la interfaz para procesar tus archivos PDF y subirlos a GitHub Pages.

## Notas

- Asegúrate de tener permisos para pushear al repositorio de GitHub que estés utilizando.
- Los archivos PDF en Google Drive deben ser accesibles mediante un enlace compartido público.
