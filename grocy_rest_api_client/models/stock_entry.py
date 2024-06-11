import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockEntry")


@_attrs_define
class StockEntry:
    """
    Example:
        {'id': '77', 'product_id': '1', 'amount': '2', 'best_before_date': '2019-07-07', 'purchased_date': '2019-05-03',
            'stock_id': '5ccc6b2421979', 'price': None, 'open': '0', 'opened_date': None, 'row_created_timestamp':
            '2019-05-03 18:24:04', 'location_id': '4', 'shopping_location_id': None}

    Attributes:
        id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        location_id (Union[Unset, int]):
        shopping_location_id (Union[Unset, int]):
        amount (Union[Unset, float]):
        best_before_date (Union[Unset, datetime.date]):
        purchased_date (Union[Unset, datetime.date]):
        stock_id (Union[Unset, str]): A unique id which references this stock entry during its lifetime
        price (Union[Unset, float]):
        open_ (Union[Unset, int]):
        opened_date (Union[Unset, datetime.date]):
        note (Union[Unset, str]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    location_id: Union[Unset, int] = UNSET
    shopping_location_id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    best_before_date: Union[Unset, datetime.date] = UNSET
    purchased_date: Union[Unset, datetime.date] = UNSET
    stock_id: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    open_: Union[Unset, int] = UNSET
    opened_date: Union[Unset, datetime.date] = UNSET
    note: Union[Unset, str] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        product_id = self.product_id

        location_id = self.location_id

        shopping_location_id = self.shopping_location_id

        amount = self.amount

        best_before_date: Union[Unset, str] = UNSET
        if not isinstance(self.best_before_date, Unset):
            best_before_date = self.best_before_date.isoformat()

        purchased_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchased_date, Unset):
            purchased_date = self.purchased_date.isoformat()

        stock_id = self.stock_id

        price = self.price

        open_ = self.open_

        opened_date: Union[Unset, str] = UNSET
        if not isinstance(self.opened_date, Unset):
            opened_date = self.opened_date.isoformat()

        note = self.note

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if shopping_location_id is not UNSET:
            field_dict["shopping_location_id"] = shopping_location_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if best_before_date is not UNSET:
            field_dict["best_before_date"] = best_before_date
        if purchased_date is not UNSET:
            field_dict["purchased_date"] = purchased_date
        if stock_id is not UNSET:
            field_dict["stock_id"] = stock_id
        if price is not UNSET:
            field_dict["price"] = price
        if open_ is not UNSET:
            field_dict["open"] = open_
        if opened_date is not UNSET:
            field_dict["opened_date"] = opened_date
        if note is not UNSET:
            field_dict["note"] = note
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        product_id = d.pop("product_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        shopping_location_id = d.pop("shopping_location_id", UNSET)

        amount = d.pop("amount", UNSET)

        _best_before_date = d.pop("best_before_date", UNSET)
        best_before_date: Union[Unset, datetime.date]
        if isinstance(_best_before_date, Unset):
            best_before_date = UNSET
        else:
            best_before_date = isoparse(_best_before_date).date()

        _purchased_date = d.pop("purchased_date", UNSET)
        purchased_date: Union[Unset, datetime.date]
        if isinstance(_purchased_date, Unset):
            purchased_date = UNSET
        else:
            purchased_date = isoparse(_purchased_date).date()

        stock_id = d.pop("stock_id", UNSET)

        price = d.pop("price", UNSET)

        open_ = d.pop("open", UNSET)

        _opened_date = d.pop("opened_date", UNSET)
        opened_date: Union[Unset, datetime.date]
        if isinstance(_opened_date, Unset):
            opened_date = UNSET
        else:
            opened_date = isoparse(_opened_date).date()

        note = d.pop("note", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        stock_entry = cls(
            id=id,
            product_id=product_id,
            location_id=location_id,
            shopping_location_id=shopping_location_id,
            amount=amount,
            best_before_date=best_before_date,
            purchased_date=purchased_date,
            stock_id=stock_id,
            price=price,
            open_=open_,
            opened_date=opened_date,
            note=note,
            row_created_timestamp=row_created_timestamp,
        )

        stock_entry.additional_properties = d
        return stock_entry

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
