import pytest
import logger

from tests_python.code_for_testing import Human


@pytest.mark.regression
def test_parameters(create_new_human):
    """"
    Descriptions: test check that Human name return name, age return age, gender return gender
    Steps:
    1. Create human_new1
    2. create human_new2 equal human_new1
    3. create human_new3 equal human_new2

    Expected: name return name, age return age, gender return gender
    """
    human_new1 = Human(name='Koko', age=18, gender='female')
    human_new2 = human_new1
    human_new3 = human_new2

    assert human_new1.name == 'Koko', f'\n Name is not expected\nActual: {human_new1.name}\nExpected:Koko'
    assert human_new2.age == 18, f'\n Age is not expected\nActual: {human_new2.age}\nExpected:18'
    assert human_new3.gender == 'female', f'\n Age is not expected\nActual: {human_new3.gender}\nExpected:female'


@pytest.mark.smoke
def test_growing(human_growing):
    """"
       Descriptions: test check if age less than age limit add to age 1-year
       Steps:
       1. Create person
       2. Call grow func

     Expected: add to age 1-year
       """
    person = human_growing
    person.grow()
    assert person.age < 105, f"\n Age should be less then 105\nActual: {person.age}\nExpected: < 105"


@pytest.mark.smoke
def test_change_status(dead_man):
    """"
         Descriptions: test check if age more than age limit change status to dead
         Steps:
         1. Create dead_man with age more than age limit
         2. Call grow func

       Expected: status is dead
         """
    dead_man.grow()
    print(dead_man.status)
    assert not dead_man.age < 105 and dead_man.status == 'dead', f"\n Age should be bigger then 105 and status should " \
                                                                 f"be changes to dead \nActual: {dead_man.age}< 1" \
                                                                 f"05,{dead_man.status}\nExpected: {dead_man.age} !<105," \
                                                                 f"{dead_man.status} "


@pytest.mark.skip  # doesn't work
def test_name_validations(raising):
    person = Human(name='koko', age=18, gender='female')
    print(person.name)
    assert person.name[0].isupper() and len(person.name) < 10, f'\n Name should starts with capital letter and less than\nActual:{person.name}, less than 10 symbols\nExpected:K..., more than 10 symbols  '


@pytest.mark.regression
def test_new_gender(create_new_gender):
    """"
             Descriptions: test check if gender is not male or female raise Error
             Steps:
             1. Create person2
             2. Change status to it

           Expected: shows error 'Gender is not as expected'
             """

    person2 = Human(name='Koko', age=18, gender='female')
    person2.gender = "it"
    assert person2.gender == 'male' or 'female', f'\n Gender is not valid\nActual:{person2.gender}\nExpected:male or ' \
                                                 f'female '


@pytest.mark.skip  # doesn't work
def test_get_friends(create_new_friends):
    new_friend = create_new_friends(name='Rob', age=18, gender='female')
    new_friend2 = create_new_friends(name='Karl', age=18, gender='female')
    friends = []
    new_friend.status()
    print(friends)
    assert friends == [new_friend, new_friend2]
