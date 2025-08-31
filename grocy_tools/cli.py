import click

from grocy_tools.grocy.service import GrocyService
from grocy_tools.openfoodfacts.service import OpenFoodFactsService
from grocy_tools.orchestration.bulk_image_import import BulkImageImport
from grocy_tools.orchestration.bulk_renamer import BulkRenamer

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

main.add_command(bulk_image)
main.add_command(sanitize)
