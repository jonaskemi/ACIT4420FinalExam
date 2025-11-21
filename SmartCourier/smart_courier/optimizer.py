from math import cos, sin, asin, sqrt, radians
from .utils import timed
import csv 
import json

@timed
def haversine(lon1, lat1, lon2, lat2):
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Determines return value units.
    return c * r

@timed
def calculate_distance(deliveries):
    if not deliveries:
        return []
    
    with open('output/optimized_route.csv', 'w', newline='') as routefile:
        writer = csv.writer(routefile)
        writer.writerow(['from_customer', 'to_customer', 'distance_km'])
    
        start_depot = (59.94169250714698, 10.944143711757192, "postensterminal")            # Assuming depot is at "Postens Terminal"
        unvisited = []                                  # List of deliveries to visit 
        current_location = start_depot                  # Start at the depot
        distance = 0.0                                  # Total distance traveled    
    
        # Convert valid deliveries CSV to list of dicts
        with open(deliveries, 'r') as validfile:
            reader = csv.reader(validfile)
            next(reader)  # Skip header
            for row in reader:
                customer = row[0]
                latitude = float(row[1])
                longitude = float(row[2])
                priority = row[3]
                weight_kg = float(row[4])
                unvisited.append({
                    'customer': customer,
                    'latitude': latitude,
                    'longitude': longitude,
                    'priority': priority,
                    'weight_kg': weight_kg
                })

        while unvisited:
            # Finding the deliveries with the highest priority first
            high_priority = [d for d in unvisited if d['priority'].lower() == 'high']
            medium_priority= [d for d in unvisited if d['priority'].lower() == 'medium']
         
            # Deliver high priority first
            if high_priority:
                deliveries = high_priority
            elif medium_priority:
                deliveries = medium_priority
            else:
                deliveries = unvisited
        
            nearest = min(
                deliveries, # If there is high priority deliveries, only consider those then medium then low
                key=lambda delivery: haversine(  # Uses lambda to calculate distance from current location to each delivery then pick the minimum
                current_location[1], current_location[0],
                float(delivery['longitude']), float(delivery['latitude'])
                ))
        
            leg_distance = haversine(
                current_location[1], current_location[0],
                float(nearest['longitude']), float(nearest['latitude'])
            )
            distance += leg_distance
            next_location = (float(nearest['latitude']), float(nearest['longitude']), nearest['customer'])    
            writer.writerow([current_location[2], next_location[2], distance])
        
            # Set current to the next location and remove the visited delivery from unvisited
            current_location = next_location
            unvisited.remove(nearest)
        
        # Return to depot after all deliveries are done
        return_leg = haversine(
            current_location[1], current_location[0],
            start_depot[1], start_depot[0]
        )
        distance += return_leg
        writer.writerow([current_location[2], start_depot[2], distance])
    return distance

@timed
def calculate_transport_modes(optimized_route_file):
    with open('data/transport_modes.json', 'r') as f:
        json_list = json.load(f)
        transport_data = {m['mode']: m for m in json_list}
        
        car = transport_data['Car']
        bike = transport_data['Bicycle']
        walk = transport_data['Walking']
    
    route_options = []    
        
    with open(optimized_route_file, 'r') as routefile:
        reader = csv.reader(routefile)
        next(reader)  # Skip header
        
        for row in reader:
            from_customer, to_customer, distance_km = row
            distance_km = float(distance_km)
            
            # Calculations for car, bike, and walk
            car_data = {
                'mode': 'Car',
                'time_hrs': distance_km / car['speed_kmh'],
                'cost': distance_km * car['cost_per_km'],
                'emissions_kgCO2': distance_km * car['co2_per_km']
            }
            bike_data = {
                'mode': 'Bicycle',
                'time_hrs': distance_km / bike['speed_kmh'],
                'cost': distance_km * bike['cost_per_km'],
                'emissions_kgCO2': distance_km * bike['co2_per_km']
            }
            walk_data = {
                'mode': 'Walking',
                'time_hrs': distance_km / walk['speed_kmh'],
                'cost': distance_km * walk['cost_per_km'],
                'emissions_kgCO2': distance_km * walk['co2_per_km']
            }
            route_options.append({
                'from_customer': from_customer,
                'to_customer': to_customer,
                'distance_km': distance_km,
                'car': car_data,
                'bicycle': bike_data,
                'walking': walk_data
            })
        # total calculations can be added here if needed
        total_distance = sum(option['distance_km'] for option in route_options)
        total_time_car = sum(option['car']['time_hrs'] for option in route_options)
        total_cost_car = sum(option['car']['cost'] for option in route_options)
        total_emissions_car = sum(option['car']['emissions_kgCO2'] for option in route_options)
        
        total_time_bicycle = sum(option['bicycle']['time_hrs'] for option in route_options)
        total_cost_bicycle = sum(option['bicycle']['cost'] for option in route_options)
        total_emissions_bicycle = sum(option['bicycle']['emissions_kgCO2'] for option in route_options)
        
        total_time_walking = sum(option['walking']['time_hrs'] for option in route_options)
        total_cost_walking = sum(option['walking']['cost'] for option in route_options)
        total_emissions_walking = sum(option['walking']['emissions_kgCO2'] for option in route_options)
        
        print(f"\nTotal distance: {total_distance:.2f} km")
        print(f"Car - Total time: {total_time_car:.2f} hrs, Total cost: {total_cost_car:.2f} NOK, Total emissions: {total_emissions_car:.2f} kgCO2")
        print(f"Bicycle - Total time: {total_time_bicycle:.2f} hrs, Total cost: {total_cost_bicycle:.2f} NOK, Total emissions: {total_emissions_bicycle:.2f} kgCO2")
        print(f"Walking - Total time: {total_time_walking:.2f} hrs, Total cost: {total_cost_walking:.2f} NOK, Total emissions: {total_emissions_walking:.2f} kgCO2\n")
        
    return route_options

@timed
def save_route_summary(route_options, output_file='output/optimized_route_mode.csv'):
    with open(output_file, 'w', newline='') as summaryfile:
        writer = csv.writer(summaryfile)
        writer.writerow(['from_customer', 'to_customer', 'distance_km', 'mode_of_transport', 'time_hrs', 'cost', 'emissions_kgCO2'])
        
        for option in route_options:
            for mode in ['car', 'bicycle', 'walking']:
                data = option[mode]
                writer.writerow([
                    option['from_customer'],
                    option['to_customer'],
                    option['distance_km'],
                    data['mode'],
                    f"{data['time_hrs']:.2f}",
                    f"{data['cost']:.2f}",
                    f"{data['emissions_kgCO2']:.2f}"
                ])
     
@timed           
def save_final_route(route_options, transport_mode, output_file='output/final_route.csv'):
    
    with open(output_file, 'w', newline='') as finalfile:
        writer = csv.writer(finalfile)
        writer.writerow(['from_customer', 'to_customer', 'distance_km', 'mode_of_transport', 'time_hrs', 'cost', 'emissions_kgCO2'])
        
        for option in route_options:
            data = option[transport_mode.lower()]
            writer.writerow([
                option['from_customer'],
                option['to_customer'],
                option['distance_km'],
                data['mode'],
                f"{data['time_hrs']:.2f}",
                f"{data['cost']:.2f}",
                f"{data['emissions_kgCO2']:.2f}"
            ])
 
@timed           
def print_route_summary(route_options):
    for option in route_options:
        print(f"From {option['from_customer']} to {option['to_customer']} ({option['distance_km']:.2f} km):")
        for mode in ['car', 'bicycle', 'walking']:
            data = option[mode]
            print(f"\n  {data['mode']}: Time: {data['time_hrs']:.2f} hrs, Cost: ${data['cost']:.2f}, Emissions: {data['emissions_kgCO2']:.2f} kgCO2")
        print("\n-----------------------------------------------------")

