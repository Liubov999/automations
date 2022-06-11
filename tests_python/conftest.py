import logging
import pytest

from tests_python.code_for_testing import Human

logger = logging.getLogger()
logger.setLevel('INFO')


@pytest.fixture()
def create_new_human():

    def human_factory(name, age, gender):
        return Human(name=name, age=age, gender=gender)
        yield human_factory
    logger.info(msg='Fixture finished')


@pytest.fixture()
def human_growing():
    logger.info(msg='Fixture start')
    yield Human(name='Ali', age=10, gender='female')
    logger.info(msg='Fixture finished')


@pytest.fixture()
def dead_man():
    logger.info(msg='Fixture start')
    yield Human(name='Ali', age=190, gender='male')
    logger.info(msg='Fixture finished')


@pytest.fixture()
def raising():
    logger.info(msg='Fixture start')
    yield Human
    logger.info(msg='Fixture finished')


@pytest.fixture()
def create_new_gender():
    logger.info(msg='Fixture start')
    yield Human
    logger.info(msg='Fixture finished')


@pytest.fixture()
def create_new_friends():

    logger.info(msg='Fixture start')

    def new_friend(name, age, gender):
        return Human(name=name, age=age, gender=gender)
        yield new_friend
    logger.info(msg='Fixture finished')



# @pytest.fixture()
# def growingg():
# logger.info(msg='Fixture start')
# yield Human(name='Ali', age=104, gender='female')
# logger.info(msg='Fixture finished')





#@pytest.fixture()
#def human_name():
    #logger.info(msg='Fixture start')
    #yield Human(name='Ali', age=104, gender='female')
    #logger.info(msg='Fixture finished')
