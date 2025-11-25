● Project Overview
The Enhanced Inventory Manager is a Python-based application designed to modernize stock tracking and asset management. It addresses the inefficiencies of manual record-keeping by providing a digital platform for real-time data accuracy. This project implements essential CRUD (Create, Read, Update, Delete) operations, allowing users to efficiently manage products, monitor stock levels, and generate reports.



● ​Key Features
This project includes three major functional modules as required:
​Product Management: Add new items with details (Name, ID, Quantity, Price).
​Inventory Control: Update stock levels (restock or issue items) and delete obsolete records.
​Reporting & Search: View full inventory lists and search for specific items by ID or Name.
​Data Persistence: Automatically saves all records to file storage to ensure data is not lost between sessions.
​Input Validation: Robust error handling to prevent invalid data entries (e.g., negative stock).



● ​Technologies Used
​Language: Python 3.x
​Version Control: Git & GitHub
​Data Storage: File Handling (CSV/Text-based storage)
​Development Environment: VS Code



● ​Installation & Setup Steps
Follow these steps to set up the project on your local machine:
​Clone the Repository
git clone https://github.com/manthanawaya/enhanced_inventory_manager.git
​Navigate to the Project Directory
cd enhanced_inventory_manager
​Run the Application
python main.py
(Note: Ensure you have Python installed. If python doesn't work, try python3)



● ​Instructions for Testing
To verify the system functionality, follow these test cases:

1.​Test Adding an Item:
​Select "Add Item" from the menu.
​Enter valid details (e.g., ID: 101, Name: Laptop, Qty: 5).
​Expected Result: System confirms "Item Added Successfully."


2.​Test Updating Stock:
​Select "Update Item".
​Enter ID 101 and change quantity to 10.
​Expected Result: Inventory report shows updated quantity.


3.​Test Error Handling:
​Try entering a negative number for quantity.
​Expected Result: System displays "Invalid Input" and asks again.


