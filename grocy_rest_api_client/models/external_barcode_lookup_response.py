from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalBarcodeLookupResponse")


@_attrs_define
class ExternalBarcodeLookupResponse:
    """
    Attributes:
        name (Union[Unset, str]):
        location_id (Union[Unset, int]):
        qu_id_purchase (Union[Unset, int]):
        qu_id_stock (Union[Unset, int]):
        qu_factor_purchase_to_stock (Union[Unset, float]):
        barcode (Union[Unset, str]): Can contain multiple barcodes separated by comma
        id (Union[Unset, int]): The id of the added product, only included when the producted was added to the database
    """

    name: Union[Unset, str] = UNSET
    location_id: Union[Unset, int] = UNSET
    qu_id_purchase: Union[Unset, int] = UNSET
    qu_id_stock: Union[Unset, int] = UNSET
    qu_factor_purchase_to_stock: Union[Unset, float] = UNSET
    barcode: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        location_id = self.location_id

        qu_id_purchase = self.qu_id_purchase

        qu_id_stock = self.qu_id_stock

        qu_factor_purchase_to_stock = self.qu_factor_purchase_to_stock

        barcode = self.barcode

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if qu_id_purchase is not UNSET:
            field_dict["qu_id_purchase"] = qu_id_purchase
        if qu_id_stock is not UNSET:
            field_dict["qu_id_stock"] = qu_id_stock
        if qu_factor_purchase_to_stock is not UNSET:
            field_dict["qu_factor_purchase_to_stock"] = qu_factor_purchase_to_stock
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        location_id = d.pop("location_id", UNSET)

        qu_id_purchase = d.pop("qu_id_purchase", UNSET)

        qu_id_stock = d.pop("qu_id_stock", UNSET)

        qu_factor_purchase_to_stock = d.pop("qu_factor_purchase_to_stock", UNSET)

        barcode = d.pop("barcode", UNSET)

        id = d.pop("id", UNSET)

        external_barcode_lookup_response = cls(
            name=name,
            location_id=location_id,
            qu_id_purchase=qu_id_purchase,
            qu_id_stock=qu_id_stock,
            qu_factor_purchase_to_stock=qu_factor_purchase_to_stock,
            barcode=barcode,
            id=id,
        )

        external_barcode_lookup_response.additional_properties = d
        return external_barcode_lookup_response

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
