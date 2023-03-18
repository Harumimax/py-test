import pytest
from kassa.utils import get_change

def test_get_change_easy():
    price = "8000"
    paid = "5000 5000"
    get_change(price, paid)
    assert result == "1000 1000"

def test_get_change_hard():
    price = "5463"
    paid = "5000 5000"
    get_change(price, paid)
    assert result == "1000 1000 1000 1000 500 10 10 10 5 2"

def test_get_change_float():
    price = "10.34"
    paid = "10 10"
    get_change(price, paid)
    assert result == "5 2 2 0.5 0.1 0.05 0.01"

def test_get_change_error():
    price = "2"
    paid = "1"
    with pytest.raises(ValueError):
        get_change(price, paid)
