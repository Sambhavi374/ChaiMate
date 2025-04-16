import streamlit as st
import openai

# Set up the Streamlit app
st.title("Guruji ka Chatbot")
st.subheader("Chat with Hitesh Sir's AI Model")
st.write("Enter your OpenAI API key to start chatting with the chatbot.")

# Input for API key
api_key = st.text_input("API Key", type="password")

# Check if API key is provided
if api_key:
    openai.api_key = api_key

    # Input for user question
    user_question = st.text_input("Ask a question to the chatbot:")

    if st.button("Submit"):
        if user_question.strip():
            try:
                # Call OpenAI API
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=user_question,
                    max_tokens=150
                )
                # Display the chatbot's response
                chatbot_response = response.choices[0].text.strip()
                st.write("Chatbot's Response:")
                st.write(chatbot_response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a question.")
else:
    st.warning("Please enter your API key to proceed.")