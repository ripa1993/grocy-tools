import click

from grocy_tools.grocy.service import GrocyService
from grocy_tools.openfoodfacts.service import OpenFoodFactsService
from grocy_tools.orchestration.bulk_image_import import BulkImageImport


@click.group()
def main():
    pass


@click.command()
@click.option('--grocy-api-url', required=True, help='Grocy API url')
@click.option('--grocy-api-key', required=True, help='Grocy API key')
def bulk_image(grocy_api_url: str, grocy_api_key: str):
    grocy_svc = GrocyService(grocy_api_url, grocy_api_key)
    off_svc = OpenFoodFactsService()
    BulkImageImport(grocy_svc, off_svc).run()

main.add_command(bulk_image)
