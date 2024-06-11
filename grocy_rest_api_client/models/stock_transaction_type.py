from enum import Enum


class StockTransactionType(str, Enum):
    CONSUME = "consume"
    INVENTORY_CORRECTION = "inventory-correction"
    PRODUCT_OPENED = "product-opened"
    PURCHASE = "purchase"

    def __str__(self) -> str:
        return str(self.value)
