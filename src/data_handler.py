# --- src/data_handler.py ---
import json
import os
from .product import Product # Note the dot: .product means look inside this package

FILE_NAME = 'inventory_data.json'

def load_inventory():
    """Loads product data from the JSON file and returns a list of Product objects."""
    # (The rest of the function remains the same as in your original file)
    if not os.path.exists(FILE_NAME):
        print(f"[{FILE_NAME}] not found. Starting with an empty inventory.")
        return []
        
    try:
        with open(FILE_NAME, 'r') as f:
            data = json.load(f)
            # Recreate Product objects from the dictionary data
            return [Product(**item) for item in data]
    except json.JSONDecodeError:
        print(f"Error reading [{FILE_NAME}]. File might be empty or corrupted. Starting with an empty inventory.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during loading: {e}. Starting with an empty inventory.")
        return []

def save_inventory(inventory_list):
    """Saves the current list of Product objects back to the JSON file."""
    data_to_save = [p.to_dict() for p in inventory_list]
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(data_to_save, f, indent=4)
    except IOError as e:
        print(f"Error saving data to file: {e}")