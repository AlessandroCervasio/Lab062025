from dataclasses import dataclass
from datetime import date

from decimal import Decimal



@dataclass
class DailySales():
    Retailer_code:int
    Product_number:int
    Order_method_code:int
    Date:date
    Quantity:int
    Unit_sale_price:Decimal

    def __eq__(self, other):
        (self.Retailer_code, self.Product_number, self.Order_method_code)==(other.Retailer_code, other.Product_number, other.Order_method_code)

    def __hash__(self):
        return hash((self.Retailer_code, self.Product_number, self.Order_method_code))

    def __str__(self):
        return f"Data: {self.Date}; Ricavo: {self.Unit_sale_price*self.Quantity}; Retailer: {self.Retailer_code}; Product: {self.Product_number} "