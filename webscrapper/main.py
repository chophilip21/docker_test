"""Simple scrapper that randomly scraps a website and gets sentences from it."""
from fastapi import FastAPI
from scrape import get_random_news

app = FastAPI()


@app.get("/")
async def root():
    """Simple get function that randomly fetches a news content."""
    return get_random_news()
