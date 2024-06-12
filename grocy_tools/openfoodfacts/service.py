from abc import ABCMeta

import openfoodfacts


class OpenFoodFactsServiceInterface(metaclass=ABCMeta):
    def get_image_url_by_barcode(self, barcode: str) -> str | None:
        raise NotImplementedError


class OpenFoodFactsService(OpenFoodFactsServiceInterface):
    def __init__(self, user_agent="GrocyTools/0.1"):
        self.client = openfoodfacts.API(user_agent=user_agent)

    def get_image_url_by_barcode(self, barcode: str) -> str | None:
        field = "image_front_small_url"
        res = self.client.product.get(barcode, fields=[field])
        if res is not None and field in res.keys():
            return res[field]
        else:
            return None
