
import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

# Función para extraer texto de un archivo PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Función para extraer texto de un archivo DOCX
def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Función para extraer texto de un archivo HTML
def extract_text_from_html(file):
    soup = BeautifulSoup(file, "html.parser")
    return soup.get_text()

# Función para extraer texto de un archivo TXT
def extract_text_from_txt(file):
    return file.read().decode('utf-8')

# Función para limpiar el texto
def clean_text(text):
    text = re.sub(r"\s+", " ", text)  # Reemplazar múltiples espacios por uno
    return text.strip()

# Cargar el modelo de Hugging Face
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Función para generar embeddings
def generate_embeddings(text):
    return model.encode(text)

# Función para crear un índice FAISS
def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

# Interfaz gráfica con Streamlit
st.title("Chatbot de Análisis de Currículum Vitae")
uploaded_files = st.file_uploader("Sube tus documentos", accept_multiple_files=True)

if uploaded_files:
    # Combinar todo el texto de los archivos subidos
    all_text = ""
    for uploaded_file in uploaded_files:
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(uploaded_file)
        elif file_type == "text/plain":
            text = extract_text_from_txt(uploaded_file)
        elif file_type == "text/html":
            text = extract_text_from_html(uploaded_file)
        else:
            st.warning(f"Formato de archivo no soportado: {uploaded_file.name}")
            continue  # Saltar al siguiente archivo

        # Limpiar y añadir texto
        text = clean_text(text)
        all_text += text + "\n"

    # Generar embeddings para el texto combinado
    embeddings = generate_embeddings([all_text])

    # Crear índice FAISS
    index = create_faiss_index(embeddings)

    # Mostrar texto extraído
    st.text_area("Texto extraído de los currículums:", all_text, height=300)

    # Permitir al usuario escribir preguntas
    question = st.text_input("Haz una pregunta sobre los currículums:")
    if question:
        # Generar embedding de la pregunta
        query_embedding = generate_embeddings([question])

        # Buscar en el índice FAISS
        distances, indices = index.search(np.array([query_embedding[0]]), k=5)

        # Mostrar respuestas
        st.write("Respuestas encontradas:")
        for i in indices[0]:
            st.write(all_text)
