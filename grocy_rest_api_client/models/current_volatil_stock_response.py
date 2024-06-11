from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.current_stock_response import CurrentStockResponse
    from ..models.current_volatil_stock_response_missing_products_item import (
        CurrentVolatilStockResponseMissingProductsItem,
    )


T = TypeVar("T", bound="CurrentVolatilStockResponse")


@_attrs_define
class CurrentVolatilStockResponse:
    """
    Attributes:
        due_products (Union[Unset, List['CurrentStockResponse']]):
        overdue_products (Union[Unset, List['CurrentStockResponse']]):
        expired_products (Union[Unset, List['CurrentStockResponse']]):
        missing_products (Union[Unset, List['CurrentVolatilStockResponseMissingProductsItem']]):
    """

    due_products: Union[Unset, List["CurrentStockResponse"]] = UNSET
    overdue_products: Union[Unset, List["CurrentStockResponse"]] = UNSET
    expired_products: Union[Unset, List["CurrentStockResponse"]] = UNSET
    missing_products: Union[Unset, List["CurrentVolatilStockResponseMissingProductsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        due_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.due_products, Unset):
            due_products = []
            for due_products_item_data in self.due_products:
                due_products_item = due_products_item_data.to_dict()
                due_products.append(due_products_item)

        overdue_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.overdue_products, Unset):
            overdue_products = []
            for overdue_products_item_data in self.overdue_products:
                overdue_products_item = overdue_products_item_data.to_dict()
                overdue_products.append(overdue_products_item)

        expired_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.expired_products, Unset):
            expired_products = []
            for expired_products_item_data in self.expired_products:
                expired_products_item = expired_products_item_data.to_dict()
                expired_products.append(expired_products_item)

        missing_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.missing_products, Unset):
            missing_products = []
            for missing_products_item_data in self.missing_products:
                missing_products_item = missing_products_item_data.to_dict()
                missing_products.append(missing_products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if due_products is not UNSET:
            field_dict["due_products"] = due_products
        if overdue_products is not UNSET:
            field_dict["overdue_products"] = overdue_products
        if expired_products is not UNSET:
            field_dict["expired_products"] = expired_products
        if missing_products is not UNSET:
            field_dict["missing_products"] = missing_products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.current_stock_response import CurrentStockResponse
        from ..models.current_volatil_stock_response_missing_products_item import (
            CurrentVolatilStockResponseMissingProductsItem,
        )

        d = src_dict.copy()
        due_products = []
        _due_products = d.pop("due_products", UNSET)
        for due_products_item_data in _due_products or []:
            due_products_item = CurrentStockResponse.from_dict(due_products_item_data)

            due_products.append(due_products_item)

        overdue_products = []
        _overdue_products = d.pop("overdue_products", UNSET)
        for overdue_products_item_data in _overdue_products or []:
            overdue_products_item = CurrentStockResponse.from_dict(overdue_products_item_data)

            overdue_products.append(overdue_products_item)

        expired_products = []
        _expired_products = d.pop("expired_products", UNSET)
        for expired_products_item_data in _expired_products or []:
            expired_products_item = CurrentStockResponse.from_dict(expired_products_item_data)

            expired_products.append(expired_products_item)

        missing_products = []
        _missing_products = d.pop("missing_products", UNSET)
        for missing_products_item_data in _missing_products or []:
            missing_products_item = CurrentVolatilStockResponseMissingProductsItem.from_dict(missing_products_item_data)

            missing_products.append(missing_products_item)

        current_volatil_stock_response = cls(
            due_products=due_products,
            overdue_products=overdue_products,
            expired_products=expired_products,
            missing_products=missing_products,
        )

        current_volatil_stock_response.additional_properties = d
        return current_volatil_stock_response

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
