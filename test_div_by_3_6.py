import pytest

def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

def test_div_rais_exception(input_value):
    with pytest.raises(ZeroDivisionError):
        assert input_value / 0