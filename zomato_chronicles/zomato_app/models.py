menu = {
    1: {'name': 'Pizza', 'price': 10.99, 'availability': True},
    2: {'name': 'Burger', 'price': 5.99, 'availability': True},
    3: {'name': 'Pasta', 'price': 8.99, 'availability': False},
    # Add more menu items as needed
}

orders = {}

class Order:
    def __init__(self, order_id, customer_name, dishes):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes = dishes
        self.status = 'received'

    def update_status(self, new_status):
        self.status = new_status

    def check_dish_availability(self, dish_id):
        if dish_id in menu and menu[dish_id]['availability']:
            return True
        return False
