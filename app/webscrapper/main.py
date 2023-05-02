"""Simple scrapper that randomly scraps a website and gets sentences from it."""
from fastapi import FastAPI
from scrape import get_random_news
from summarize import summarize_random_news, Data
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/get/news", status_code=200)
async def get_news():
    """Simple get function that randomly fetches a news content."""
    return get_random_news()


@app.get("/api/v1/get/summary", status_code=200)
async def get_summary(data: Data):
    """Simple get function that randomly fetches a news content."""
    return summarize_random_news(data)


Instrumentator().instrument(app).expose(app)
