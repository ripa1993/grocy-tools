from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockShoppinglistAddProductBody")


@_attrs_define
class PostStockShoppinglistAddProductBody:
    """
    Example:
        {'product_id': 3, 'list_id': 2, 'product_amount': 5, 'note': 'This is the note of the shopping list item...'}

    Attributes:
        product_id (Union[Unset, int]): A valid product id of the product to be added
        qu_id (Union[Unset, int]): A valid quantity unit id (used only for display; the amount needs to be related to
            the products stock QU), when omitted, the products stock QU is used
        list_id (Union[Unset, int]): A valid shopping list id, when omitted, the default shopping list (with id 1) is
            used
        product_amount (Union[Unset, float]): The amount (related to the products stock QU) to add, when omitted, the
            default amount of 1 is used
        note (Union[Unset, str]): The note of the shopping list item
    """

    product_id: Union[Unset, int] = UNSET
    qu_id: Union[Unset, int] = UNSET
    list_id: Union[Unset, int] = UNSET
    product_amount: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        qu_id = self.qu_id

        list_id = self.list_id

        product_amount = self.product_amount

        note = self.note

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if qu_id is not UNSET:
            field_dict["qu_id"] = qu_id
        if list_id is not UNSET:
            field_dict["list_id"] = list_id
        if product_amount is not UNSET:
            field_dict["product_amount"] = product_amount
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_id = d.pop("product_id", UNSET)

        qu_id = d.pop("qu_id", UNSET)

        list_id = d.pop("list_id", UNSET)

        product_amount = d.pop("product_amount", UNSET)

        note = d.pop("note", UNSET)

        post_stock_shoppinglist_add_product_body = cls(
            product_id=product_id,
            qu_id=qu_id,
            list_id=list_id,
            product_amount=product_amount,
            note=note,
        )

        post_stock_shoppinglist_add_product_body.additional_properties = d
        return post_stock_shoppinglist_add_product_body

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
