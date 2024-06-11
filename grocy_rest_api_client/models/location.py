import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_userfields import LocationUserfields


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """
    Example:
        {'id': '2', 'name': '0', 'description': None, 'row_created_timestamp': '2019-05-02 20:12:25', 'userfields':
            None}

    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
        userfields (Union[Unset, LocationUserfields]): Key/value pairs of userfields
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    userfields: Union[Unset, "LocationUserfields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

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
        if description is not UNSET:
            field_dict["description"] = description
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if userfields is not UNSET:
            field_dict["userfields"] = userfields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_userfields import LocationUserfields

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        _userfields = d.pop("userfields", UNSET)
        userfields: Union[Unset, LocationUserfields]
        if isinstance(_userfields, Unset):
            userfields = UNSET
        else:
            userfields = LocationUserfields.from_dict(_userfields)

        location = cls(
            id=id,
            name=name,
            description=description,
            row_created_timestamp=row_created_timestamp,
            userfields=userfields,
        )

        location.additional_properties = d
        return location

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
