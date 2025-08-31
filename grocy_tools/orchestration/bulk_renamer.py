from abc import ABCMeta
import re

from grocy_tools.orchestration.constants import brands, known_replacements


class BulkRenamerInterface(metaclass=ABCMeta):
    def run_sanitize(self):
        raise NotImplementedError

class BulkRenamer(BulkRenamerInterface):
    def __init__(self, grocy_svc):
        self.grocy_svc = grocy_svc

    def run_sanitize(self, dry_run=False):
        products = self.grocy_svc.get_products()
        for product in products:
            new_product_name = product.name.strip()
            new_product_name = new_product_name.title()
            new_product_name = self.restructure_name_with_brand(new_product_name, brands)
            new_product_name = self.known_replacements(new_product_name, known_replacements)
            if product.name != new_product_name:
                print(f"Product '{product.name}' will be renamed to '{new_product_name}'")
                if not dry_run:
                    product.name = new_product_name
                    res = self.grocy_svc.update_product(product)
                    if res:
                        print(f"Product '{product.name}' not updated due to {res}")

    @staticmethod
    def restructure_name_with_brand(product_name, brand_list):
        for brand in brand_list:
            pattern = re.compile(rf"[\(\[]?{re.escape(brand)}[\)\]]?", re.IGNORECASE)
            if pattern.search(product_name):
                new_name = pattern.sub("", product_name).strip()
                return f"{new_name} [{brand}]"
        return product_name

    @staticmethod
    def known_replacements(product_name, mappings):
        for old, new in mappings.items():
            product_name = product_name.replace(old, new)
        return product_name
