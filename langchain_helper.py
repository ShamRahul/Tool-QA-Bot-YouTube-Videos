# Import necessary libraries and modules
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

def create_db_from_youtube_video_url(video_url: str) -> FAISS:
    # Load YouTube video transcript using the provided URL
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()

    # Split the transcript into smaller chunks for processing
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    # Create a FAISS vector store from the split documents using the OpenAI embeddings
    db = FAISS.from_documents(docs, embeddings)
    return db

def get_response_from_query(db, query, k=8):
    """
    GPT-4 can handle up to 8192 tokens. Setting the chunksize to 1000 and k to 8 maximizes
    the number of tokens to analyze.
    """

    # Search for the most similar documents in the FAISS vector store based on the query
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    # Initialize the OpenAI model (GPT-4 in this case)
    llm = OpenAI(model_name="gpt-4", temperature=0.5)

    # Define a prompt template for the OpenAI model
    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        """,
    )

    # Create a chain for the OpenAI model using the defined prompt
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain to get a response based on the query and the most similar documents
    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response, docs
