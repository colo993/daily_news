import httpx


class ApiHandler:
	def __init__(self, url) -> None:
		self.url = url

	def fetch_data(self):
		try:
			response = httpx.get(self.url)
			return response.json()
		except httpx.RequestError as e:
			raise ValueError(f'Api request failed: {e}') from e
