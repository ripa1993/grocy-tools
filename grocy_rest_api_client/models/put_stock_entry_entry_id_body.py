import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutStockEntryEntryIdBody")


@_attrs_define
class PutStockEntryEntryIdBody:
    """
    Example:
        {'id': '2', 'amount': '1', 'best_before_date': '2021-07-19', 'purchased_date': '2020-01-01', 'price': '22.03',
            'open': False, 'location_id': '4'}

    Attributes:
        amount (Union[Unset, float]): The amount to add - please note that when tare weight handling for the product is
            enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be
            automatically calculated based on what is in stock and the defined tare weight
        best_before_date (Union[Unset, datetime.date]): The due date of the product to add, when omitted, the current
            date is used
        price (Union[Unset, float]): The price per stock quantity unit in configured currency
        open_ (Union[Unset, bool]): If the stock entry was already opened or not
        location_id (Union[Unset, int]): If omitted, the default location of the product is used
        shopping_location_id (Union[Unset, int]): If omitted, no store will be affected
        purchased_date (Union[Unset, datetime.date]): The date when this stock entry was purchased
    """

    amount: Union[Unset, float] = UNSET
    best_before_date: Union[Unset, datetime.date] = UNSET
    price: Union[Unset, float] = UNSET
    open_: Union[Unset, bool] = UNSET
    location_id: Union[Unset, int] = UNSET
    shopping_location_id: Union[Unset, int] = UNSET
    purchased_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        best_before_date: Union[Unset, str] = UNSET
        if not isinstance(self.best_before_date, Unset):
            best_before_date = self.best_before_date.isoformat()

        price = self.price

        open_ = self.open_

        location_id = self.location_id

        shopping_location_id = self.shopping_location_id

        purchased_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchased_date, Unset):
            purchased_date = self.purchased_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if best_before_date is not UNSET:
            field_dict["best_before_date"] = best_before_date
        if price is not UNSET:
            field_dict["price"] = price
        if open_ is not UNSET:
            field_dict["open"] = open_
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if shopping_location_id is not UNSET:
            field_dict["shopping_location_id"] = shopping_location_id
        if purchased_date is not UNSET:
            field_dict["purchased_date"] = purchased_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        _best_before_date = d.pop("best_before_date", UNSET)
        best_before_date: Union[Unset, datetime.date]
        if isinstance(_best_before_date, Unset):
            best_before_date = UNSET
        else:
            best_before_date = isoparse(_best_before_date).date()

        price = d.pop("price", UNSET)

        open_ = d.pop("open", UNSET)

        location_id = d.pop("location_id", UNSET)

        shopping_location_id = d.pop("shopping_location_id", UNSET)

        _purchased_date = d.pop("purchased_date", UNSET)
        purchased_date: Union[Unset, datetime.date]
        if isinstance(_purchased_date, Unset):
            purchased_date = UNSET
        else:
            purchased_date = isoparse(_purchased_date).date()

        put_stock_entry_entry_id_body = cls(
            amount=amount,
            best_before_date=best_before_date,
            price=price,
            open_=open_,
            location_id=location_id,
            shopping_location_id=shopping_location_id,
            purchased_date=purchased_date,
        )

        put_stock_entry_entry_id_body.additional_properties = d
        return put_stock_entry_entry_id_body

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
