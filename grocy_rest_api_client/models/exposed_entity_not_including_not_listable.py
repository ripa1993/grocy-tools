from enum import Enum


class ExposedEntityNotIncludingNotListable(str, Enum):
    BATTERIES = "batteries"
    BATTERY_CHARGE_CYCLES = "battery_charge_cycles"
    CHORES = "chores"
    CHORES_LOG = "chores_log"
    EQUIPMENT = "equipment"
    LOCATIONS = "locations"
    MEAL_PLAN = "meal_plan"
    MEAL_PLAN_SECTIONS = "meal_plan_sections"
    PRODUCTS = "products"
    PRODUCTS_AVERAGE_PRICE = "products_average_price"
    PRODUCTS_LAST_PURCHASED = "products_last_purchased"
    PRODUCT_BARCODES = "product_barcodes"
    PRODUCT_GROUPS = "product_groups"
    QUANTITY_UNITS = "quantity_units"
    QUANTITY_UNIT_CONVERSIONS = "quantity_unit_conversions"
    QUANTITY_UNIT_CONVERSIONS_RESOLVED = "quantity_unit_conversions_resolved"
    RECIPES = "recipes"
    RECIPES_NESTINGS = "recipes_nestings"
    RECIPES_POS = "recipes_pos"
    RECIPES_POS_RESOLVED = "recipes_pos_resolved"
    SHOPPING_LIST = "shopping_list"
    SHOPPING_LISTS = "shopping_lists"
    SHOPPING_LOCATIONS = "shopping_locations"
    STOCK = "stock"
    STOCK_CURRENT_LOCATIONS = "stock_current_locations"
    STOCK_LOG = "stock_log"
    TASKS = "tasks"
    TASK_CATEGORIES = "task_categories"
    USERENTITIES = "userentities"
    USERFIELDS = "userfields"
    USEROBJECTS = "userobjects"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
