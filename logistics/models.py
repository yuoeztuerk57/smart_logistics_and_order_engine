class InvalidItemError(Exception):
    pass

class Item:
    def __init__(self, name: str, price: float):
        if price <= 0:
            raise InvalidItemError("Der Preis muss größer als 0 € sein.")
        self.name = name
        self.price = price

class PhysicalItem(Item):
    def __init__(self, name: str, price: float, weight_kg: float):
        super().__init__(name, price)
        self.weight_kg = weight_kg

class DigitalItem(Item):
    def __init__(self, name: str, price: float, download_link: str):
        super().__init__(name, price)
        self.download_link = download_link
        self.weight_kg = 0.0

class Order:
    def __init__(self):
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def calculate_total(self, discount_fn=None) -> float:
        total = sum(item.price for item in self.items)
        if discount_fn:
            total = discount_fn(total)
        return round(total, 2)