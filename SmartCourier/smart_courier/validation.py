import re

PRIORITY_PATTERN = re.compile(r'^(High|Medium|Low)$')
CUSTOMER_NAME_PATTERN = re.compile(r'^[\x20-\x7E]+$')

def validate_priority(value):
    return isinstance(value, str) and bool(PRIORITY_PATTERN.match(value.capitalize()))

def validate_customer_name(value):
    return isinstance(value, str) and bool(CUSTOMER_NAME_PATTERN.match(value))

def validate_latitude(value):
    try:
        lat = float(value)
        return -90 <= lat <= 90
    except (ValueError, TypeError):
        return False

def validate_longitude(value):
    try:
        lon = float(value)
        return -180 <= lon <= 180
    except (ValueError, TypeError):
        return False
    
def validate_weight(value):
    try:
        weight = float(value)
        return weight > 0
    except (ValueError, TypeError):
        return False

