# Fergus Haak - 28/07/2023 - Creator Principle Example
# Code example from Arjan Codes

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ProductDescription:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDescription
    quantity: int


@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.now())

    # Sale is responsible for creating new objects inside of itself instead of creating the objects and then adding them in to the sale object
    def add_line_item(self, product: ProductDescription, quantity: int):
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDescription(price=5000, description="Gaming Headset")
    keyboard = ProductDescription(price=7500, description="Mechanical Gaming Keyboard")

    sale = Sale()
    sale.add_line_item(product=headset, quantity=2)
    sale.add_line_item(product=keyboard, quantity=3)

    print(sale)


if __name__ == "__main__":
    main()
