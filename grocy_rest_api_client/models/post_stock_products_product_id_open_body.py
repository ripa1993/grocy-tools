from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockProductsProductIdOpenBody")


@_attrs_define
class PostStockProductsProductIdOpenBody:
    """
    Example:
        {'amount': 1}

    Attributes:
        amount (Union[Unset, float]): The amount to mark as opened
        stock_entry_id (Union[Unset, str]): A specific stock entry id to open, if used, the amount has to be 1
        allow_subproduct_substitution (Union[Unset, bool]): `true` when any in-stock sub product should be used when the
            given product is a parent product and currently not in-stock
    """

    amount: Union[Unset, float] = UNSET
    stock_entry_id: Union[Unset, str] = UNSET
    allow_subproduct_substitution: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        stock_entry_id = self.stock_entry_id

        allow_subproduct_substitution = self.allow_subproduct_substitution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if stock_entry_id is not UNSET:
            field_dict["stock_entry_id"] = stock_entry_id
        if allow_subproduct_substitution is not UNSET:
            field_dict["allow_subproduct_substitution"] = allow_subproduct_substitution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        stock_entry_id = d.pop("stock_entry_id", UNSET)

        allow_subproduct_substitution = d.pop("allow_subproduct_substitution", UNSET)

        post_stock_products_product_id_open_body = cls(
            amount=amount,
            stock_entry_id=stock_entry_id,
            allow_subproduct_substitution=allow_subproduct_substitution,
        )

        post_stock_products_product_id_open_body.additional_properties = d
        return post_stock_products_product_id_open_body

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
