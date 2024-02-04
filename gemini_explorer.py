import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, ChatSession

# Initialize Gemini model
project = "gemini_explorer"
vertexai.init(project=project)
config = generative_models.GenerationConfig(temperature=0.4)
model = GenerativeModel("gemini-pro", generation_config=config)
chat = model.start_chat()

# List to store chat history
chat_history = []

# Function to send messages
def send_message(message):
    # Add the message to the chat history
    chat_history.append(message)
    # Display the message in the app
    st.write(message)

# Function to interact with the Gemini model
def process_user_input(user_input):
    # Use the Gemini model to generate a response based on user input
    response = chat.continue_chat(user_input)
    # Add the user input and the model's response to the chat history
    send_message(f"User: {user_input}")
    send_message(f"Aurora: {response}")

# Initial prompt
user_name = st.text_input("Please enter your name")

# Ensure that chat_history is initialized
if len(chat_history) == 0:
    initial_prompt = f"Hey {user_name}! I'm Aurora, an assistant powered by Google Gemini. Let's explore together! 🚀"
    send_message(initial_prompt)

# Display chat history
for message in chat_history:
    st.write(message)
# User input
query = st.text_input("Gemini explorer")
if query:
    # Process user input and update chat history
    process_user_input(query)
