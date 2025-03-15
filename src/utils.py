from typing import Generator
import streamlit as st

def init_session_state(openai_model: str) -> None:
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = openai_model

    if "messages" not in st.session_state:
        st.session_state.messages = []

def show_messages() -> None:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def to_stream(stream) -> Generator[str, None, None]:
    for response in stream:
        if hasattr(response, "delta"):
            yield response.delta