from abc import ABCMeta, abstractmethod


class ImageSourceInterface(metaclass=ABCMeta):
    @abstractmethod
    def find_image_url(self, barcode: str | None, name: str) -> str | None: ...
