import streamlit as st

st.set_page_config(page_title="Life Hacker Bot", page_icon="💡")

st.title("💡 Life Hacker Chatbot")
st.write("Ask me for quick life hacks!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask for a life hack...")

def get_life_hack(user_input):
    hacks = {
        "sleep": "Try the 4-7-8 breathing method to fall asleep faster 😴",
        "focus": "Use the Pomodoro technique: 25 min work, 5 min break ⏱️",
      
