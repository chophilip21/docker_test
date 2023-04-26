import streamlit as st
import pandas as pd
import requests
import json
import uuid


# init sessionv variables
if "news" not in st.session_state:
    st.session_state.news = "Click the button to get news"

if "summary" not in st.session_state:
    st.session_state.summary = "Click the button to get summary"


def display_news():
    """Called upon onclick of get_news_button"""

    txt = str(uuid.uuid4())
    return txt


def get_summary():
    """Called upon onclick of summarize_button"""

    txt = str(uuid.uuid4())
    return txt


st.title("Summarize News using AI 🤖")

st.markdown(
    "Microservice test application using FastAPI (backend), HuggingFace (inference), and Streamlit(frontend). Using Docker Compose to turn into microservice. To get a news article, hit the Get News Article. To summarize the article, hit the Summarize button.",
    unsafe_allow_html=False,
    help=None,
)

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

col1, col2, col3, col4 = st.columns(4)


with col1:
    pass
with col2:
    get_news_button = st.button("Get News", on_click=display_news)
with col3:
    summarize_buttom = st.button("Summarize")
with col4:
    pass

if get_news_button:
    st.session_state.news = display_news()

if summarize_buttom:
    st.session_state.summary = get_summary()

st.header("News Article", help=None)
st.code(st.session_state.news, language="python")
st.divider()
st.subheader("Summary")
st.code(st.session_state.summary, language="python")
