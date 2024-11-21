import os
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()

API_KEY = os.environ["API_KEY"]
NEWS_API = NewsApiClient(api_key=API_KEY)


class News:

    AMOUNT_OF_NEWS = 10
    ORDER_OF_ARTICLES = "relevancy"

    def __init__(
        self, list_of_topics: List, from_date: datetime, language: str = "en"
    ) -> None:
        self.list_of_topics = list_of_topics
        self.from_date = from_date
        self.language = language

    def get_top_ten_articles(self) -> List:
        top_ten_articles = []
        for topic in self.list_of_topics:
            all_news = NEWS_API.get_everything(
                q=topic,
                from_param=self.from_date,
                language=self.language,
                page_size=self.AMOUNT_OF_NEWS,
                sort_by=self.ORDER_OF_ARTICLES
            )
            top_ten_articles.append(all_news.get("articles"))
        return top_ten_articles
    
    def get_title(self, news: dict) -> str:
        return news.get("title")

    def get_description(self, news: dict) -> str:
        return news.get("description")

    def get_url(self, news: dict) -> str:
        return news.get("url")
