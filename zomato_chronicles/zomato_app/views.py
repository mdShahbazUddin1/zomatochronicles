# zomato_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

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

def menu_view(request):
    return render(request, 'zomato_app/menu.html', {'menu': menu})

def place_order_view(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        dish_ids = [int(dish_id) for dish_id in request.POST.getlist('dish')]
        
        available_dishes = [dish_id for dish_id in dish_ids if Order.check_dish_availability(Order, dish_id)]
        if len(available_dishes) == len(dish_ids):
            order_id = len(orders) + 1
            order = Order(order_id, customer_name, available_dishes)
            orders[order_id] = order
            return render(request, 'zomato_app/order_placed.html', {'order': order})
        else:
            unavailable_dishes = set(dish_ids) - set(available_dishes)
            return render(request, 'zomato_app/order_failed.html', {'unavailable_dishes': unavailable_dishes})
    
    return render(request, 'zomato_app/place_order.html', {'menu': menu})
