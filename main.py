import streamlit as st
from src.utils import (
    get_pdf_text,
    get_text_chunks,
    get_vectorstore,
    get_conversation_chain,
)


def handle_input(question):
    response = st.session_state.conversation({"question": question})
    print(type(response), response["answer"])
    return response


def main():
    st.set_page_config("chat with pdfs", page_icon=":books:")
    st.header("Chat with pdfs :books:")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    user_question = st.chat_input("Ask a question about your documents")
    if user_question:
        st.session_state.messages.append({"role": "user", "message": user_question})
        st.session_state.messages.append(
            {"role": "assistant", "message": handle_input(user_question)["answer"]}
        )
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["message"])

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs", type="pdf", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                # get reads of the pdfs
                raw_text = get_pdf_text(pdf_docs)
                # transform readed pdfs into chunks
                chunks = get_text_chunks(raw_text)
                # create vector store
                vectorstore = get_vectorstore(chunks)
                # create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)


if __name__ == "__main__":
    main()
