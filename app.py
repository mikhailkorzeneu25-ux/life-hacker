import streamlit as st
import requests
import json

# Page settings
st.set_page_config(page_title="life hacker chat bot", page_icon="🤖")

st.title("🤖 life hacker chat bot")
st.write("Powered by Local AI (No API Key Needed)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to talk to Ollama
def get_ai_response(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    response_json = response.json()

    return response_json["response"]

# User input
if prompt := st.chat_input("Type your message..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(prompt)
            st.markdown(ai_response)

    # Save AI response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )
