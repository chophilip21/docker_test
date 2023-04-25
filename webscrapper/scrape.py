import requests
from bs4 import BeautifulSoup
import numpy as np
import re
import random


def get_random_news():
    url = "https://www.dailymail.co.uk"
    r1 = requests.get(url)

    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, "html5lib")
    coverpage_news = soup1.find_all("h2", class_="linkro-darkred")

    list_links = []

    # choose a random number
    n = random.randint(0, len(coverpage_news))

    final_data = {}
    list_links = []

    # Getting the link of the article
    link = url + coverpage_news[n].find("a")["href"]
    list_links.append(link)

    # Getting the title
    title = coverpage_news[n].find("a").get_text()

    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, "html5lib")
    body = soup_article.find_all("p", class_="mol-para-with-font")

    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(body)):
        paragraph = body[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)

    # Removing special characters
    final_article = re.sub("\\xa0", "", final_article)

    final_data["title"] = title.strip()
    final_data["content"] = final_article

    return final_data


if __name__ == "__main__":
    test = get_random_news()
