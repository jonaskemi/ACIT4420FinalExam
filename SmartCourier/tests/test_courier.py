import pytest
from smart_courier.validation import (validate_customer_name, validate_priority, validate_latitude, validate_longitude, validate_weight)

def test_validate_customer_name():
    assert validate_customer_name("John Doe")
    #assert not validate_customer_name("John123")

def test_validate_priority():
    #assert validate_priority("High")
    assert validate_priority("Urgent")

def test_validate_latitude():
    #assert validate_latitude(45.0)
    assert  validate_latitude(100.0)

def test_validate_longitude():
    #assert validate_longitude(-75.0)
    assert validate_longitude(-200.0)

def test_validate_weight():
    #assert validate_weight(10.0)
    assert validate_weight(-1.0)

if __name__ == "__main__":
    pytest.main()