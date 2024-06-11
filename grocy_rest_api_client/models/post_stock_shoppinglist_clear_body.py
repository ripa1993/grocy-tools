from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockShoppinglistClearBody")


@_attrs_define
class PostStockShoppinglistClearBody:
    """
    Example:
        {'list_id': 2, 'done_only': False}

    Attributes:
        list_id (Union[Unset, int]): The shopping list id to clear, when omitted, the default shopping list (with id 1)
            is used
        done_only (Union[Unset, bool]): When `true`, only done items will be removed (defaults to `false` when ommited)
    """

    list_id: Union[Unset, int] = UNSET
    done_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        list_id = self.list_id

        done_only = self.done_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_id is not UNSET:
            field_dict["list_id"] = list_id
        if done_only is not UNSET:
            field_dict["done_only"] = done_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        list_id = d.pop("list_id", UNSET)

        done_only = d.pop("done_only", UNSET)

        post_stock_shoppinglist_clear_body = cls(
            list_id=list_id,
            done_only=done_only,
        )

        post_stock_shoppinglist_clear_body.additional_properties = d
        return post_stock_shoppinglist_clear_body

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
