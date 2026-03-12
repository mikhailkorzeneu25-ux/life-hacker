import streamlit as st
import requests
import time

# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="Life Hacker AI",
    page_icon="🤖"
)

st.title("🤖 Life Hacker AI")
st.write("Ask for productivity, study, or life advice.")

# -----------------------------
# HuggingFace API
# -----------------------------
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

# IMPORTANT: add your HuggingFace token
headers = {
    "Authorization": "Bearer YOUR_HUGGINGFACE_API_KEY"
}

# -----------------------------
# AI response function
# -----------------------------
def get_ai_response(prompt):

    payload = {
        "inputs": f"You are a helpful life coach chatbot.\nUser: {prompt}\nAssistant:"
    }

    for i in range(5):  # retry if model is loading
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            return result[0]["generated_text"]

        # If model is loading
        if response.status_code == 503:
            time.sleep(3)

    return "⚠️ AI is busy right now. Please try again."

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask for a life hack...")

if prompt:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(prompt)
            st.markdown(ai_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })
