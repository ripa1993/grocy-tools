import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.stock_transaction_type import StockTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockProductsByBarcodeBarcodeAddBody")


@_attrs_define
class PostStockProductsByBarcodeBarcodeAddBody:
    """
    Example:
        {'amount': 1, 'best_before_date': '2019-01-19', 'transaction_type': 'purchase', 'price': '1.99'}

    Attributes:
        amount (Union[Unset, float]): The amount to add - please note that when tare weight handling for the product is
            enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be
            automatically calculated based on what is in stock and the defined tare weight
        best_before_date (Union[Unset, datetime.date]): The due date of the product to add, when omitted, the current
            date is used
        transaction_type (Union[Unset, StockTransactionType]):
        price (Union[Unset, float]): The price per stock quantity unit in configured currency
        location_id (Union[Unset, int]): If omitted, the default location of the product is used
    """

    amount: Union[Unset, float] = UNSET
    best_before_date: Union[Unset, datetime.date] = UNSET
    transaction_type: Union[Unset, StockTransactionType] = UNSET
    price: Union[Unset, float] = UNSET
    location_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        best_before_date: Union[Unset, str] = UNSET
        if not isinstance(self.best_before_date, Unset):
            best_before_date = self.best_before_date.isoformat()

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        price = self.price

        location_id = self.location_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if best_before_date is not UNSET:
            field_dict["best_before_date"] = best_before_date
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if price is not UNSET:
            field_dict["price"] = price
        if location_id is not UNSET:
            field_dict["location_id"] = location_id

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

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, StockTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = StockTransactionType(_transaction_type)

        price = d.pop("price", UNSET)

        location_id = d.pop("location_id", UNSET)

        post_stock_products_by_barcode_barcode_add_body = cls(
            amount=amount,
            best_before_date=best_before_date,
            transaction_type=transaction_type,
            price=price,
            location_id=location_id,
        )

        post_stock_products_by_barcode_barcode_add_body.additional_properties = d
        return post_stock_products_by_barcode_barcode_add_body

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
