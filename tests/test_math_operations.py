from time import sleep

from src.math_operations import sum, minus, divide


def test_sum():
    sleep(5)
    assert sum(5, 5) == 10, 'Invalid result'
    sleep(5)
    assert sum(5, 6) == 11, 'Invalid result'
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
