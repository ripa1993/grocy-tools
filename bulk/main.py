import base64
import os
from io import BytesIO

import httpx
import openfoodfacts

from grocy_rest_api_client import Client
from grocy_rest_api_client.api.stock import get_stock, get_stock_products_product_id
from grocy_rest_api_client.api.files import put_files_group_file_name
from grocy_rest_api_client.api.generic_entity_interactions import put_objects_entity_object_id
from grocy_rest_api_client.models import FileGroups, ExposedEntityNotIncludingNotEditable, Product
from grocy_rest_api_client.types import File


def main():
    client = Client(
        base_url=os.getenv("GROCY_API_URL"),
        headers={
            "GROCY-API-KEY": os.getenv("GROCY_API_KEY")
        }
    )

    off = openfoodfacts.API(user_agent="GrocyBulkImage/0.1")

    current_stock = get_stock.sync(client=client)
    for s in current_stock:
        if s.product.picture_file_name is None and isinstance(s.product_id, int):
            print(f"Product '{s.product.name}' has no image")
            product_details = get_stock_products_product_id.sync(client=client, product_id=s.product_id)
            if len(product_details.product_barcodes) > 0:
                print(f"Starting image search by barcode")
                uploaded = False
                for barcode in product_details.product_barcodes:
                    p = off.product.get(barcode.barcode, fields=["image_front_small_url"])
                    if p is not None and "image_front_small_url" in p.keys():
                        print(f"Found image on OpenFoodFacts for {barcode.barcode}")
                        image_front_small_url = p["image_front_small_url"]
                        image_res = httpx.get(image_front_small_url)
                        image_data = BytesIO(image_res.content)
                        extension = image_front_small_url.split(".")[-1]
                        filename_b64 = base64.b64encode(f"{barcode.barcode}.{extension}".encode("utf-8")).decode("utf-8")
                        status = put_files_group_file_name.sync(
                            client=client,
                            group=FileGroups.PRODUCTPICTURES,
                            file_name=filename_b64,
                            body=File(payload=image_data)
                        )
                        if status is None:
                            put_objects_entity_object_id.sync(
                                client=client,
                                entity=ExposedEntityNotIncludingNotEditable.PRODUCTS,
                                body=Product(
                                    picture_file_name=f"{barcode.barcode}.{extension}"
                                ),
                                object_id=s.product_id
                            )
                            uploaded = True
                    if uploaded:
                        break


if __name__ == '__main__':
    main()
