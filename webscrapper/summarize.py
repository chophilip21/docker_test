from transformers import pipeline
import warnings
from pydantic import BaseModel

warnings.filterwarnings("ignore")


class Data(BaseModel):
    """Data model for the summary. Keep it simple."""

    content: str


def summarize_random_news(content: Data) -> dict:
    """Summarizes a random news."""
    summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")
    summarized_content = summarizer(content.content)
    actual_summary = summarized_content[0]["summary_text"]

    return {"summary": actual_summary}


if __name__ == "__main__":
    summary = summarize_random_news()
    print(summary)
