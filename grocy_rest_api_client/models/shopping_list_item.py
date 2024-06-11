import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shopping_list_item_userfields import ShoppingListItemUserfields


T = TypeVar("T", bound="ShoppingListItem")


@_attrs_define
class ShoppingListItem:
    """
    Attributes:
        id (Union[Unset, int]):
        shopping_list_id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        note (Union[Unset, str]):
        amount (Union[Unset, float]): The manual entered amount Default: 0.0.
        row_created_timestamp (Union[Unset, datetime.datetime]):
        userfields (Union[Unset, ShoppingListItemUserfields]): Key/value pairs of userfields
    """

    id: Union[Unset, int] = UNSET
    shopping_list_id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = 0.0
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    userfields: Union[Unset, "ShoppingListItemUserfields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        shopping_list_id = self.shopping_list_id

        product_id = self.product_id

        note = self.note

        amount = self.amount

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        userfields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.userfields, Unset):
            userfields = self.userfields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if shopping_list_id is not UNSET:
            field_dict["shopping_list_id"] = shopping_list_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if note is not UNSET:
            field_dict["note"] = note
        if amount is not UNSET:
            field_dict["amount"] = amount
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if userfields is not UNSET:
            field_dict["userfields"] = userfields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shopping_list_item_userfields import ShoppingListItemUserfields

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        shopping_list_id = d.pop("shopping_list_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        note = d.pop("note", UNSET)

        amount = d.pop("amount", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        _userfields = d.pop("userfields", UNSET)
        userfields: Union[Unset, ShoppingListItemUserfields]
        if isinstance(_userfields, Unset):
            userfields = UNSET
        else:
            userfields = ShoppingListItemUserfields.from_dict(_userfields)

        shopping_list_item = cls(
            id=id,
            shopping_list_id=shopping_list_id,
            product_id=product_id,
            note=note,
            amount=amount,
            row_created_timestamp=row_created_timestamp,
            userfields=userfields,
        )

        shopping_list_item.additional_properties = d
        return shopping_list_item

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
