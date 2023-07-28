# Fergus Haak - 28/07/2023 - Information Expert Principle Example
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

    # Information Expert suggests that Sale class should have control of total_price method
    # since it has access to all items which is required to calculate sale price, sale also has
    # access to any changes applied to items such as discounts ect
    @property
    def total_price(self) -> int:
        return sum((line.quantity * line.product.price for line in self.items))

    def add_line_item(self, product: ProductDescription, quantity: int):
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDescription(price=5000, description="Gaming Headset")
    keyboard = ProductDescription(price=7500, description="Mechanical Gaming Keyboard")

    sale = Sale()
    sale.add_line_item(product=headset, quantity=2)
    sale.add_line_item(product=keyboard, quantity=3)

    print(sale)
    print(sale.total_price)

if __name__ == "__main__":
    main()

