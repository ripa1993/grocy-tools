from abc import ABCMeta

import httpx

from grocy_rest_api_client.models import ProductDetailsResponse
from grocy_tools.grocy.service import GrocyService
from grocy_tools.image_sources import ImageSourceInterface


class BulkImageImportInterface(metaclass=ABCMeta):
    def run_stock(self):
        raise NotImplementedError
    def run_all(self):
        raise NotImplementedError

class BulkImageImport(BulkImageImportInterface):
    def __init__(self, grocy_svc: GrocyService, image_sources: list[ImageSourceInterface]):
        self.grocy_svc = grocy_svc
        self.image_sources = image_sources

    def _find_and_upload_image(self, product_id: int, barcodes: list[str], name: str) -> bool:
        if barcodes:
            for barcode in barcodes:
                for source in self.image_sources:
                    image = source.find_image_url(barcode, name)
                    if image is not None:
                        try:
                            res = self.grocy_svc.put_product_image_from_url(product_id, image)
                        except httpx.TransportError as e:
                            print(f"Failed to download image from {image}: {e}")
                            continue
                        if res is None:
                            print(f"Image found via {type(source).__name__}")
                            return True
        else:
            for source in self.image_sources:
                image = source.find_image_url(None, name)
                if image is not None:
                    try:
                        res = self.grocy_svc.put_product_image_from_url(product_id, image)
                    except httpx.TransportError as e:
                        print(f"Failed to download image from {image}: {e}")
                        continue
                    if res is None:
                        print(f"Image found via {type(source).__name__} (name search)")
                        return True
        return False

    def run_stock(self):
        stock_products = self.grocy_svc.get_stock_products()
        for stock_product in stock_products:
            if stock_product.product.picture_file_name is None and isinstance(stock_product.product_id, int):
                print(f"Product '{stock_product.product.name}' has no image")
                barcodes = []
                product_details = self.grocy_svc.get_product_details(stock_product.product_id)
                if isinstance(product_details, ProductDetailsResponse) and len(product_details.product_barcodes) > 0:
                    barcodes = [pb.barcode for pb in product_details.product_barcodes]
                updated = self._find_and_upload_image(stock_product.product_id, barcodes, stock_product.product.name)
                if not updated:
                    print("Image search unsuccessful")

    def run_all(self):
        products = self.grocy_svc.get_products()
        for product in products:
            if product.picture_file_name is None and isinstance(product.id, int):
                print(f"Product '{product.name}' has no image")
                barcodes = []
                product_details = self.grocy_svc.get_product_details(product.id)
                if isinstance(product_details, ProductDetailsResponse) and len(product_details.product_barcodes) > 0:
                    barcodes = [pb.barcode for pb in product_details.product_barcodes]
                updated = self._find_and_upload_image(product.id, barcodes, product.name)
                if not updated:
                    print("Image search unsuccessful")
