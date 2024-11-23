import os
from datetime import datetime, timedelta
from typing import List

from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

API_KEY = os.environ["API_KEY"]
NEWS_API = NewsApiClient(api_key=API_KEY)
AMOUNT_OF_NEWS = 10
ORDER_OF_ARTICLES = "relevancy"
YESTERDAY = str((datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"))

def get_top_ten_articles(topic: str) -> list:
    """Return a list 
    of 10 dictionaries with news.
    """
    top_ten_news = NEWS_API.get_everything(
                q=topic,
                from_param=YESTERDAY,
                language='en',
                page_size=AMOUNT_OF_NEWS,
                sort_by=ORDER_OF_ARTICLES
            )
    return top_ten_news['articles']
