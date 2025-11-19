from .validation import (validate_customer_name, validate_priority, validate_latitude, validate_longitude, validate_weight)
from .optimizer import optimizer
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
            
def run_optimizer():
    optimizer('output/valid.csv')
            
def view_csv_file(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def main():
    while True: 
        print("\n==============================")
        print(" Smart Courier Main Menu ")
        print("==============================")
        print("1. Start Validation and Optimization Process")
        print("2. Reset Output Files (recommended before new runs)")
        print("3. Exit")
        choice = input("\nPlease enter your choice (1-3): ")
        
        # Start validation process
        if choice == '1':
            deliveries_file = input("\nEnter the path to the deliveries file (press enter to use data/deliveries.csv): \n")
            try:
                if not deliveries_file:
                    deliveries_file = 'data/deliveries.csv'
            except FileNotFoundError:
                print("File not found. Please check the path and try again.")
                print("==============================")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("==============================")
                break
            view_csv_file(deliveries_file)
            
            # Validation confirmation
            try:
                print("\nDo you wish to validate the deliveries from file:", deliveries_file, "?")
                confirm = input("Type 'yes' to confirm, or anything else to return to exit: ")
            
                if confirm.lower() != 'yes':
                    print("Exiting the program.")
                    print("==============================")
                    break
                elif confirm.lower() == 'yes':
                    print("Validating.\n")
                    validate_inputs(deliveries_file=deliveries_file)
                    print("\nValidation complete. These are valid deliveries: output/valid.csv")
                    print("===================================================================")
                    view_csv_file('output/valid.csv')
            except Exception as e:
                print(f"An error occurred: {e}")
                print("==============================")
                break

            # Option to see rejected deliveries
            try:
                print("\nDo you wish to view the rejected deliveries?")
                view_rejected = input("Type 'yes' to view rejected deliveries, or anything else to exit: ")
                if view_rejected.lower() != 'yes':
                    print("Exiting the program.")
                    print("==============================")
                    break
                elif view_rejected.lower() == 'no':
                    pass
                elif view_rejected.lower() == 'yes':
                    print("\nThese are the rejected deliveries: output/rejected.csv")
                    print("===============================================================")
                    view_csv_file('output/rejected.csv')
            except Exception as e:
                print(f"An error occurred: {e}")
                print("==============================")
                break
                
            try:        
                print("\nOkay! Do you wish to continue to the optimizer?")
                continue_optimizer = input("Type 'yes' to continue to the optimizer, or anything else to return to main menu: ")
        
                if continue_optimizer.lower() != 'yes':
                    print("Exiting the program.")
                    print("==============================")
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("==============================")
                break
            try:
                run_optimizer()
                total_distance = run_optimizer()
                print(f"\nOptimization complete. Total distance for the route: {total_distance:.2f} km")
                print("These are the optimized routes: output/optimized_route.csv")
                print("====================================================================================")
                view_csv_file('output/optimized_route.csv')
                print("====================================================================================")
                
                print("\nRoute summary based on transport mode: ")
                with open('output/optimized_route.csv', 'r') as routefile:
                    reader = csv.reader(routefile)
                    
                
            except Exception as e:
                print(f"\nAn error occurred during optimization: {e}")
                print("==============================")
                break
         
        # Reset output files   
        elif choice == '2':
            open('output/valid.csv', 'w').write('customer,latitude,lognitude,priority,weight_kg\n')
            open('output/rejected.csv', 'w').write('customer,latitude,lognitude,priority,weight_kg\n')
            open('output/optimized_route.csv', 'w').write('from_customer,to_customer,distance_km,mode_of_transport,time,cost,emissions_kgCO2\n')
            print("\nOutput files have been reset.")
            print("==============================")
        
        # Exit program
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()