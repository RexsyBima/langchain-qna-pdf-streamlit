from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_community.embeddings.huggingface_hub import HuggingFaceHubEmbeddings


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for p in pdf_reader.pages:
            text += p.extract_text()
    return text


def get_text_chunks(raw_text):
    splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = splitter.split_text(raw_text)
    return chunks


def get_vectorstore(text_chunks):
    embedding = OpenAIEmbeddings(disallowed_special=())
    # embedding = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    # embedding = HuggingFaceHubEmbeddings(repo_id="BAAI/bge-large-zh-v1.5")
    vectorstore = FAISS.from_texts(text_chunks, embedding)
    return vectorstore


def get_conversation_chain(vectorstore: FAISS):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        ChatOpenAI(), retriever=vectorstore.as_retriever(), memory=memory
    )
    return conversation_chain


list_of_text = [
    """In this book, I invite you to embark on an educational journey with me to learn how
to build Large Language Models (LLMs) from the ground up. Together, we'll delve deep
into the LLM training pipeline, starting from data loading and culminating in finetuning
LLMs on custom datasets.""",
    """
For many years, I've been deeply immersed in the world of deep learning, coding
LLMs, and have found great joy in explaining complex concepts thoroughly. This book
has been a long-standing idea in my mind, and I'm thrilled to finally have the opportunity
to write it and share it with you. Those of you familiar with my work, especially from my
blog, have likely seen glimpses of my approach to coding from scratch. This method has
resonated well with many readers, and I hope it will be equally effective for you.""",
    """I've designed the book to emphasize hands-on learning, primarily using PyTorch and
without relying on pre-existing libraries. With this approach, coupled with numerous
figures and illustrations, I aim to provide you with a thorough understanding of how LLMs
work, their limitations, and customization methods. Moreover, we'll explore commonly
used workflows and paradigms in pretraining and fine-tuning LLMs, offering insights into
their development and customization.
""",
]
