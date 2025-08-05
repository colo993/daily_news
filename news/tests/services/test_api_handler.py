import pytest
from news.services.api_handler import ApiHandler


@pytest.fixture
def mock_item_data():
	return {'name': 'test_topic', 'max_news_per_day': 2, 'keywords': 'test_key1, test_key2'}


@pytest.fixture
def mock_list_data():
	return [
		{'name': 'test_topic1', 'max_news_per_day': 2, 'keywords': 'test_key1, test_key2'},
		{'name': 'test_topic2', 'max_news_per_day': 2, 'keywords': 'test_key3, test_key4'},
	]


class TestApiHandler:
	def test_fetch_data_with_success(self, mocker, mock_item_data):
		mock_response = mocker.Mock()
		mock_response.json.return_value = mock_item_data
		# prevent rising an exception, since it is test with success response
		mock_response.raise_for_status.return_value = None

		get_mock = mocker.patch(
			'news.services.api_handler.requests.get', return_value=mock_response
		)  # ignore 501
		handler = ApiHandler(url='https://news.example.com')

		data = handler.fetch_data()

		assert data == mock_item_data
		get_mock.assert_called_once()
		get_mock.assert_called_once_with('https://news.example.com')

	def fetch_data_with_error(self):
		# use in mock_response.raise_for_status.side_effect = HTTPError('404 Not Found')
		pass

	def fetch_data_with_network_error(self):
		# use side effect = RequestException
		pass
