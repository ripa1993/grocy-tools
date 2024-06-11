import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockProductsByBarcodeBarcodeInventoryBody")


@_attrs_define
class PostStockProductsByBarcodeBarcodeInventoryBody:
    """
    Attributes:
        new_amount (Union[Unset, float]): The new current amount for the given product - please note that when tare
            weight handling for the product is enabled, this needs to be the amount including the container weight (gross),
            the amount to be posted will be automatically calculated based on what is in stock and the defined tare weight
        best_before_date (Union[Unset, datetime.date]): The due date which applies to added products
        location_id (Union[Unset, int]): If omitted, the default location of the product is used (only applies to added
            products)
        price (Union[Unset, float]): If omitted, the last price of the product is used (only applies to added products)
    """

    new_amount: Union[Unset, float] = UNSET
    best_before_date: Union[Unset, datetime.date] = UNSET
    location_id: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_amount = self.new_amount

        best_before_date: Union[Unset, str] = UNSET
        if not isinstance(self.best_before_date, Unset):
            best_before_date = self.best_before_date.isoformat()

        location_id = self.location_id

        price = self.price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_amount is not UNSET:
            field_dict["new_amount"] = new_amount
        if best_before_date is not UNSET:
            field_dict["best_before_date"] = best_before_date
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        new_amount = d.pop("new_amount", UNSET)

        _best_before_date = d.pop("best_before_date", UNSET)
        best_before_date: Union[Unset, datetime.date]
        if isinstance(_best_before_date, Unset):
            best_before_date = UNSET
        else:
            best_before_date = isoparse(_best_before_date).date()

        location_id = d.pop("location_id", UNSET)

        price = d.pop("price", UNSET)

        post_stock_products_by_barcode_barcode_inventory_body = cls(
            new_amount=new_amount,
            best_before_date=best_before_date,
            location_id=location_id,
            price=price,
        )

        post_stock_products_by_barcode_barcode_inventory_body.additional_properties = d
        return post_stock_products_by_barcode_barcode_inventory_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
