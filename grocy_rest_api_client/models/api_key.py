import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKey")


@_attrs_define
class ApiKey:
    """
    Attributes:
        id (Union[Unset, int]):
        api_key (Union[Unset, str]):
        expires (Union[Unset, datetime.datetime]):
        last_used (Union[Unset, datetime.datetime]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    api_key: Union[Unset, str] = UNSET
    expires: Union[Unset, datetime.datetime] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        api_key = self.api_key

        expires: Union[Unset, str] = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if expires is not UNSET:
            field_dict["expires"] = expires
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        api_key = d.pop("api_key", UNSET)

        _expires = d.pop("expires", UNSET)
        expires: Union[Unset, datetime.datetime]
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        _last_used = d.pop("last_used", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        api_key = cls(
            id=id,
            api_key=api_key,
            expires=expires,
            last_used=last_used,
            row_created_timestamp=row_created_timestamp,
        )

        api_key.additional_properties = d
        return api_key

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
