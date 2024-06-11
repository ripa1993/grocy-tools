import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stock_transaction_type import StockTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockJournal")


@_attrs_define
class StockJournal:
    """
    Example:
        {'id': '1', 'correlation_id': None, 'undone': '0', 'undone_timestamp': None, 'transaction_type': 'purchase',
            'spoiled': '0', 'amount': '1', 'location_id': '4', 'location_name': 'Candy cupboard', 'product_name': 'Gummy
            bears', 'qu_name': 'Pack', 'qu_name_plural': 'Packs', 'user_display_name': 'Demo User', 'row_created_timestamp':
            '2020-11-14 16:42:21'}

    Attributes:
        correlation_id (Union[Unset, str]):
        undone (Union[Unset, int]):
        undone_timestamp (Union[Unset, datetime.datetime]):
        amount (Union[Unset, float]):
        location_id (Union[Unset, int]):
        location_name (Union[Unset, str]):
        product_name (Union[Unset, str]):
        qu_name (Union[Unset, str]):
        qu_name_plural (Union[Unset, str]):
        user_display_name (Union[Unset, str]):
        spoiled (Union[Unset, bool]):  Default: False.
        transaction_type (Union[Unset, StockTransactionType]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
    """

    correlation_id: Union[Unset, str] = UNSET
    undone: Union[Unset, int] = UNSET
    undone_timestamp: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    location_id: Union[Unset, int] = UNSET
    location_name: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    qu_name: Union[Unset, str] = UNSET
    qu_name_plural: Union[Unset, str] = UNSET
    user_display_name: Union[Unset, str] = UNSET
    spoiled: Union[Unset, bool] = False
    transaction_type: Union[Unset, StockTransactionType] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        correlation_id = self.correlation_id

        undone = self.undone

        undone_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.undone_timestamp, Unset):
            undone_timestamp = self.undone_timestamp.isoformat()

        amount = self.amount

        location_id = self.location_id

        location_name = self.location_name

        product_name = self.product_name

        qu_name = self.qu_name

        qu_name_plural = self.qu_name_plural

        user_display_name = self.user_display_name

        spoiled = self.spoiled

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if undone is not UNSET:
            field_dict["undone"] = undone
        if undone_timestamp is not UNSET:
            field_dict["undone_timestamp"] = undone_timestamp
        if amount is not UNSET:
            field_dict["amount"] = amount
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if qu_name is not UNSET:
            field_dict["qu_name"] = qu_name
        if qu_name_plural is not UNSET:
            field_dict["qu_name_plural"] = qu_name_plural
        if user_display_name is not UNSET:
            field_dict["user_display_name"] = user_display_name
        if spoiled is not UNSET:
            field_dict["spoiled"] = spoiled
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        correlation_id = d.pop("correlation_id", UNSET)

        undone = d.pop("undone", UNSET)

        _undone_timestamp = d.pop("undone_timestamp", UNSET)
        undone_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_undone_timestamp, Unset):
            undone_timestamp = UNSET
        else:
            undone_timestamp = isoparse(_undone_timestamp)

        amount = d.pop("amount", UNSET)

        location_id = d.pop("location_id", UNSET)

        location_name = d.pop("location_name", UNSET)

        product_name = d.pop("product_name", UNSET)

        qu_name = d.pop("qu_name", UNSET)

        qu_name_plural = d.pop("qu_name_plural", UNSET)

        user_display_name = d.pop("user_display_name", UNSET)

        spoiled = d.pop("spoiled", UNSET)

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, StockTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = StockTransactionType(_transaction_type)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        stock_journal = cls(
            correlation_id=correlation_id,
            undone=undone,
            undone_timestamp=undone_timestamp,
            amount=amount,
            location_id=location_id,
            location_name=location_name,
            product_name=product_name,
            qu_name=qu_name,
            qu_name_plural=qu_name_plural,
            user_display_name=user_display_name,
            spoiled=spoiled,
            transaction_type=transaction_type,
            row_created_timestamp=row_created_timestamp,
        )

        stock_journal.additional_properties = d
        return stock_journal

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
