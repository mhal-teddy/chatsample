import streamlit as st

pages = [
    st.Page("src/chat.py", title="Chat", url_path="chat"),
    st.Page("src/web_search.py", title="Web Search", url_path="web_search")
]

pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()