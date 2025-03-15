from openai import OpenAI
import streamlit as st
from src.utils import init_session_state, show_messages, to_stream

st.title("Chat with LLM")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

init_session_state("gpt-4o-mini")
show_messages()

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    stream = client.responses.create(
        model=st.session_state["openai_model"],
        input=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state["messages"]
        ],
        stream=True,
    )
    with st.chat_message("assistant"):
        response = st.write_stream(to_stream(stream))
    st.session_state.messages.append({"role": "assistant", "content": response})