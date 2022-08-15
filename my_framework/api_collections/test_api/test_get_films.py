from requests import get
import pytest
from http import HTTPStatus
import json
import allure

from my_framework.api_collections import config
from my_framework.api_collections.films_api import FilmsApi
from my_framework.api_collections.films_data_class import Film


def get_response_us_by_episode_id(episode_id):
    return get(f"{config.config['base_url']}/api/films/{episode_id}")


@allure.feature('Liubov Iarova')
def test_get_film_response():
    response = get(f"{config.config['base_url']}/api/films/1")
    assert response.status_code == HTTPStatus.OK, f'\nStatus is not as expected\nActual: {response.status_code}'\
                                                  f'\nExpected:{HTTPStatus.OK} '


@allure.feature('Liubov Iarova')
def test_not_found_error():
    response = get(f"{config.config['base_url']}/api/filmsss/1")
    assert response.status_code == HTTPStatus.NOT_FOUND, f'\nStatus is not as expected\nActual: {response.status_code}'\
                                                         f'\nExpected:{HTTPStatus.NOT_FOUND} '


@allure.feature('Liubov Iarova')
def test_response_json(create_film):
    response = FilmsApi().get_films(episode_id=1)
    json_films = json.loads(response.text)
    expected_film = create_film
    actual_film = Film(json_films["director"], json_films["producer"], json_films["release_date"])
    assert actual_film == expected_film, f"\nPerson as not expected"


@allure.feature('Liubov Iarova')
def test_edited_episode_1():
    response = FilmsApi().get_films(episode_id=1)
    json_object = json.loads(response.text)
    assert json_object["edited"] == "2014-12-20T19:49:45.256000Z", f'\nPlace name is not as expected\nActual{json_object["edited"]}' \
                                                                   f'\nExpected:"2014-12-20T19:49:45.256000Z"'


@allure.feature('Liubov Iarova')
def test_title_episode_2():
    response = FilmsApi().get_films(episode_id=2)
    json_object = json.loads(response.text)
    assert json_object["title"] == "The Empire Strikes Back", f'\nPlace name is not as expected\nActual{json_object["title"]}' \
                                                              f'\nExpected:"The Empire Strikes Back"'


@allure.issue('test', 'Known issue')
def test_skip():
    pytest.skip('Not implemented!')


testdb=# insert into products (total) values ( products.price*orders.quantity FROM products, orders where products.id = orders.id order by id);
ERROR:  syntax error at or near "FROM"
LINE 1: ...s (total) values ( products.price*orders.quantity FROM produ...
                                                             ^
testdb=#  insert into products (total) SELECT products.price*orders.quantity FROM prod
ucts, orders where products.id = orders.id order by id;
ERROR:  column reference "id" is ambiguous
LINE 1: ... products, orders where products.id = orders.id order by id;
                                                                    ^
testdb=#  insert into products (total) SELECT products.price*orders.quantity FROM prod
ucts, orders where products.id = orders.id
testdb-#  insert into products (total) SELECT products.price*orders.quantity FROM products, orders where products.id = orders.id
testdb-#
