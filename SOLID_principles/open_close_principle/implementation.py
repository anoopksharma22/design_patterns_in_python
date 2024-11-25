from dataclasses import dataclass, field
from typing import List

@dataclass
class Order:
    items: List = field()

    def add_item(self, name):
        self.items.append(name)


if __name__ == "__main__":
    items = ['Apple', 'Orange', 'Banana']
    o1 = Order(items)
    # o1.add_item("Apple")
    # o1.add_item("Banana")
    # o1.add_item("Orange")

    # o2 = Order()
    # o2.add_item("Watch")
    # o2.add_item("Mouse")
    # o2.add_item("Headphone")

    # print(f'Items in order o2 {o2.items}')
    print(f'Items in order o1 {o1.items}')