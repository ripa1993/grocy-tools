import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stock_transaction_type import StockTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockLogEntry")


@_attrs_define
class StockLogEntry:
    """
    Attributes:
        id (Union[Unset, int]):
        product_id (Union[Unset, int]):
        amount (Union[Unset, float]):
        best_before_date (Union[Unset, datetime.date]):
        purchased_date (Union[Unset, datetime.date]):
        used_date (Union[Unset, datetime.date]):
        spoiled (Union[Unset, bool]):  Default: False.
        stock_id (Union[Unset, str]):
        transaction_id (Union[Unset, str]):
        transaction_type (Union[Unset, StockTransactionType]):
        note (Union[Unset, str]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    product_id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    best_before_date: Union[Unset, datetime.date] = UNSET
    purchased_date: Union[Unset, datetime.date] = UNSET
    used_date: Union[Unset, datetime.date] = UNSET
    spoiled: Union[Unset, bool] = False
    stock_id: Union[Unset, str] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, StockTransactionType] = UNSET
    note: Union[Unset, str] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        product_id = self.product_id

        amount = self.amount

        best_before_date: Union[Unset, str] = UNSET
        if not isinstance(self.best_before_date, Unset):
            best_before_date = self.best_before_date.isoformat()

        purchased_date: Union[Unset, str] = UNSET
        if not isinstance(self.purchased_date, Unset):
            purchased_date = self.purchased_date.isoformat()

        used_date: Union[Unset, str] = UNSET
        if not isinstance(self.used_date, Unset):
            used_date = self.used_date.isoformat()

        spoiled = self.spoiled

        stock_id = self.stock_id

        transaction_id = self.transaction_id

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

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
        if amount is not UNSET:
            field_dict["amount"] = amount
        if best_before_date is not UNSET:
            field_dict["best_before_date"] = best_before_date
        if purchased_date is not UNSET:
            field_dict["purchased_date"] = purchased_date
        if used_date is not UNSET:
            field_dict["used_date"] = used_date
        if spoiled is not UNSET:
            field_dict["spoiled"] = spoiled
        if stock_id is not UNSET:
            field_dict["stock_id"] = stock_id
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
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

        _used_date = d.pop("used_date", UNSET)
        used_date: Union[Unset, datetime.date]
        if isinstance(_used_date, Unset):
            used_date = UNSET
        else:
            used_date = isoparse(_used_date).date()

        spoiled = d.pop("spoiled", UNSET)

        stock_id = d.pop("stock_id", UNSET)

        transaction_id = d.pop("transaction_id", UNSET)

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, StockTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = StockTransactionType(_transaction_type)

        note = d.pop("note", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        stock_log_entry = cls(
            id=id,
            product_id=product_id,
            amount=amount,
            best_before_date=best_before_date,
            purchased_date=purchased_date,
            used_date=used_date,
            spoiled=spoiled,
            stock_id=stock_id,
            transaction_id=transaction_id,
            transaction_type=transaction_type,
            note=note,
            row_created_timestamp=row_created_timestamp,
        )

        stock_log_entry.additional_properties = d
        return stock_log_entry

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
