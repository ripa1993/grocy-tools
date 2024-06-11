from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockProductsProductIdTransferBody")


@_attrs_define
class PostStockProductsProductIdTransferBody:
    """
    Example:
        {'amount': 1, 'location_id_from': 1, 'location_id_to': 2}

    Attributes:
        amount (Union[Unset, float]): The amount to transfer - please note that when tare weight handling for the
            product is enabled, this needs to be the amount including the container weight (gross), the amount to be posted
            will be automatically calculated based on what is in stock and the defined tare weight
        location_id_from (Union[Unset, int]): A valid location id, the location from where the product should be
            transfered
        location_id_to (Union[Unset, int]): A valid location id, the location to where the product should be transfered
        stock_entry_id (Union[Unset, str]): A specific stock entry id to transfer, if used, the amount has to be 1
    """

    amount: Union[Unset, float] = UNSET
    location_id_from: Union[Unset, int] = UNSET
    location_id_to: Union[Unset, int] = UNSET
    stock_entry_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        location_id_from = self.location_id_from

        location_id_to = self.location_id_to

        stock_entry_id = self.stock_entry_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if location_id_from is not UNSET:
            field_dict["location_id_from"] = location_id_from
        if location_id_to is not UNSET:
            field_dict["location_id_to"] = location_id_to
        if stock_entry_id is not UNSET:
            field_dict["stock_entry_id"] = stock_entry_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        location_id_from = d.pop("location_id_from", UNSET)

        location_id_to = d.pop("location_id_to", UNSET)

        stock_entry_id = d.pop("stock_entry_id", UNSET)

        post_stock_products_product_id_transfer_body = cls(
            amount=amount,
            location_id_from=location_id_from,
            location_id_to=location_id_to,
            stock_entry_id=stock_entry_id,
        )

        post_stock_products_product_id_transfer_body.additional_properties = d
        return post_stock_products_product_id_transfer_body

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
