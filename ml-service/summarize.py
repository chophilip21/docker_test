from transformers import AutoTokenizer
import requests
from transformers import pipeline
import json
import warnings

warnings.filterwarnings("ignore")


def summarize_random_news():
    """Summarizes a random news."""
    response = requests.get("http://127.0.0.1:8000")
    content = response.json()
    summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")
    summarized_content = summarizer(content["content"])

    # todo, as summary input, maybe use both title and content.
    actual_summary = summarized_content[0]["summary_text"]

    content["summary"] = actual_summary

    return content


if __name__ == "__main__":
    summary = summarize_random_news()
    print(summary)
