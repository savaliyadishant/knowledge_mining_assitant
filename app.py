# import streamlit as st
# import google.generativeai as genai
# from PIL import Image
# import os

# genai.configure(api_key=st.secrets.get("GEMINI_API_KEY"))

# # Set up page
# st.set_page_config(page_title="Gemini Chatbot", layout="wide")
# st.title("💬 Gemini Chatbot (ChatGPT Style)")

# # Set up model and chat
# if "chat" not in st.session_state:
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     st.session_state.chat = model.start_chat(history=[])

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display existing chat history
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # Optional image upload
# uploaded_image = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

# # Input box at bottom
# prompt = st.chat_input("Ask something...")

# # When user sends a message
# if prompt:
#     # Show user message
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Send to Gemini
#     try:
#         if uploaded_image:
#             image = Image.open(uploaded_image)
#             response = st.session_state.chat.send_message([prompt, image])
#         else:
#             response = st.session_state.chat.send_message(prompt)

#         reply = response.text

#         # Show assistant message
#         with st.chat_message("assistant"):
#             st.markdown(reply)
#         st.session_state.messages.append({"role": "assistant", "content": reply})

#     except Exception as e:
#         st.error(f"❌ Gemini Error: {e}")
import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Configure Gemini
genai.configure(api_key=st.secrets.get("GEMINI_API_KEY"))

# Page setup
st.set_page_config(page_title="Gemini Chatbot", layout="wide")
st.title("💬 Gemini Chatbot (ChatGPT Style)")

# Model init
if "chat" not in st.session_state:
    model = genai.GenerativeModel("gemini-1.5-flash")
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Row with upload and chat input side-by-side (simulate + button)
col1, col2 = st.columns([1, 6])
with col1:
    uploaded_image = st.file_uploader("📎", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
with col2:
    prompt = st.chat_input("Ask something...")

# When user submits
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini reply
    try:
        if uploaded_image:
            image = Image.open(uploaded_image)
            response = st.session_state.chat.send_message([prompt, image])
        else:
            response = st.session_state.chat.send_message(prompt)

        reply = response.text

        with st.chat_message("assistant"):
            st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"❌ Gemini Error: {e}")
