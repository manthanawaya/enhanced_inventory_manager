ENHANCED CONSOLE-BASED JSON INVENTORY MANAGER

PROJECT OVERVIEW
This is a straightforward, console-based Inventory Management System built in Python. Its primary function is to track product stock levels and the total monetary value of the inventory.
Instead of relying on a complex database, this project uses a standard JSON file (inventory_data.json) for persistent data storage. This setup perfectly demonstrates core Python concepts like Object-Oriented Programming (using a Product class), file I/O, and basic data aggregation.

------------------------------------------------------

KEY FEATURES
* Add Product: Quickly create new items, assigning a unique ID, name, quantity, and unit price.
* View All Products: Get a formatted, easy-to-read table view of the entire current stock.
* Update Product: Modify the stock quantity or the unit price of any existing product using its unique ID.
* Delete Product: Permanently remove an item from the inventory list.
* Generate Report: Calculate and display key metrics, including the total item count and the overall monetary value of the entire inventory.

------------------------------------------------------

TECH STACK
* Language: Python 3.x
* Data Storage: JSON (inventory_data.json)
* Source Control: Git / GitHub

------------------------------------------------------

GETTING STARTED

1. INSTALLATION & SETUP
    git clone <YOUR_GITHUB_REPO_LINK>
    cd Enhanced-Inventory-Manager/src

2. RUNNING THE APPLICATION
* Execute the main script from your terminal:
    python main.py
* The interactive console menu will immediately load, prompting you to choose an action (1-6).

------------------------------------------------------

TESTING INSTRUCTIONS
You can quickly test the core functionality right from the console:
1.  Select option 1 (Add New Product) and enter sample data (e.g., Name: Mechanical Keyboard, Qty: 15, Price: 150.00).
2.  Select option 2 (View All Products) to confirm the new item has been logged.
3.  Select option 3 (Update Product). Use the new product's ID (e.g., 1001) to update the stock quantity (e.g., change 15 to 20) or the price.
4.  Finally, select option 5 (Generate Inventory Report) and verify that the calculated totals reflect your recent addition and update.

