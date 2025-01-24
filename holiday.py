# holiday.py

# Importing the necessary libraries (not needed in this case, but good practice for future use)

# Define the hotel_cost() function to calculate the cost based on number of nights.
def hotel_cost(num_nights):
    # Define a fixed price per night.
    price_per_night = 100  # assuming $100 per night for simplicity
    # Calculate the total cost for the hotel stay.
    total_cost = num_nights * price_per_night
    # Return the calculated total cost.
    return total_cost

# Define the plane_cost() function to calculate flight costs based on the chosen city.
def plane_cost(city_flight):
    # Define flight costs for different cities.
    if city_flight == "New York":
        return 300
    elif city_flight == "Paris":
        return 400
    elif city_flight == "Tokyo":
        return 600
    elif city_flight == "Cape Town":
        return 500
    else:
        return 0  # return 0 if the city isn't recognized (could also raise an error here)

# Define the car_rental() function to calculate the cost based on rental days.
def car_rental(rental_days):
    # Define a fixed cost per rental day.
    cost_per_day = 40  # assuming $40 per day for simplicity
    # Calculate the total cost for car rental.
    total_cost = rental_days * cost_per_day
    # Return the calculated total cost.
    return total_cost

# Define the holiday_cost() function to calculate total holiday cost.
def holiday_cost(num_nights, city_flight, rental_days):
    # Get the hotel cost by calling hotel_cost().
    total_hotel_cost = hotel_cost(num_nights)
    # Get the plane cost by calling plane_cost().
    total_plane_cost = plane_cost(city_flight)
    # Get the car rental cost by calling car_rental().
    total_car_cost = car_rental(rental_days)
    # Calculate the total holiday cost by adding all costs.
    total_cost = total_hotel_cost + total_plane_cost + total_car_cost
    # Return the total holiday cost.
    return total_cost

# Main code to interact with the user and print details.

# Step 1: Get inputs from the user.
city_flight = input("Enter the city you are flying to (New York, Paris, Tokyo, Cape Town): ")
num_nights = int(input("Enter the number of nights you will stay: "))
rental_days = int(input("Enter the number of days you will rent a car: "))

# Step 2: Calculate the total holiday cost by calling holiday_cost().
total_cost = holiday_cost(num_nights, city_flight, rental_days)

# Step 3: Print out a breakdown of all the costs for the holiday.
print("\n--- Holiday Cost Breakdown ---")
print(f"Flight to {city_flight}: ${plane_cost(city_flight)}")
print(f"Hotel cost for {num_nights} nights: ${hotel_cost(num_nights)}")
print(f"Car rental for {rental_days} days: ${car_rental(rental_days)}")
print(f"Total holiday cost: ${total_cost}")
