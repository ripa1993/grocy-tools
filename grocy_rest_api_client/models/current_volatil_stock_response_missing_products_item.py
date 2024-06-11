from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentVolatilStockResponseMissingProductsItem")


@_attrs_define
class CurrentVolatilStockResponseMissingProductsItem:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        amount_missing (Union[Unset, float]):
        is_partly_in_stock (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    amount_missing: Union[Unset, float] = UNSET
    is_partly_in_stock: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        amount_missing = self.amount_missing

        is_partly_in_stock = self.is_partly_in_stock

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if amount_missing is not UNSET:
            field_dict["amount_missing"] = amount_missing
        if is_partly_in_stock is not UNSET:
            field_dict["is_partly_in_stock"] = is_partly_in_stock

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        amount_missing = d.pop("amount_missing", UNSET)

        is_partly_in_stock = d.pop("is_partly_in_stock", UNSET)

        current_volatil_stock_response_missing_products_item = cls(
            id=id,
            name=name,
            amount_missing=amount_missing,
            is_partly_in_stock=is_partly_in_stock,
        )

        current_volatil_stock_response_missing_products_item.additional_properties = d
        return current_volatil_stock_response_missing_products_item

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
