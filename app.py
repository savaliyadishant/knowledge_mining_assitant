import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Set your Gemini API key (can be read from secrets or environment for safety)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the multimodal Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="Gemini Chat", layout="centered")
st.title("🧠 Gemini-Powered Chatbot (Text + Image)")

# Session state to store conversation
if "history" not in st.session_state:
    st.session_state.history = []

uploaded_image = st.file_uploader("Upload an image (optional)", type=["png", "jpg", "jpeg"])
user_input = st.text_input("Ask something...", key="prompt")

if st.button("Send") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    
    try:
        if uploaded_image:
            image = Image.open(uploaded_image)
            response = model.generate_content([user_input, image])
        else:
            response = model.generate_content(user_input)
        
        st.session_state.history.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")

# Display the conversation history
for msg in st.session_state.history:
    st.markdown(f"**{msg['role'].capitalize()}:** {msg['content']}")
