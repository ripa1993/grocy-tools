from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stock_transaction_type import StockTransactionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStockProductsByBarcodeBarcodeConsumeBody")


@_attrs_define
class PostStockProductsByBarcodeBarcodeConsumeBody:
    """
    Example:
        {'amount': 1, 'transaction_type': 'consume', 'spoiled': False}

    Attributes:
        amount (Union[Unset, float]): The amount to remove - please note that when tare weight handling for the product
            is enabled, this needs to be the amount including the container weight (gross), the amount to be posted will be
            automatically calculated based on what is in stock and the defined tare weight
        transaction_type (Union[Unset, StockTransactionType]):
        spoiled (Union[Unset, bool]): True when the given product was spoiled, defaults to false
        stock_entry_id (Union[Unset, str]): A specific stock entry id to consume, if used, the amount has to be 1
        recipe_id (Union[Unset, int]): A valid recipe id for which this product was used (for statistical purposes only)
        location_id (Union[Unset, int]): A valid location id (if supplied, only stock at the given location is
            considered, if ommitted, stock of any location is considered)
        exact_amount (Union[Unset, bool]): For tare weight handling enabled products, `true` when the given is the
            absolute amount to be consumed, not the amount including the container weight
        allow_subproduct_substitution (Union[Unset, bool]): `rue` when any in-stock sub product should be used when the
            given product is a parent product and currently not in-stock
    """

    amount: Union[Unset, float] = UNSET
    transaction_type: Union[Unset, StockTransactionType] = UNSET
    spoiled: Union[Unset, bool] = UNSET
    stock_entry_id: Union[Unset, str] = UNSET
    recipe_id: Union[Unset, int] = UNSET
    location_id: Union[Unset, int] = UNSET
    exact_amount: Union[Unset, bool] = UNSET
    allow_subproduct_substitution: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount

        transaction_type: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_type, Unset):
            transaction_type = self.transaction_type.value

        spoiled = self.spoiled

        stock_entry_id = self.stock_entry_id

        recipe_id = self.recipe_id

        location_id = self.location_id

        exact_amount = self.exact_amount

        allow_subproduct_substitution = self.allow_subproduct_substitution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if spoiled is not UNSET:
            field_dict["spoiled"] = spoiled
        if stock_entry_id is not UNSET:
            field_dict["stock_entry_id"] = stock_entry_id
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if exact_amount is not UNSET:
            field_dict["exact_amount"] = exact_amount
        if allow_subproduct_substitution is not UNSET:
            field_dict["allow_subproduct_substitution"] = allow_subproduct_substitution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount", UNSET)

        _transaction_type = d.pop("transaction_type", UNSET)
        transaction_type: Union[Unset, StockTransactionType]
        if isinstance(_transaction_type, Unset):
            transaction_type = UNSET
        else:
            transaction_type = StockTransactionType(_transaction_type)

        spoiled = d.pop("spoiled", UNSET)

        stock_entry_id = d.pop("stock_entry_id", UNSET)

        recipe_id = d.pop("recipe_id", UNSET)

        location_id = d.pop("location_id", UNSET)

        exact_amount = d.pop("exact_amount", UNSET)

        allow_subproduct_substitution = d.pop("allow_subproduct_substitution", UNSET)

        post_stock_products_by_barcode_barcode_consume_body = cls(
            amount=amount,
            transaction_type=transaction_type,
            spoiled=spoiled,
            stock_entry_id=stock_entry_id,
            recipe_id=recipe_id,
            location_id=location_id,
            exact_amount=exact_amount,
            allow_subproduct_substitution=allow_subproduct_substitution,
        )

        post_stock_products_by_barcode_barcode_consume_body.additional_properties = d
        return post_stock_products_by_barcode_barcode_consume_body

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
