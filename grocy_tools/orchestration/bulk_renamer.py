from abc import ABCMeta


class BulkRenamerInterface(metaclass=ABCMeta):
    def run_sanitize(self):
        raise NotImplementedError

class BulkRenamer(BulkRenamerInterface):
    def __init__(self, grocy_svc):
        self.grocy_svc = grocy_svc

    def run_sanitize(self):
        products = self.grocy_svc.get_products()
        for product in products:
            new_product_name = product.name.strip()
            new_product_name = new_product_name.title()
            if product.name != new_product_name:
                print(f"Product '{product.name}' will be renamed to '{new_product_name}'")
                product.name = new_product_name
                res = self.grocy_svc.update_product(product)
                if res:
                    print(f"Product '{product.name}' not updated due to {res}")
