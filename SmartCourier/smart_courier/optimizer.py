from math import cos, sin, asin, sqrt
import csv

def haversine(lon1, lat1, lon2, lat2):
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Determines return value units.
    return c * r

def optimizer(deliveries):
    if not deliveries:
        return []
    
    with open('output/optimized_route.csv', 'w', newline='') as routefile:
        writer = csv.writer(routefile)
        writer.writerow(['from_customer', 'to_customer', 'distance_km'])
    
        start_depot = (59.94, 10.94, "Postens Terminal")            # Assuming depot is at "Postens Terminal"
        unvisited = []                          # List of deliveries to visit 
        current_location = start_depot          # Start at the depot
        distance = 0.0                          # Total distance traveled    
    
        # Convert valid deliveries CSV to list of dicts
        with open(deliveries, 'r') as validfile:
            reader = csv.reader(validfile)
            next(reader)  # Skip header
            for row in reader:
                customer, latitude, longitude, priority, weight_kg = row
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