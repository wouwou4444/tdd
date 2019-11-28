import pytest

@pytest.mark.xfail
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.xfail
@pytest.mark.vbe
def test_greater_equal():
    num = 100
    assert num >= 100
    
@pytest.mark.skip
@pytest.mark.vbe
def test_less():
    num = 100
    assert num < 200