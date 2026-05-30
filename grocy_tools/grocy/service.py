import base64
from abc import ABCMeta
from io import BytesIO
from typing import Iterator

import httpx

from grocy_rest_api_client import Client
from grocy_rest_api_client.api.files import put_files_group_file_name
from grocy_rest_api_client.api.generic_entity_interactions import get_objects_entity
from grocy_rest_api_client.api.generic_entity_interactions import put_objects_entity_object_id
from grocy_rest_api_client.api.stock import get_stock, get_stock_products_product_id
from grocy_rest_api_client.models import FileGroups, ExposedEntityNotIncludingNotEditable, Product, Error400, \
    ProductDetailsResponse, CurrentStockResponse, ExposedEntityNotIncludingNotListable
from grocy_rest_api_client.types import File


class GrocyServiceInterface(metaclass=ABCMeta):
    def get_stock_products(self):
        raise NotImplementedError

    def get_product_details(self, product_id: int):
        raise NotImplementedError

    def put_product_image_from_url(self, product_id: int, url: str) -> Error400 | None:
        raise NotImplementedError

class GrocyService(GrocyServiceInterface):
    def __init__(self, api_url, api_key):
        self.client = Client(
           base_url=api_url,
           headers={
               "GROCY-API-KEY": api_key,
           }
        )

    def get_stock_products(self) -> list[CurrentStockResponse] | None:
        return get_stock.sync(client=self.client)

    def get_product_details(self, product_id: int) -> Error400 | ProductDetailsResponse | None:
        return get_stock_products_product_id.sync(client=self.client, product_id=product_id)

    def put_product_image_from_url(self, product_id: int, url: str) -> Error400 | None:
        image_response = httpx.get(url, timeout=10)
        image_data = BytesIO(image_response.content)
        extension = url.split(".")[-1]
        file_name = f"{product_id}.{extension}"
        file_name_b64 = base64.b64encode(file_name.encode("utf-8")).decode("utf-8")
        status = put_files_group_file_name.sync(
            client=self.client,
            group=FileGroups.PRODUCTPICTURES,
            file_name=file_name_b64,
            body=File(payload=image_data)
        )
        if status is None:
            return put_objects_entity_object_id.sync(
                client=self.client,
                entity=ExposedEntityNotIncludingNotEditable.PRODUCTS,
                body=Product(
                    picture_file_name=file_name
                ),
                object_id=product_id
            )
        return status

    def get_products(self) -> Iterator[Product]:
        offset = 0
        complete = False
        while not complete:
            res = get_objects_entity.sync(ExposedEntityNotIncludingNotListable.PRODUCTS, client=self.client, limit=100, offset=offset)
            if isinstance(res, list) and len(res) > 0:
                for item in res:
                    if isinstance(item, Product):
                        yield item
                offset += 100
            else:
                complete = True

    def update_product(self, product: Product) -> Error400 | None:
        return put_objects_entity_object_id.sync(
            client=self.client,
            entity=ExposedEntityNotIncludingNotEditable.PRODUCTS,
            body=product,
            object_id=product.id
        )
