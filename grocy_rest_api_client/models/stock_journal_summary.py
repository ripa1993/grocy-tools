from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stock_transaction_type import StockTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StockJournalSummary")


@_attrs_define
class StockJournalSummary:
    """
    Example:
        {'id': '1', 'user_id': '1', 'user_display_name': 'Demo User', 'product_name': 'Chocolate', 'product_id': '2',
            'transaction_type': 'purchase', 'qu_name': 'Pack', 'qu_name_plural': 'Packs', 'amount': '1'}

    Attributes:
        amount (Union[Unset, float]):
        user_id (Union[Unset, int]):
        product_name (Union[Unset, str]):
        product_id (Union[Unset, int]):
        qu_name (Union[Unset, str]):
        qu_name_plural (Union[Unset, str]):
        user_display_name (Union[Unset, str]):
        transaction_type (Union[Unset, StockTransactionType]):
    """

    amount: Union[Unset, float] = UNSET
    user_id: Union[Unset, int] = UNSET
    product_name: Union[Unset, str] = UNSET
    product_id: Union[Unset, int] = UNSET
    qu_name: Union[Unset, str] = UNSET
    qu_name_plural: Union[Unset, str] = UNSET
    user_display_name: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, StockTransactionType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        user_id = self.user_id

        product_name = self.product_name

        product_id = self.product_id

        qu_name = self.qu_name

        qu_name_plural = self.qu_name_plural

        user_display_name = self.user_display_name

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if qu_name is not UNSET:
            field_dict["qu_name"] = qu_name
        if qu_name_plural is not UNSET:
            field_dict["qu_name_plural"] = qu_name_plural
        if user_display_name is not UNSET:
            field_dict["user_display_name"] = user_display_name
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        user_id = d.pop("user_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_id = d.pop("product_id", UNSET)

        qu_name = d.pop("qu_name", UNSET)

        qu_name_plural = d.pop("qu_name_plural", UNSET)

        user_display_name = d.pop("user_display_name", UNSET)

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, StockTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = StockTransactionType(_transaction_type)

        stock_journal_summary = cls(
            amount=amount,
            user_id=user_id,
            product_name=product_name,
            product_id=product_id,
            qu_name=qu_name,
            qu_name_plural=qu_name_plural,
            user_display_name=user_display_name,
            transaction_type=transaction_type,
        )

        stock_journal_summary.additional_properties = d
        return stock_journal_summary

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
