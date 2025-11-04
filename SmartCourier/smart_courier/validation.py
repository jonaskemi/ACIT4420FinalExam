import re

PRIORITY_PATTERN = re.compile(r'^(High|Medium|Low)$')
CUSTOMER_NAME_PATTERN = re.compile(r'^[\x20-\x7E]+$')

def validate_priority(value):
    """Validate that the priority is one of the accepted values. Added case sensitivity handling."""
    return isinstance(value, str) and bool(PRIORITY_PATTERN.match(value.capitalize()))

def validate_customer_name(value):
    """Validate that the customer name is valid."""
    return isinstance(value, str) and bool(CUSTOMER_NAME_PATTERN.match(value))

def validate_latitude(value):
    """Validate that the latitude is within valid range."""
    try:
        lat = float(value)
        return -90 <= lat <= 90
    except (ValueError, TypeError):
        return False

def validate_longitude(value):
    """Validate that the longitude is within valid range."""
    try:
        lon = float(value)
        return -180 <= lon <= 180
    except (ValueError, TypeError):
        return False
    
def validate_weight(value):
    """Validate that the weight is a positive number."""
    try:
        weight = float(value)
        return weight > 0
    except (ValueError, TypeError):
        return False

