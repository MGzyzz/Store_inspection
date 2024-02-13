from datetime import datetime, timedelta
import random
import math
from product import Milk, Salt, Fish, Corn, Stew


class Store:
    def __init__(self, product):
        self.product = product


    def get_random_delivery_time(self):
        for i in self.product:
            random_number = random.randint(1, 200)
            delivery_timestamp = datetime.now() - timedelta(days=random_number)
            i.delivery_timestamp = delivery_timestamp

    def get_random_storage_place(self):
        for i in self.product:
            storage = ['Icebox', 'Showcase']
            random_storage = random.choice(storage)
            i.storage = random_storage

    def check(self):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jul", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
        self.get_random_delivery_time()
        print(
            f'{"Inspection result:":>40}\n\n{"Product"} | Delivered at | Storage place | S. life days | Fresh\n---------+--------------+---------------+--------------+-------')

        for i in range(21):
            self.get_random_delivery_time()
            self.get_random_storage_place()
            random_product = random.choice(self.product)
            print(f"{random_product.name:<7} | {months[random_product.delivery_timestamp.month - 1]} {random_product.delivery_timestamp.day}, {random_product.delivery_timestamp.year:} | {random_product.storage:<13} | {random_product.storage_life_days:<12} | {random_product.is_fresh()}")


store = Store([Milk('Milk', 60, None, None), Salt('Salt', math.inf, None, None), Fish("Fish", 20, 6, None), Corn("Corn", 150, None,None), Stew('Stew', 180, None,None)])

store.check()