from .validation import (validate_customer_name, validate_priority, validate_latitude, validate_longitude, validate_weight)

def validate_inputs(deliveries_file='data/deliveries.csv'):
    with open(deliveries_file, 'r') as f:
        lines = f.read().splitlines()[1:] 
    
    for line in lines:
        customer, latitude, longitude, priority, weight_kg = line.split(',')
        
        if (validate_customer_name(customer) and
            validate_latitude(float(latitude)) and
            validate_longitude(float(longitude)) and
            validate_priority(priority) and
            validate_weight(float(weight_kg))):
            print(f"valid: {line}")
        else:
            print(f"Invalid: {line}")

def main():
    validate_inputs()

if __name__ == "__main__":
    main()