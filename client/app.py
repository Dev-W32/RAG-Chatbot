import streamlit as st
from components.upload import render_uploader
from components.chatui import render_chat
from components.history_download import render_history_download



st.set_page_config(page_title="Rag Chatbot", page_icon=":robot_face:", layout="wide")
st.title("RAG PDF Chatbot")

render_uploader()
render_chat()
render_history_download()
