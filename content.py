from datetime import datetime, timedelta

from news import News

yesterday = str((datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"))
print(yesterday)
news = News(list_of_topics=['IMSA', 'FIA WEC'], from_date=yesterday)
file_path = 'daily_news.txt'

def create_file():
    try:
        with open(file_path, 'w') as file:
            for i, all_articles in enumerate(news.get_top_ten_articles()):
                file.write(f'News for topic {news.list_of_topics[i]}' + '\n')
                for article in all_articles:
                    title = news.get_title(article)
                    file.write(f'Title: {title}' + '\n')
                    description = news.get_description(article)
                    file.write(f'Description: {description}' + '\n')
                    url = news.get_url(article)
                    file.write(f'Url: {url}' + '\n')
                file.write('\n')
    except IOError as e:
        print(f"An error occurred: {e}")




