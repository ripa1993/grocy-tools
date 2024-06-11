from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockShoppinglistRemoveProductBody")


@_attrs_define
class PostStockShoppinglistRemoveProductBody:
    """
    Example:
        {'product_id': 3, 'list_id': 2, 'product_amount': 5}

    Attributes:
        product_id (Union[Unset, int]): A valid product id of the item on the shopping list
        list_id (Union[Unset, int]): A valid shopping list id, when omitted, the default shopping list (with id 1) is
            used
        product_amount (Union[Unset, float]): The amount of product units to remove, when omitted, the default amount of
            1 is used
    """

    product_id: Union[Unset, int] = UNSET
    list_id: Union[Unset, int] = UNSET
    product_amount: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        list_id = self.list_id

        product_amount = self.product_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if list_id is not UNSET:
            field_dict["list_id"] = list_id
        if product_amount is not UNSET:
            field_dict["product_amount"] = product_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("product_id", UNSET)

        list_id = d.pop("list_id", UNSET)

        product_amount = d.pop("product_amount", UNSET)

        post_stock_shoppinglist_remove_product_body = cls(
            product_id=product_id,
            list_id=list_id,
            product_amount=product_amount,
        )

        post_stock_shoppinglist_remove_product_body.additional_properties = d
        return post_stock_shoppinglist_remove_product_body

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
