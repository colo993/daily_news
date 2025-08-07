import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = 'https://newsdata.io/api/1/latest'


def get_parameter(name: str, value: str | None = None) -> None | str:
	return f'{name}={value}' if value else None

# add def compose_parameters and pass it to build URL
# adjust tests

def build_url(parameters: list) -> str:
	api_key = os.getenv('API_KEY')
	if not api_key:
		raise ValueError('API_KEY environment variable not set')
	all_parameters = '&'.join(parameters)
	return f'{BASE_URL}?apikey={api_key}&{all_parameters}'
