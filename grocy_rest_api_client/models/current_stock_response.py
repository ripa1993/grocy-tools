import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_without_userfields import ProductWithoutUserfields


T = TypeVar("T", bound="CurrentStockResponse")


@_attrs_define
class CurrentStockResponse:
    """
    Attributes:
        product_id (Union[Unset, int]):
        amount (Union[Unset, float]):
        amount_aggregated (Union[Unset, float]):
        amount_opened (Union[Unset, float]):
        amount_opened_aggregated (Union[Unset, float]):
        best_before_date (Union[Unset, datetime.date]): The next due date for this product
        is_aggregated_amount (Union[Unset, bool]): Indicates wheter this product has sub-products or not / if the fields
            `amount_aggregated` and `amount_opened_aggregated` are filled
        product (Union[Unset, ProductWithoutUserfields]):  Example: {'id': '1', 'name': 'Cookies', 'description': None,
            'location_id': '4', 'qu_id_purchase': '3', 'qu_id_stock': '3', 'min_stock_amount': '8',
            'default_best_before_days': '0', 'row_created_timestamp': '2019-05-02 20:12:26', 'product_group_id': '1',
            'picture_file_name': 'cookies.jpg', 'default_best_before_days_after_open': '0', 'enable_tare_weight_handling':
            '0', 'tare_weight': '0.0', 'not_check_stock_fulfillment_for_recipes': '0', 'shopping_location_id': None,
            'userfields': None, 'should_not_be_frozen': '1', 'default_consume_location_id': '5', 'move_on_open': '1'}.
    """

    product_id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    amount_aggregated: Union[Unset, float] = UNSET
    amount_opened: Union[Unset, float] = UNSET
    amount_opened_aggregated: Union[Unset, float] = UNSET
    best_before_date: Union[Unset, datetime.date] = UNSET
    is_aggregated_amount: Union[Unset, bool] = UNSET
    product: Union[Unset, "ProductWithoutUserfields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_id = self.product_id

        amount = self.amount

        amount_aggregated = self.amount_aggregated

        amount_opened = self.amount_opened

        amount_opened_aggregated = self.amount_opened_aggregated

        best_before_date: Union[Unset, str] = UNSET
        if not isinstance(self.best_before_date, Unset):
            best_before_date = self.best_before_date.isoformat()

        is_aggregated_amount = self.is_aggregated_amount

        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_aggregated is not UNSET:
            field_dict["amount_aggregated"] = amount_aggregated
        if amount_opened is not UNSET:
            field_dict["amount_opened"] = amount_opened
        if amount_opened_aggregated is not UNSET:
            field_dict["amount_opened_aggregated"] = amount_opened_aggregated
        if best_before_date is not UNSET:
            field_dict["best_before_date"] = best_before_date
        if is_aggregated_amount is not UNSET:
            field_dict["is_aggregated_amount"] = is_aggregated_amount
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_without_userfields import ProductWithoutUserfields

        d = src_dict.copy()
        product_id = d.pop("product_id", UNSET)

        amount = d.pop("amount", UNSET)

        amount_aggregated = d.pop("amount_aggregated", UNSET)

        amount_opened = d.pop("amount_opened", UNSET)

        amount_opened_aggregated = d.pop("amount_opened_aggregated", UNSET)

        _best_before_date = d.pop("best_before_date", UNSET)
        best_before_date: Union[Unset, datetime.date]
        if isinstance(_best_before_date, Unset):
            best_before_date = UNSET
        else:
            best_before_date = isoparse(_best_before_date).date()

        is_aggregated_amount = d.pop("is_aggregated_amount", UNSET)

        _product = d.pop("product", UNSET)
        product: Union[Unset, ProductWithoutUserfields]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = ProductWithoutUserfields.from_dict(_product)

        current_stock_response = cls(
            product_id=product_id,
            amount=amount,
            amount_aggregated=amount_aggregated,
            amount_opened=amount_opened,
            amount_opened_aggregated=amount_opened_aggregated,
            best_before_date=best_before_date,
            is_aggregated_amount=is_aggregated_amount,
            product=product,
        )

        current_stock_response.additional_properties = d
        return current_stock_response

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
