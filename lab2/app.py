import streamlit as st
import ollama


OLLAMA_BASE_URL = "http://localhost:11434/api"

st.set_page_config(
    page_title="Ollama Multi-Modèles",
    layout="wide",
)

st.title("Application locale Ollama multi-modèles")
st.write(
    "Cette application détecte les modèles Ollama installés localement, "
    "permet de choisir un modèle et compare plusieurs modèles sur la même question.")



models =  [m.model for m in ollama.list().models]

if not models:
    st.error("Aucun modèle Ollama n’a été détecté.")
    st.info("Vérifiez que Ollama est lancé, puis exécutez par exemple : ollama pull gemma3:1b")
    st.stop()


with st.sidebar:
    st.header("Configuration")
    selected_model = st.selectbox("Modèle principal", models)



user_prompt = st.chat_input("Comment je peux vous aider aujourd'hui")

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = ollama.chat(
        model=selected_model,
        messages=[
            {
                'role':'user',
                'content':user_prompt
            }
        ]
    )
    answer = response['message']['content']
    st.chat_message("assistant").write(answer)
