# --- src/product.py ---
class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)

    def __str__(self):
        """Returns a user-friendly string representation of the product."""
        return f"ID: {self.product_id} | Name: {self.name:<20} | Stock: {self.quantity:<5} | Price: ${self.price:.2f}"

    def to_dict(self):
        """Used by data_handler to save the object to a JSON file."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price
        }