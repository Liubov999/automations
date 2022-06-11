import pytest


def test_status(human_status):
    human_status.status = 'alive'
    assert human_status.status == 'alive'


def test_status_negative(human_status):
    human_status.status = 'dead'
    assert human_status.status == 'alive'


def test_age(age_test):
    age_test.age = int
    assert age_test.age == int


def test_age_negative(age_test):
    age_test.age = str, bool
    assert age_test.age == int

def test_grow(growing):
    growing.age


def test_my(human_dead):
    print("\nTEST START")
    print(human_dead.age)
    human_dead.age = 2
    print(human_dead.age)
    #assert human_dead.age == 106, f"ERROR"


def test_type(human_name):
    logger.info('\nTEST START')
    human3 = human_name
    human3.name = 11
    assert human3.name is not str, f'Error'

    # def test_name(new_name):
    print("\nTEST START")
    new_name.name = 'kotik'
    print(new_name)
    if not (new_name[0].isupper() and not (len(new_name) < 10)):
        raise SyntaxError('Name should starts with capital letter')
    assert new_name < 10

    # def test_name(name_test):
    # print("\nTEST START")
    # name_test.name = str
    # assert name_test.name == str

    # def test_name_negative(name_test):
    print("\nTEST START")
    name_test.name = int
    assert name_test.name == str

    ##def test_status_negative(human_status):
    print("\nTEST START")
    human_status.status = 'dead'
    assert human_status.status == 'alive'

    # def test_age(age_test):
    print("\nTEST START")
    age_test.age = int
    assert age_test.age == int

    # def test_age_negative(age_test):
    print("\nTEST START")
    age_test.age = str, bool
    assert age_test.age == int

    # def test_gender(gender_test):
    print("\nTEST START")
    gender_test.gender = str
    assert gender_test.gender == str

    # def test_gender_negative(gender_test):
    print("\nTEST START")
    gender_test.gender = int
    assert gender_test.gender == str

    # def test_name(new_name):
    print("\nTEST START")
    new_name.name = 'kotik'
    print(new_name)
    if not (new_name[0].isupper() and not (len(new_name) < 10)):
        raise SyntaxError('Name should starts with capital letter')
    assert new_name < 10

    # def test_error(gender_test):
    print("\nTEST START")
    gender_test.gender = 11
    if gender_test.gender == str:
        print('success')
    else:
        raise Exception
    assert gender_test.gender != str


def test_grow(growing):
    print("\nTEST START")
    growing.grow()
    print(growing.status)
    if growing.age < 104:
        print(growing.status)
    assert growing.status == 'alive'


def test_my(human_dead):
    print("\nTEST START")
    print(human_dead.age)
    human_dead.age = 2
    print(human_dead.age)
    # assert human_dead.age == 106, f"ERROR"


def test_type(human_name):
    logger.info('\nTEST START')
    human3 = human_name
    human3.name = 11
    assert human3.name is not str, f'Error'