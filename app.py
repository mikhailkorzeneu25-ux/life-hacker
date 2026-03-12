import streamlit as st
import requests

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
# OpenRouter API
# -----------------------------
API_KEY = "YOUR_OPENROUTER_API_KEY"

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# -----------------------------
# AI Response Function
# -----------------------------
def get_ai_response(prompt):

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful life coach giving productivity and life advice."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]

    return "⚠️ AI failed to respond."

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# Chat Input
# -----------------------------
prompt = st.chat_input("Ask for a life hack...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_ai_response(prompt)
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
