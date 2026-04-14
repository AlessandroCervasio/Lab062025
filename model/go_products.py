from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product():
    Product_number:int
    Product_line:str
    Product_type:str
    Product:str
    Product_brand:str
    Product_color:str
    Unit_cost:Decimal
    Unit_price:Decimal

    def __eq__(self, other):
        self.Product_number==other.Product_number

    def __hash__(self):
        return hash(self.Product_number)

    def __str__(self):
        return f"Prodotto: {self.Product} ({self.Product_number})"
