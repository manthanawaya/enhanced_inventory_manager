# --- src/inventory_manager.py ---
from .product import Product
from .data_handler import load_inventory, save_inventory

# Global inventory list, loaded once at startup
inventory = load_inventory()

def generate_new_id():
    """Generates a simple, unique ID for a new product."""
    if not inventory:
        return 1001
    return max(p.product_id for p in inventory) + 1

def add_product(name, quantity, price):
    """Adds a new product to the inventory."""
    new_id = generate_new_id()
    new_product = Product(new_id, name, quantity, price)
    inventory.append(new_product)
    save_inventory(inventory)
    return new_product

def view_all_products():
    """Returns the current list of all products."""
    return inventory

def update_product(product_id, new_quantity, new_price):
    """Updates the quantity and/or price of an existing product."""
    try:
        product_id = int(product_id)
    except ValueError:
        return False

    for product in inventory:
        if product.product_id == product_id:
            if new_quantity is not None:
                product.quantity = int(new_quantity)
            if new_price is not None:
                product.price = float(new_price)
            save_inventory(inventory)
            return True
    return False

def delete_product(product_id):
    """Removes a product from the inventory."""
    try:
        product_id = int(product_id)
    except ValueError:
        return False
        
    global inventory
    initial_length = len(inventory)
    inventory = [p for p in inventory if p.product_id != product_id]
    
    if len(inventory) < initial_length:
        save_inventory(inventory)
        return True
    return False

def generate_inventory_report():
    """Calculates total stock count and total inventory value."""
    total_items = sum(p.quantity for p in inventory)
    total_value = sum(p.quantity * p.price for p in inventory)
    return total_items, total_value