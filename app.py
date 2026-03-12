import streamlit as st
import requests

# -----------------------------
# Page settings
# -----------------------------
st.set_page_config(
    page_title="Life Hacker AI",
    page_icon="🤖"
)

st.title("🤖 Life Hacker AI")
st.write("Ask for productivity, study, or life advice.")

# -----------------------------
# HuggingFace model API
# -----------------------------
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {}

def get_ai_response(prompt):

    payload = {
        "inputs": f"You are a helpful life coach chatbot. Give helpful life advice.\nUser: {prompt}\nAssistant:"
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]

    return "⚠️ AI is loading. Try again in a few seconds."

# -----------------------------
# Chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat input
# -----------------------------
prompt = st.chat_input("Ask for a life hack...")

if prompt:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.spinner("Thinking..."):
        response = get_ai_response(prompt)

    # Show AI response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
