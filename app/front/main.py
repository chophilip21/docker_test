import streamlit as st
import pandas as pd
import requests

import os

# init sessionv variables
if "news" not in st.session_state:
    st.session_state.news = "Click the button to get news"

if "summary" not in st.session_state:
    st.session_state.summary = "Click the button to get summary"


# TODO:Fix the backend port logic by copying a file or something.
def display_news():
    """Called upon onclick of get_news_button"""
    if "BACKEND_PORT" not in os.environ:
        backend_port = 5000
    else:
        backend_port = str(os.getenv("BACKEND_PORT"))

    # get the news from backend
    response = requests.get(f"http://backend:{backend_port}/api/v1/get/news")

    # response successful return the data
    if response.status_code == 200:
        content = response.json()
        text = content["content"]
        title = content["title"]
        return f"{title}\n\n{text}"

    else:
        return "Port set properly, but backend did not respond with 200"


def get_summary():
    """Called upon onclick of summarize_button"""

    if st.session_state.news == "Click the button to get news":
        return "Get news first, and then ask to summarize"

    if "BACKEND_PORT" not in os.environ:
        backend_port = 5000
    else:
        backend_port = str(os.getenv("BACKEND_PORT"))

    # get the news from backend using json obj (based on Pydantic definition).
    json_obj = {"content": st.session_state.news}
    response = requests.get(
        f"http://backend:{backend_port}/api/v1/get/summary", json=json_obj
    )

    if response.status_code == 200:
        content = response.json()
        summary = content["summary"]
        return summary
    else:
        return "Port set properly, but backend did not respond with 200"


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
    get_news_button = st.button("Get News")
with col3:
    summarize_buttom = st.button("Summarize")
with col4:
    pass

if get_news_button:
    st.session_state.news = display_news()

if summarize_buttom:
    st.session_state.summary = get_summary()

st.header("News Article", help=None)
st.markdown(st.session_state.news)
st.divider()
st.subheader("Summary")
st.markdown(st.session_state.summary)
