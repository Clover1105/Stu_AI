from .utils.helper import calculate_total

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, price):
        self.items.append(price)

    def get_total(self):
        return calculate_total(self.items)
