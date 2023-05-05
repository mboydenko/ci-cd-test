import allure

from time import sleep


from src.math_operations import sum, minus, divide


@allure.suite('Test sum')
@allure.description("Testing sum")
def test_sum():
    with allure.step('Testing sum of 5 and 5 equals 11'):
        sleep(5)
        assert sum(5, 5) == 10, 'Invalid result'
    with allure.step('Testing sum of 5 and 5 equals 11'):
        sleep(5)
        assert sum(5, 6) == 11, 'Invalid result'
    with allure.step('Testing sum of 5 and 5 equals 11'):
        sleep(5)
        assert sum(4, -5) == -1, 'Invalid result'


def test_minus():
    sleep(5)
    assert minus(5, 5) == 0, 'Invalid result'
    sleep(5)
    assert minus(5, 6) == -1, 'Invalid result'
    sleep(5)
    assert minus(4, -5) == 9, 'Invalid result'


def test_divide():
    sleep(5)
    assert divide(5, 5) == 1, 'Invalid result'
    sleep(5)
    assert divide(12, 6) == 2, 'Invalid result'
