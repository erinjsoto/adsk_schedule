import datetime
import json
import numpy as np
from utils import get_random_shift

# Path to the user.json file
user_json_path = 'adsk_schedule/users/user.json'

# Load the JSON data
with open(user_json_path, 'r') as file:
    user_data = json.load(file)

# Example: Read users and their preferred shifts separately
user_names = [user['name'] for user in user_data]
user_shifts = [user['shift'] for user in user_data]

print("User names:", user_names)
print("User shift preferences:", user_shifts)

# Example usage:
name, shift = get_random_shift(user_names, user_shifts)
print(f"Selected user: {name}, Assigned shift: {shift}")