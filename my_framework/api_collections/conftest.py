import pytest

from my_framework.api_collections.films_data_class import Film
from my_framework.api_collections.vehicles_data_class import Vehicles


@pytest.fixture
def create_film():
    return Film("George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25")


@pytest.fixture
def create_vehicles():
    return Vehicles("Sand Crawler", "Digger Crawler", "30")



