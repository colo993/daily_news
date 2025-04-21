from news import get_top_ten_articles

FILE_NAME = 'daily_news.txt'
topics = ['IMSA', 'FIA WEC', 'Fanatec GT World Challenge']


def create_file_with_content():
	try:
		with open(FILE_NAME, 'w') as file:
			for topic in topics:
				file.write(f'<h1>News for topic {topic}</h1>' + '\n')
				for article in get_top_ten_articles(topic):
					file.write(f'<b>Title</b>: {article["title"]}' + '\n')
					file.write(f'<b>Description</b>: {article["description"]}' + '\n')
					file.write(f'<b>Url</b>: {article["url"]}' + '\n')
					file.write('<hr width="100%" size="1"')
				file.write('\n')
	except IOError as e:
		print(f'Unable to open file: {FILE_NAME}.\nError: {e}')
