import streamlit as st

# Page config
st.set_page_config(
    page_title="Life Hacker Chat Bot",
    page_icon="🤖"
)

st.title("🤖 Life Hacker Chat Bot")
st.write("Smart productivity and life tips")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function for chatbot responses
def get_ai_response(prompt):

    prompt = prompt.lower()

    if "study" in prompt:
        return "📚 Try the Pomodoro technique: 25 minutes study, 5 minutes break."

    elif "productivity" in prompt:
        return "⚡ Start your day with the most important task first."

    elif "sleep" in prompt:
        return "😴 Avoid screens 1 hour before bedtime."

    elif "motivation" in prompt:
        return "🔥 Discipline beats motivation. Build small daily habits."

    elif "exercise" in prompt:
        return "💪 Even 10 minutes of movement daily improves health."

    elif "focus" in prompt:
        return "🎯 Remove distractions and work in short focused sprints."

    elif "time management" in prompt:
        return "⏰ Use the 2-minute rule: if it takes less than 2 minutes, do it now."

    else:
        return "🤖 Try asking about: study, productivity, sleep, focus, exercise, or motivation."

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask for a life hack...")

if prompt:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    response = get_ai_response(prompt)

    # Save bot message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)
