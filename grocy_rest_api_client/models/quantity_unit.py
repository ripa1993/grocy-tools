import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quantity_unit_userfields import QuantityUnitUserfields


T = TypeVar("T", bound="QuantityUnit")


@_attrs_define
class QuantityUnit:
    """
    Example:
        {'id': '2', 'name': 'Piece', 'description': None, 'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural':
            'Pieces', 'plural_forms': None, 'userfields': None}

    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        name_plural (Union[Unset, str]):
        description (Union[Unset, str]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
        plural_forms (Union[Unset, str]):
        userfields (Union[Unset, QuantityUnitUserfields]): Key/value pairs of userfields
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    name_plural: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    plural_forms: Union[Unset, str] = UNSET
    userfields: Union[Unset, "QuantityUnitUserfields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        name_plural = self.name_plural

        description = self.description

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        plural_forms = self.plural_forms

        userfields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.userfields, Unset):
            userfields = self.userfields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if name_plural is not UNSET:
            field_dict["name_plural"] = name_plural
        if description is not UNSET:
            field_dict["description"] = description
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if plural_forms is not UNSET:
            field_dict["plural_forms"] = plural_forms
        if userfields is not UNSET:
            field_dict["userfields"] = userfields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quantity_unit_userfields import QuantityUnitUserfields

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        name_plural = d.pop("name_plural", UNSET)

        description = d.pop("description", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        plural_forms = d.pop("plural_forms", UNSET)

        _userfields = d.pop("userfields", UNSET)
        userfields: Union[Unset, QuantityUnitUserfields]
        if isinstance(_userfields, Unset):
            userfields = UNSET
        else:
            userfields = QuantityUnitUserfields.from_dict(_userfields)

        quantity_unit = cls(
            id=id,
            name=name,
            name_plural=name_plural,
            description=description,
            row_created_timestamp=row_created_timestamp,
            plural_forms=plural_forms,
            userfields=userfields,
        )

        quantity_unit.additional_properties = d
        return quantity_unit

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
