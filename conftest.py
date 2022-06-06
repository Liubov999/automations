import logging
import pytest

from code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.fixture()
def human_dead():
    logger.info(msg='Fixture start')
    yield Human(name='Lily', age=104, gender='female')
    logger.info(msg='Fixture finished')

@pytest.fixture()
def human_name():
    logger.info(msg='Fixture start')
    yield Human(name='Ali', age=104, gender='female')
    logger.info(msg='Fixture finished')





@pytest.fixture()
def create_custom_human():
    def human_factory(name, age, gender):
        return Human(name=name, age=age, gender=gender)

    yield human_factory
