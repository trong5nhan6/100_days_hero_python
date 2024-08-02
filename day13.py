from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, manufacturer, stock_quantity):
        self._name = name
        self._price = price
        self._manufacturer = manufacturer
        self._stock_quantity = stock_quantity

    def get_name(self):
        pass

    def set_name(self, name):
        pass

    def get_price(self):
        pass

    def set_price(self, price):
        pass

    def get_manufacturer(self):
        pass

    def set_manufacturer(self, manufacturer):
        pass

    def get_stock_quantity(self):
        pass

    def set_stock_quantity(self, stock_quantity):
        pass


class Phone(Product):
    def __init__(self, name, price, manufacturer, stock_quantity, screen_size):
        super().__init__(name, price, manufacturer, stock_quantity)
        self._screen_size = screen_size

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_manufacturer(self):
        return self._manufacturer

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def get_stock_quantity(self):
        return self._stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self._stock_quantity = stock_quantity

    def get_screen_size(self):
        return self._screen_size

    def set_screen_size(self, screen_size):
        self._screen_size = screen_size


class Laptop(Product):
    def __init__(self, name, price, manufacturer, stock_quantity, ram_size):
        super().__init__(name, price, manufacturer, stock_quantity)
        self._ram_size = ram_size

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_manufacturer(self):
        return self._manufacturer

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def get_stock_quantity(self):
        return self._stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self._stock_quantity = stock_quantity

    def get_ram_size(self):
        return self._ram_size

    def set_ram_size(self, ram_size):
        self._ram_size = ram_size


class TV(Product):
    def __init__(self, name, price, manufacturer, stock_quantity, screen_resolution):
        super().__init__(name, price, manufacturer, stock_quantity)
        self._screen_resolution = screen_resolution

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_manufacturer(self):
        return self._manufacturer

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def get_stock_quantity(self):
        return self._stock_quantity

    def set_stock_quantity(self, stock_quantity):
        self._stock_quantity = stock_quantity

    def get_screen_resolution(self):
        return self._screen_resolution

    def set_screen_resolution(self, screen_resolution):
        self._screen_resolution = screen_resolution


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.products = {}

    def add_product(self, product, quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def calculate_total(self):
        total = 0
        for product, quantity in self.products.items():
            total += product.get_price() * quantity
        return total

    def print_invoice(self):
        print(f"Invoice for {self.customer_name}")
        for product, quantity in self.products.items():
            print(
                f"{product.get_name()} - {quantity} x ${product.get_price()} = ${product.get_price() * quantity}")
        print(f"Total: ${self.calculate_total()}")


phone = Phone("iPhone 14", 999, "Apple", 10, "6.1 inches")
laptop = Laptop("Dell XPS 13", 1199, "Dell", 5, "16 GB")
tv = TV("Samsung 4K", 799, "Samsung", 7, "3840x2160")

order = Order("John Doe")
order.add_product(phone, 2)
order.add_product(laptop, 1)
order.add_product(tv, 1)

order.print_invoice()
