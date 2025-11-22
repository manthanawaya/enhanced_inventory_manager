# --- src/main.py ---
from .inventory_manager import (
    add_product, 
    view_all_products, 
    update_product, 
    delete_product, 
    generate_inventory_report
)

def print_menu():
    """Displays the main menu options."""
    print("\n--- Inventory Management System ---")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Update Product Stock/Price")
    print("4. Delete Product")
    print("5. Generate Inventory Report")
    print("6. Exit")
    print("-----------------------------------")

def input_validation(prompt, data_type=str):
    """A helper for basic error handling and input validation."""
    while True:
        try:
            value = input(prompt).strip()
            # If input is empty and we allow it (for optional updates)
            if not value and data_type in [int, float]:
                return None 
            
            if not value and data_type == str:
                print("Name cannot be empty.")
                continue

            if data_type == int:
                val = int(value)
                if val < 0:
                    raise ValueError("Must be a non-negative number.")
                return val
            elif data_type == float:
                val = float(value)
                if val < 0:
                    raise ValueError("Must be a non-negative number.")
                return val
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# (The handler functions call the logic from inventory_manager.py)

def handle_add_product():
    print("\n--- Add New Product ---")
    name = input_validation("Enter Product Name: ", str)
    quantity = input_validation("Enter Quantity in Stock: ", int)
    price = input_validation("Enter Unit Price: ", float)

    if name and quantity is not None and price is not None:
        new_product = add_product(name, quantity, price)
        print(f"\n✅ Product added successfully! ID: {new_product.product_id}")
    else:
        print("❌ Product not added due to missing input.")

def handle_view_products():
    products = view_all_products()
    if not products:
        print("\nInventory is currently empty.")
        return

    print(f"\n--- Current Inventory (Total Products: {len(products)}) ---")
    for p in products:
        print(p)
    print("----------------------------------------------------------")

def handle_update_product():
    product_id = input_validation("Enter Product ID to Update: ", int)
    if product_id is None:
        return

    print("--- Enter new values (leave blank to keep current value) ---")
    new_quantity = input_validation("Enter New Quantity: ", int)
    new_price = input_validation("Enter New Price: ", float)

    if new_quantity is None and new_price is None:
        print("No updates provided.")
        return

    if update_product(product_id, new_quantity, new_price):
        print(f"\n✅ Product ID {product_id} updated successfully!")
    else:
        print(f"\n❌ Error: Product ID {product_id} not found.")

def handle_delete_product():
    product_id = input_validation("Enter Product ID to Delete: ", int)
    
    if product_id is not None:
        if delete_product(product_id):
            print(f"\n✅ Product ID {product_id} deleted successfully.")
        else:
            print(f"\n❌ Error: Product ID {product_id} not found.")

def handle_report():
    total_items, total_value = generate_inventory_report()
    
    print("\n--- Inventory Summary Report ---")
    print(f"Total Unique Products: {len(view_all_products())}")
    print(f"Total Items in Stock: {total_items}")
    print(f"Total Inventory Value: ${total_value:.2f}")
    print("------------------------------")

def main():
    """The main application entry point."""
    print("Welcome to the Console Inventory Manager.")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            handle_add_product()
        elif choice == '2':
            handle_view_products()
        elif choice == '3':
            handle_update_product()
        elif choice == '4':
            handle_delete_product()
        elif choice == '5':
            handle_report()
        elif choice == '6':
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()