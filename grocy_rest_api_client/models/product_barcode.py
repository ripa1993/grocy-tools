from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductBarcode")


@_attrs_define
class ProductBarcode:
    """
    Attributes:
        product_id (Union[Unset, int]):
        barcode (Union[Unset, str]):
        qu_id (Union[Unset, int]):
        shopping_location_id (Union[Unset, int]):
        amount (Union[Unset, float]):
        last_price (Union[Unset, float]):
        note (Union[Unset, str]):
    """

    product_id: Union[Unset, int] = UNSET
    barcode: Union[Unset, str] = UNSET
    qu_id: Union[Unset, int] = UNSET
    shopping_location_id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    last_price: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        barcode = self.barcode

        qu_id = self.qu_id

        shopping_location_id = self.shopping_location_id

        amount = self.amount

        last_price = self.last_price

        note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if qu_id is not UNSET:
            field_dict["qu_id"] = qu_id
        if shopping_location_id is not UNSET:
            field_dict["shopping_location_id"] = shopping_location_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if last_price is not UNSET:
            field_dict["last_price"] = last_price
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("product_id", UNSET)

        barcode = d.pop("barcode", UNSET)

        qu_id = d.pop("qu_id", UNSET)

        shopping_location_id = d.pop("shopping_location_id", UNSET)

        amount = d.pop("amount", UNSET)

        last_price = d.pop("last_price", UNSET)

        note = d.pop("note", UNSET)

        product_barcode = cls(
            product_id=product_id,
            barcode=barcode,
            qu_id=qu_id,
            shopping_location_id=shopping_location_id,
            amount=amount,
            last_price=last_price,
            note=note,
        )

        product_barcode.additional_properties = d
        return product_barcode

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
