from src.math_operations import sum, minus


def test_sum():
    assert sum(5, 5) == 10, 'Invalid result'
    assert sum(5, 6) == 11, 'Invalid result'
    assert sum(4, -5) == -1, 'Invalid result'


def test_minus():
    assert minus(5, 5) == 0, 'Invalid result'
    assert minus(5, 6) == -1, 'Invalid result'
    assert minus(4, -5) == 9, 'Invalid result'
