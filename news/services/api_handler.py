import requests


class ApiHandler:
	def __init__(self, url) -> None:
		self.url = url

	def fetch_data(self):
		try:
			response = requests.get(self.url)
			return response.json()
		except requests.exceptions.RequestException as e:
			raise ValueError(f'Api request failed: {e}') from e
