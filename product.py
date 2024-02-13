from datetime import datetime
import math


class Product:
    def __init__(self, name, storage_life_days, storage, delivery_timestamp: datetime = None):
        self.name = name
        self.storage_life_days = storage_life_days
        self.storage = storage
        self.delivery_timestamp = delivery_timestamp

    def is_fresh(self):
        check_product = (datetime.now() - self.delivery_timestamp).days
        if self.storage == "Icebox" or self.storage == "Showcase":
            if self.storage_life_days == math.inf:
                return True
            elif self.storage_life_days >= check_product:
                return True
            else:
                return False


class Milk(Product):
    def is_fresh(self):
        check_product = (datetime.now() - self.delivery_timestamp).days
        if self.storage == "Icebox":
            if self.storage_life_days == math.inf:
                return True
            elif check_product <= self.storage_life_days:
                return True
            elif check_product >= self.storage_life_days:
                return False
            else:
                return False
        else:
            if self.storage_life_days == math.inf:
                return True
            elif check_product <= self.storage_life_days / 2:
                return True
            elif check_product >= self.storage_life_days / 2:
                return False
            else:
                return False


class Salt(Product):
    def __init__(self, name, storage_life_days, storage, delivery_timestamp: datetime = None):
        super().__init__(name, storage_life_days, storage, delivery_timestamp)


class Fish(Product):
    def is_fresh(self):
        check_product = (datetime.now() - self.delivery_timestamp).days
        if self.storage == "Icebox":
            if self.storage_life_days == math.inf:
                return True
            elif check_product <= self.storage_life_days:
                return True
            elif check_product >= self.storage_life_days:
                return False
            else:
                return False
        else:
            if self.storage_life_days == math.inf:
                return True
            elif check_product <= round(self.storage_life_days / 6, 2):
                return True
            elif check_product >= round(self.storage_life_days / 6, 2):
                return False
            else:
                return False


class Corn(Product):
    def __init__(self, name, storage_life_days, storage, delivery_timestamp: datetime = None):
        super().__init__(name, storage_life_days, storage, delivery_timestamp)


class Stew(Product):
    def __init__(self, name, storage_life_days, storage, delivery_timestamp: datetime = None):
        super().__init__(name, storage_life_days, storage, delivery_timestamp)





