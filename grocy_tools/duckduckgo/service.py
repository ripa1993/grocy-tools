from ddgs import DDGS
from ddgs.exceptions import DDGSException

from grocy_tools.image_sources import ImageSourceInterface


class DuckDuckGoImageService(ImageSourceInterface):
    def find_image_url(self, barcode: str | None, name: str) -> str | None:
        if not name:
            return None
        try:
            results = DDGS().images(name, safesearch="moderate", max_results=1)
        except DDGSException as e:
            print(f"DuckDuckGo image search failed for '{name}': {e}")
            return None
        return results[0]["image"] if results else None
