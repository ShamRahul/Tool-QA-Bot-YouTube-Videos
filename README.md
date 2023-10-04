# 🦜🔗 QA BOT - YOUTUBE

This project serves as a tool to answer queries based on YouTube video transcripts. It leverages the power of OpenAI, LangChain, and Streamlit to provide a user-friendly interface where users can input a YouTube video URL and ask questions related to the video's content.

## 🌟 Features

- **YouTube Video Transcript Extraction**: Extracts the transcript of a given YouTube video.
- **Query Resolution**: Resolves user queries based on the extracted transcript using OpenAI models.
- **User-friendly Interface**: Provides a user-friendly interface through Streamlit for easy interaction.

## 🚀 How to Run

### 🛠️ Prerequisites

- Python installed on your system. (Preferably Python 3.8)
- Basic knowledge of Python programming.
- Streamlit, LangChain, OpenAI, and other necessary libraries installed.

### 🛠️ Setup & Installation

1. Clone the Repository:
   ```sh
   git clone <repository-url>
   cd <repository-dir>
2. Install Necessary Libraries
   ```sh
   pip install streamlit langchain openai youtube-transcript-api faiss-cpu
3. Run the streamlit app
   ```sh
   streamlit run <script-name>.py
   
## 📘 How to Use

- **Input YouTube Video URL**: Use the sidebar to input the YouTube video URL.
- **Ask a Question**: Input your query related to the video in the provided text area.
- **Provide OpenAI API Key**: Input your OpenAI API key.
- **Submit**: Click the submit button to get the response based on the video's transcript.

## 📚 Behind the Scenes

The system utilizes the LangChain library to interact with OpenAI models. The YouTube video's transcript is extracted and then split into manageable chunks. These chunks are used to create a vector store for efficient similarity search. When a user asks a question, the system searches for the most relevant chunks from the transcript and then uses an OpenAI model to generate a detailed answer based on the relevant chunks.

## 🙏 Acknowledgements

Special thanks to the creators of LangChain, OpenAI, and Streamlit for their amazing libraries and frameworks. Many thanks to freeCodeCamp.org for amazing tutorials. 

## 🤝 Contributing

Feel free to fork the project, make changes, and open a pull request if you think your changes should be included in the main project.

