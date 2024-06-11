from enum import Enum


class ExposedEntityNotIncludingNotEditable(str, Enum):
    BATTERIES = "batteries"
    CHORES = "chores"
    EQUIPMENT = "equipment"
    LOCATIONS = "locations"
    MEAL_PLAN = "meal_plan"
    MEAL_PLAN_SECTIONS = "meal_plan_sections"
    PRODUCTS = "products"
    PRODUCT_BARCODES = "product_barcodes"
    PRODUCT_GROUPS = "product_groups"
    QUANTITY_UNITS = "quantity_units"
    QUANTITY_UNIT_CONVERSIONS = "quantity_unit_conversions"
    RECIPES = "recipes"
    RECIPES_NESTINGS = "recipes_nestings"
    RECIPES_POS = "recipes_pos"
    SHOPPING_LIST = "shopping_list"
    SHOPPING_LISTS = "shopping_lists"
    SHOPPING_LOCATIONS = "shopping_locations"
    TASKS = "tasks"
    TASK_CATEGORIES = "task_categories"
    USERENTITIES = "userentities"
    USERFIELDS = "userfields"
    USEROBJECTS = "userobjects"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
