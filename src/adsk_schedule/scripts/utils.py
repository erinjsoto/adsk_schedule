"""
utils.py: Helper functions for schedule generation and validation.
"""

import numpy as np

def get_random_shift(user_names, user_shifts):
    """Selects a random user and a random shift from that user's preferences."""
    idx = np.random.choice(len(user_names))
    selected_user = user_names[idx]
    if isinstance(user_shifts[idx], list):
        selected_shift = np.random.choice(user_shifts[idx])
    else:
        selected_shift = user_shifts[idx]
    return selected_user, selected_shift

def select_random_user_and_shift(user_data):
    """
    Selects a random user and a random shift from their preferences.
    Args:
        user_data (list): List of user dicts with 'name' and 'shift' keys.
    Returns:
        tuple: (user_name, selected_shift)
    """
    user = np.random.choice(user_data)
    shifts = user['shift'] if isinstance(user['shift'], list) else [user['shift']]
    selected_shift = np.random.choice(shifts)
    return user['name'], selected_shift


def validate_schedule(schedule, user_data):
    """
    Example validation function: Checks if all assigned shifts are in user preferences.
    Args:
        schedule (dict): Mapping of user names to assigned shifts.
        user_data (list): List of user dicts.
    Returns:
        bool: True if valid, False otherwise.
    """
    user_pref = {user['name']: user['shift'] for user in user_data}
    for name, shift in schedule.items():
        if shift not in user_pref.get(name, []):
            return False
    return True
