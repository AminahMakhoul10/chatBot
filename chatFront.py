import streamlit as st 
import chat as glib

st.set_page_config(page_title="Chatbot")
st.title("Chatbot ")

if 'memory' not in st.session_state:
    st.session_state.memory = glib.create_memory()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    
    with st.chat_message(message['role']):
        st.markdown(message['text'])

input_text = st.chat_input("Chat with your bot aqui")

if input_text:

    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append({ "role": "user", "text": input_text})
    detailed_input_text = "Você é um assistente virtual. Por favor, responda a seguinte pergunta de forma detalhada: " + input_text
    chat_response = glib.get_chat_response(detailed_input_text, st.session_state.memory)  # Chamar get_chat_response com input_text e memory

    with st.chat_message("assistant"):
        st.markdown(chat_response)

    st.session_state.chat_history.append({ "role": "assistant", "text": chat_response})