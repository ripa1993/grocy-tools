from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockLocation")


@_attrs_define
class StockLocation:
    """
    Example:
        {'id': '1', 'product_id': '3', 'amount': '2', 'location_id': '1', 'name': 'Fridge'}

    Attributes:
        id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        amount (Union[Unset, float]):
        location_id (Union[Unset, int]):
        location_name (Union[Unset, str]):
        location_is_freezer (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    location_id: Union[Unset, int] = UNSET
    location_name: Union[Unset, str] = UNSET
    location_is_freezer: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        product_id = self.product_id

        amount = self.amount

        location_id = self.location_id

        location_name = self.location_name

        location_is_freezer = self.location_is_freezer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if location_is_freezer is not UNSET:
            field_dict["location_is_freezer"] = location_is_freezer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        product_id = d.pop("product_id", UNSET)

        amount = d.pop("amount", UNSET)

        location_id = d.pop("location_id", UNSET)

        location_name = d.pop("location_name", UNSET)

        location_is_freezer = d.pop("location_is_freezer", UNSET)

        stock_location = cls(
            id=id,
            product_id=product_id,
            amount=amount,
            location_id=location_id,
            location_name=location_name,
            location_is_freezer=location_is_freezer,
        )

        stock_location.additional_properties = d
        return stock_location

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
