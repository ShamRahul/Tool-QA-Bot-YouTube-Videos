# Import necessary libraries and modules
import streamlit as st
import langchain_helper as lch
import textwrap

# Set the title of the Streamlit app
st.title("QA BOT - YOUTUBE")

# Create a sidebar for user input
with st.sidebar:
    # Create a form within the sidebar to group the input fields
    with st.form(key='my_form'):
        # Text area for users to input the YouTube video URL
        youtube_url = st.sidebar.text_area(
            label="What is the YouTube video URL?",
            max_chars=50
        )
        # Text area for users to input their query about the video
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )
        # Text input for users to provide their OpenAI API key
        openai_api_key = st.sidebar.text_input(
            label="OpenAI API Key",
            type="password",
        )

# Check if both the YouTube URL and the query are provided
if query and youtube_url:
    # If the OpenAI API key is not provided, display an informational message
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        # If all inputs are provided, create a database from the YouTube video URL
        db = lch.create_db_from_youtube_video_url(youtube_url)
        # Get a response to the query based on the created database
        response, docs = lch.get_response_from_query(db, query)
        # Display the response in the Streamlit app
        st.subheader("Answer:")
        st.text(textwrap.fill(response))
