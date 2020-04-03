class Checkout:
    class Discount:
        def __init__(self, nr_of_items, price):
            self.nr_of_items = nr_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
        self.total = 0

    def add_item_price(self, item_name: str, price: float):
        self.prices[item_name] = price

    def add_item(self, item_name):
        if item_name not in self.prices:
            raise Exception("No price specified")
        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1

    def calculate_total(self):
        total = 0
        for item, amount in self.items.items():
            total += self._calculate_item_total(item, amount)
        return total

    def add_discount(self, item, nr_of_items, price):
        discount = self.Discount(nr_of_items, price)
        self.discounts[item] = discount

    def _calculate_item_total(self, item, amount):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if amount >= discount.nr_of_items:
                total += self._calculate_item_discounted_total(item, amount, discount)
            else:
                total += self.prices[item] * amount
        else:
            total += self.prices[item] * amount
        return total

    def _calculate_item_discounted_total(self, item, amount, discount):
        total = 0
        nr_of_discounts = amount // discount.nr_of_items
        total += nr_of_discounts * discount.price
        remaining = amount % discount.nr_of_items
        total += remaining * self.prices[item]
        return total
