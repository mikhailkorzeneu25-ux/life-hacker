import streamlit as st
import random

# Page config
st.set_page_config(page_title="Cat Bot 🐱", page_icon="🐾")

st.title("🐱 Cat Bot")
st.write("Hi! I'm Cat Bot. Ask me something about cats!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate cat responses
def get_cat_response(user_input):
    user_input = user_input.lower()

    responses = {
        "food": [
            "Cats love tuna! 🐟",
            "Dry food is good, but wet food keeps cats hydrated!",
            "Treats are great... but not too many! 😸"
        ],
        "sleep": [
            "Cats sleep 12–16 hours a day! 😴",
            "If your cat sleeps a lot, that's normal!",
        ],
        "play": [
            "Cats love chasing laser pointers! 🔴",
            "Try a feather toy — they go crazy for it!",
        ],
        "name": [
            "You can name your cat Luna, Milo, or Whiskers! 🐾",
            "Shadow is a cool cat name!",
        ]
    }

    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])

    return "Meow! 🐱 I don't know about that, but I love naps and snacks!"

# User input
prompt = st.chat_input("Ask something about cats...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate bot response
    response = get_cat_response(prompt)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)
