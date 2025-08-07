import pytest

from news.services.url_builder import get_parameter, build_url


@pytest.mark.parametrize(
	'name, value, expected',
	[
		('param1', 'value1', 'param1=value1'),
		('param2', 'test1,test2', 'param2=test1,test2'),
		('param3', '1', 'param3=1'),
		('param4', '', None),
		('param5', None, None),
	],
)
def test_get_parameter(name, value, expected):
	parameter = get_parameter(name=name, value=value)
	assert parameter == expected


@pytest.mark.parametrize(
	'parameters, expected',
	[(['param1=value1', 'param2=value2'], 'https://test-api.example.com?apikey=Test_Api_Key&param1=value1&param2=value2')],
)
def test_build_url(monkeypatch, parameters, expected):
	monkeypatch.setattr('news.services.url_builder.BASE_URL', 'https://test-api.example.com'),
	monkeypatch.setenv('API_KEY', 'Test_Api_Key')
	url = build_url(parameters=parameters)
	assert url == expected
