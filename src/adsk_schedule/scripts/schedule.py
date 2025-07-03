import datetime
import json
import numpy as np

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

# If you want to randomly select a user and then a shift from their preferences:
def get_random_shift(user_names, user_shifts):
    """Selects a random user and a random shift from that user's preferences."""
    idx = np.random.choice(len(user_names))
    selected_user = user_names[idx]
    # Assume user_shifts[idx] is a list of shifts for that user
    if isinstance(user_shifts[idx], list):
        selected_shift = np.random.choice(user_shifts[idx])
    else:
        selected_shift = user_shifts[idx]
    return selected_user, selected_shift

# Example usage:
name, shift = get_random_shift(user_names, user_shifts)
print(f"Selected user: {name}, Assigned shift: {shift}")