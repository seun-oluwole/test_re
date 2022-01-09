import csv


class Item:
    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"

        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def csv_method(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


class Phone(Item):
    pass

item2 = Phone("Infinix", 120, 50)
item2.total_price()
print(item2)

item1 = Item("Phone", 50, 5)
item1.apply_discount()
print(f"Discount price is ${item1.price}")
