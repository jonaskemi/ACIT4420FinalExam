from .validation import (validate_customer_name, validate_priority, validate_latitude, validate_longitude, validate_weight)
import csv

def validate_inputs(deliveries_file):
    with open(deliveries_file, 'r') as f:
        lines = f.read().splitlines()[1:] 
    
    for line in lines:
        customer, latitude, longitude, priority, weight_kg = line.split(',')
        
        if (validate_customer_name(customer) and
            validate_latitude(float(latitude)) and
            validate_longitude(float(longitude)) and
            validate_priority(priority) and
            validate_weight(float(weight_kg))):
                with open('output/valid.csv', 'a', newline='') as validfile:
                    writer = csv.writer(validfile)
                    writer.writerow([customer, latitude, longitude, priority, weight_kg])
                print(f"valid: {line}")
        else:
            with open('output/rejected.csv', 'a', newline='') as rejectedfile:
                writer = csv.writer(rejectedfile)
                writer.writerow([customer, latitude, longitude, priority, weight_kg])
            print(f"Invalid: {line}")
            
def view_csv_file(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    # Welcome message and user prompt and check file existence
    print("\nHello! Welcome to Smart Courier!")
    deliveries_file = input("\nEnter the path to the deliveries file (press enter to use data/deliveries.csv): \n")
    try:
        if not deliveries_file:
            deliveries_file = 'data/deliveries.csv'
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    view_csv_file(deliveries_file)
    
    # Validation confirmation
    print("\nDo you wish to validate the deliveries from file:", deliveries_file, "?")  
    confirm = input("Type 'yes' to confirm, or anything else to exit: ")
    if confirm.lower() != 'yes':
        print("Exiting the program.")
        return
    try:
        validate_inputs(deliveries_file=deliveries_file)
        print("\nValidation complete. These are valid deliveries: output/valid.csv")
        view_csv_file('output/valid.csv')
    except Exception as e:
        print(f"An error occurred during validation: {e}")
        return
    
    # View rejected deliveries or continue to optimizer?
    print("\nDo you wish to view the rejected deliveries?")
    view_rejected = input("Type 'yes' to view rejected deliveries, or anything else to exit: ")
    if view_rejected.lower() == 'yes':
        print("\nThese are the rejected deliveries: output/rejected.csv")
        view_csv_file('output/rejected.csv')
    print("\nOkay! Do you wish to continue to the optimizer?")
    continue_optimizer = input("Type 'yes' to continue to the optimizer, or anything else to exit: ")
    if continue_optimizer.lower() == 'yes':
        print("Continuing to the optimizer... (Functionality not yet implemented)")
    
if __name__ == "__main__":
    main()