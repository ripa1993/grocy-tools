import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shopping_location import ShoppingLocation


T = TypeVar("T", bound="ProductPriceHistory")


@_attrs_define
class ProductPriceHistory:
    """
    Attributes:
        date (Union[Unset, datetime.datetime]):
        price (Union[Unset, float]):
        shopping_location (Union[Unset, ShoppingLocation]):  Example: {'id': '2', 'name': '0', 'description': None,
            'row_created_timestamp': '2019-05-02 20:12:25', 'userfields': None}.
    """

    date: Union[Unset, datetime.datetime] = UNSET
    price: Union[Unset, float] = UNSET
    shopping_location: Union[Unset, "ShoppingLocation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        price = self.price

        shopping_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shopping_location, Unset):
            shopping_location = self.shopping_location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if price is not UNSET:
            field_dict["price"] = price
        if shopping_location is not UNSET:
            field_dict["shopping_location"] = shopping_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.shopping_location import ShoppingLocation

        d = src_dict.copy()
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        price = d.pop("price", UNSET)

        _shopping_location = d.pop("shopping_location", UNSET)
        shopping_location: Union[Unset, ShoppingLocation]
        if isinstance(_shopping_location, Unset):
            shopping_location = UNSET
        else:
            shopping_location = ShoppingLocation.from_dict(_shopping_location)

        product_price_history = cls(
            date=date,
            price=price,
            shopping_location=shopping_location,
        )

        product_price_history.additional_properties = d
        return product_price_history

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
