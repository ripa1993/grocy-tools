from abc import ABCMeta
from io import BytesIO
from typing import Tuple

import httpx
import openfoodfacts


class OpenFoodFactsServiceInterface(metaclass=ABCMeta):
    def get_image_url_by_barcode(self, barcode: str) -> str | None:
        raise NotImplementedError

    def get_image_bytes_by_barcode(self, barcode: str) -> tuple[BytesIO, str] | None:
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

    def get_image_bytes_by_barcode(self, barcode: str) -> tuple[BytesIO, str] | None:
        url = self.get_image_url_by_barcode(barcode)
        if url is None:
            return None
        image_res = httpx.get(url)
        file_name = url.split("/")[-1]
        return BytesIO(image_res.content), file_name
