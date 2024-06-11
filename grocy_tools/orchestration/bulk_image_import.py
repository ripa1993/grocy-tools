from abc import ABCMeta

from grocy_rest_api_client.models import ProductDetailsResponse
from grocy_tools.grocy.service import GrocyService
from grocy_tools.openfoodfacts.service import OpenFoodFactsService


class BulkImageImportInterface(metaclass=ABCMeta):
    def run(self):
        raise NotImplementedError


class BulkImageImport(BulkImageImportInterface):
    def __init__(self, grocy_svc: GrocyService, off_svc: OpenFoodFactsService):
        self.grocy_svc = grocy_svc
        self.off_svc = off_svc

    def run(self):
        stock_products = self.grocy_svc.get_stock_products()
        for stock_product in stock_products:
            if stock_product.product.picture_file_name is None and isinstance(stock_product.product_id, int):
                print(f"Product '{stock_product.product.name}' has no image")
                product_details = self.grocy_svc.get_product_details(stock_product.product_id)
                if isinstance(product_details, ProductDetailsResponse) and len(product_details.product_barcodes) > 0:
                    print("Starting image search by product barcode")
                    updated = False
                    for product_barcode in product_details.product_barcodes:
                        image = self.off_svc.get_image_url_by_barcode(product_barcode.barcode)
                        if image is not None:
                            res = self.grocy_svc.put_product_image_from_url(stock_product.product_id, image)
                            if res is None:
                                updated = True
                        if updated:
                            print("Product updated")
                            break
                print("Image search by barcode unsuccessful")
