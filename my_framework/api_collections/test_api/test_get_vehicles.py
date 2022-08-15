from requests import get
from http import HTTPStatus
import json
import allure
from my_framework.api_collections import config
from my_framework.api_collections.conftest import create_vehicles
from my_framework.api_collections.vehicles_api import VehiclesApi
from my_framework.api_collections.vehicles_data_class import Vehicles


def get_response_by_vehicles_id(vehicles_id):
    return get(f"{config.config['base_url']}api/vehicles/{vehicles_id}")


@allure.feature('Liubov Iarova')
def test_get_vehicles_response():
    response = get(f"{config.config['base_url']}/api/vehicles/4")
    assert response.status_code == HTTPStatus.OK, f'\nStatus is not as expected\nActual: {response.status_code}' \
                                                  f'\nExpected:{HTTPStatus.OK} '


@allure.feature('Liubov Iarova')
def test_not_found_error():
    response = get(f"{config.config['base_url']}/api/filmsss/1")
    assert response.status_code == HTTPStatus.NOT_FOUND, f'\nStatus is not as expected\nActual: {response.status_code}' \
                                                         f'\nExpected:{HTTPStatus.NOT_FOUND} '


@allure.feature('Liubov Iarova')
def test_response_json(create_vehicles):
    response = VehiclesApi().get_vehicles(vehicles_id=4)
    json_vehicles = json.loads(response.text)
    expected_vehicles = create_vehicles
    actual_vehicles = Vehicles(json_vehicles["name"], json_vehicles["model"], json_vehicles["max_atmosphering_speed"])
    assert actual_vehicles == expected_vehicles, f"\nVehicles as not expected"


@allure.feature('Liubov Iarova')
def test_name_value_vehicles_8():
    response = VehiclesApi().get_vehicles(vehicles_id=8)
    json_object = json.loads(response.text)
    assert json_object["name"] == "TIE/LN starfighter", f'\nPlace name is not as expected\nActual{json_object["name"]}' \
                                                        f'\nExpected:"TIE/LN starfighter"'


@allure.feature('Liubov Iarova')
def test_model_value_vehicles_8():
    response = VehiclesApi().get_vehicles(vehicles_id=8)
    json_object = json.loads(response.text)
    assert json_object["model"] == "Twin Ion Engine/Ln Starfighter", f'\nPlace name is not as expected\nActual' \
                                                                     f'{json_object["model"]}' \
                                                                     f'\nExpected:"Twin Ion Engine/Ln Starfighter"'
