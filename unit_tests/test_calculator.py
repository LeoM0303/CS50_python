from calculator import square
import pytest

def main():
    test_positive()
    test_negative()
    test_zero()
    test_str()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    assert square(6) == 36

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-5) == 25
    assert square(-6) == 36

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# Run the test