import time

import openfoodfacts
import requests

from grocy_tools.image_sources import ImageSourceInterface


class OpenFoodFactsService(ImageSourceInterface):
    def __init__(self, user_agent="GrocyTools/0.1"):
        self.client = openfoodfacts.API(user_agent=user_agent)

    def find_image_url(self, barcode: str | None, name: str) -> str | None:
        if not barcode:
            return None
        field = "image_front_small_url"
        delay = 2
        for _ in range(5):
            time.sleep(delay)
            try:
                res = self.client.product.get(barcode, fields=[field])
            except requests.exceptions.HTTPError as e:
                if e.response is not None and e.response.status_code == 429:
                    print(f"Rate limited by OpenFoodFacts, retrying in {delay}s...")
                    delay *= 2
                    continue
                raise
            if res is not None and field in res.keys():
                return res[field]
            return None
        print(f"Giving up on barcode {barcode} after repeated rate limiting")
        return None
