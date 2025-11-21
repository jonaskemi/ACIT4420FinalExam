from .validation import (validate_customer_name, validate_priority, validate_latitude, validate_longitude, validate_weight)
from .optimizer import (calculate_distance, calculate_transport_modes, save_final_route, save_route_summary, print_route_summary)
from .utils import view_csv_file, timed
import csv
import logging 
import time

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='output/run.log', filemode='a')
stats = {'start_time': None, 'end_time': None}

@timed
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
            
            
def print_stats():
    elapsed_time = stats['end_time'] - stats['start_time']
    logging.info(f"Validation completed in {elapsed_time:.2f} seconds")
    print("=" * 40)
    print(f"Start time:      {time.strftime('%H:%M:%S', time.localtime(stats['start_time']))}")
    print(f"End time:        {time.strftime('%H:%M:%S', time.localtime(stats['end_time']))}")
    print(f"Elapsed:         {elapsed_time:.2f}s")
    print("=" * 40)
    

def main():
    import time as timemodule
    while True: 
        print("\n==============================")
        print(" Smart Courier Main Menu ")
        print("==============================")
        print("1. Start Validation and Optimization Process")
        print("2. Reset Output Files (recommended before new runs)")
        print("3. Open Output Files Manually")
        print("4. Exit")
        choice = input("\nPlease enter your choice (1-4): ")
        
        # Start validation process
        if choice == '1':
            stats['start_time'] = timemodule.time()
            
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
                continue_optimizer = input("Type 'yes' to continue to the optimizer, or anything else to exit: ")
        
                if continue_optimizer.lower() != 'yes':
                    print("Exiting the program.")
                    print("==============================")
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("==============================")
                break
            try:
                calculate_distance(deliveries='output/valid.csv')
                total_distance = calculate_distance(deliveries='output/valid.csv')
                print(f"\nOptimization complete. Total distance for the route: {total_distance:.2f} km")
                print("These are the optimized routes: output/optimized_route.csv")
                print("====================================================================================")
                view_csv_file('output/optimized_route.csv')
                print("====================================================================================")
                
                print("\nRoute summary based on transport mode: ")
                route_options = calculate_transport_modes(optimized_route_file='output/optimized_route.csv')
                print("\n")
                print_route_summary(route_options=route_options)
                
                print('\n Do you wanna save the route summary based on transport modes to a CSV file?')
                save_summary = input("Type 'yes' to save route summary, or anything else to skip: ")
                if save_summary.lower() == 'yes':
                    save_route_summary(route_options=route_options, output_file='output/optimized_route_mode.csv')
                    print("\nRoute summary saved to output/optimized_route_mode.csv")
                else:
                    print("\nSkipping saving route summary.")
                print("==============================")
                
                print('\n Finally, choose a transport mode for the final route:')
                final_mode = input("Enter your choice (Car, Bicycle, Walking): ")
                if final_mode.capitalize() not in ['Car', 'Bicycle', 'Walking']:
                    print("Invalid transport mode selected. Please choose from Car, Bicycle, or Walking.")
                    print("==============================")
                else:
                    save_final_route(route_options=route_options, transport_mode=final_mode, output_file='output/final_route.csv')
                    print(f"\nFinal route saved to output/final_route.csv using {final_mode} as the mode of transport.")
                    print("==============================")
                    # Neat print of final route
                    print(f"\nFinal route using {final_mode} as the mode of transport:")
                    view_csv_file('output/final_route.csv')
                stats['end_time'] = timemodule.time()
                print_stats()
                    
                
                
            except Exception as e:
                print(f"\nAn error occurred during optimization: {e}")
                print("==============================")
                break
         
        # Reset output files   
        elif choice == '2':
            stats['start_time'] = timemodule.time()
            open('output/valid.csv', 'w').write('customer,latitude,lognitude,priority,weight_kg\n')
            open('output/rejected.csv', 'w').write('customer,latitude,lognitude,priority,weight_kg\n')
            open('output/optimized_route.csv', 'w').write('from_customer,to_customer,distance_km,mode_of_transport,time,cost,emissions_kgCO2\n')
            open('output/optimized_route_mode.csv', 'w').write('from_customer,to_customer,distance_km,mode_of_transport,time_hrs,cost,emissions_kgCO2\n')
            open('output/final_route.csv', 'w').write('from_customer,to_customer,distance_km,mode_of_transport,time_hrs,cost,emissions_kgCO2\n')
            print("\nOutput files have been reset.")
            print("==============================")
            stats['end_time'] = timemodule.time()
            print_stats()
        
        # Open output files manually
        elif choice == '3':
            stats['start_time'] = timemodule.time()
            print("\nSelect the output file to view:")
            print("1. Valid Deliveries (output/valid.csv)")
            print("2. Rejected Deliveries (output/rejected.csv)")
            print("3. Optimized Route (output/optimized_route.csv)")
            print("4. Optimized Route options (output/optimized_route_mode.csv)")
            print("5. Final Route (output/final_route.csv)")
            file_choice = input("Enter your choice (1-5): ")
            
            if file_choice == '1':
                print("\nValid Deliveries:")
                print("==============================")
                view_csv_file('output/valid.csv')
            elif file_choice == '2':
                print("\nRejected Deliveries:")
                print("==============================")
                view_csv_file('output/rejected.csv')
            elif file_choice == '3':
                print("\nOptimized Route:")
                print("==============================")
                view_csv_file('output/optimized_route.csv')
            elif file_choice == '4':
                print("\nOptimized Route Options:")
                print("==============================")
                view_csv_file('output/optimized_route_mode.csv')
            elif file_choice == '5':
                print("\nFinal Route:")
                print("==============================")
                view_csv_file('output/final_route.csv')
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")
            stats['end_time'] = timemodule.time()
            print_stats()
        
        # Exit program
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()