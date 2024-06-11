from enum import Enum


class ExposedEntityNoEdit(str, Enum):
    API_KEYS = "api_keys"
    BATTERY_CHARGE_CYCLES = "battery_charge_cycles"
    CHORES_LOG = "chores_log"
    PRODUCTS_AVERAGE_PRICE = "products_average_price"
    PRODUCTS_LAST_PURCHASED = "products_last_purchased"
    QUANTITY_UNIT_CONVERSIONS_RESOLVED = "quantity_unit_conversions_resolved"
    RECIPES_POS_RESOLVED = "recipes_pos_resolved"
    STOCK = "stock"
    STOCK_CURRENT_LOCATIONS = "stock_current_locations"
    STOCK_LOG = "stock_log"

    def __str__(self) -> str:
        return str(self.value)
