import click

from grocy_tools.grocy.service import GrocyService
from grocy_tools.openfoodfacts.service import OpenFoodFactsService
from grocy_tools.orchestration.bulk_image_import import BulkImageImport
from grocy_tools.orchestration.bulk_renamer import BulkRenamer
from grocy_tools.orchestration.products_csv import ProductsCsv

def common_options(func):
    func = click.option('--grocy-api-url', required=True, help='Grocy API url')(func)
    func = click.option('--grocy-api-key', required=True, help='Grocy API key')(func)
    return func

@click.group()
def main():
    pass

@click.command()
@common_options
def bulk_image(grocy_api_url: str, grocy_api_key: str):
    grocy_svc = GrocyService(grocy_api_url, grocy_api_key)
    off_svc = OpenFoodFactsService()
    BulkImageImport(grocy_svc, off_svc).run_all()

@click.command()
@common_options
@click.option('--dry-run', is_flag=True, default=False)
def sanitize(grocy_api_url: str, grocy_api_key: str, dry_run: bool):
    grocy_svc = GrocyService(grocy_api_url, grocy_api_key)
    BulkRenamer(grocy_svc).run_sanitize(dry_run=dry_run)

@click.command()
@common_options
@click.option("-f", "--file", "file_path",
              type=click.Path(dir_okay=False, writable=True),
              required=True, help="Output CSV path")
def export_products(grocy_api_url: str, grocy_api_key: str, file_path: str):
    grocy_svc = GrocyService(grocy_api_url, grocy_api_key)
    ProductsCsv(grocy_svc).run_export(file_path)

@click.command()
@common_options
@click.option("-f", "--file", "file_path",
              type=click.Path(exists=True, dir_okay=False),
              required=True, help="Input CSV path")
@click.option("--dry-run", is_flag=True, default=False)
def import_products(grocy_api_url: str, grocy_api_key: str, file_path: str, dry_run: bool):
    grocy_svc = GrocyService(grocy_api_url, grocy_api_key)
    ProductsCsv(grocy_svc).run_import(file_path, dry_run=dry_run)

main.add_command(bulk_image)
main.add_command(sanitize)
main.add_command(export_products)
main.add_command(import_products)
