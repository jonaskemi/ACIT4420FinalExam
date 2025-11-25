import pytest
from smart_courier.validation import (validate_customer_name, validate_priority, validate_latitude, validate_longitude, validate_weight)

def test_validate_customer_name():
    # Valid test
    assert validate_customer_name("John Doe")
    
    # Invalid test
    assert not validate_customer_name("")

def test_validate_priority():
    # Valid test
    assert validate_priority("High")
    assert validate_priority("Medium")
    assert validate_priority("Low")

    # Invalid test
    assert not validate_priority("Urgent")

def test_validate_latitude():
    # Valid test
    assert validate_latitude(45.0)

    # Invalid test
    assert not validate_latitude(100.0)

def test_validate_longitude():
    # Valid test
    assert validate_longitude(-75.0)

    # Invalid test
    assert not validate_longitude(-200.0)

def test_validate_weight():
    # Valid test
    assert validate_weight(10.0)

    # Invalid test
    assert not validate_weight(-1.0)

if __name__ == "__main__":
    pytest.main()