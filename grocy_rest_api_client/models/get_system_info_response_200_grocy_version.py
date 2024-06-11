import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSystemInfoResponse200GrocyVersion")


@_attrs_define
class GetSystemInfoResponse200GrocyVersion:
    """
    Attributes:
        version (Union[Unset, str]):
        release_date (Union[Unset, datetime.date]):
    """

    version: Union[Unset, str] = UNSET
    release_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version

        release_date: Union[Unset, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["Version"] = version
        if release_date is not UNSET:
            field_dict["ReleaseDate"] = release_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("Version", UNSET)

        _release_date = d.pop("ReleaseDate", UNSET)
        release_date: Union[Unset, datetime.date]
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        get_system_info_response_200_grocy_version = cls(
            version=version,
            release_date=release_date,
        )

        get_system_info_response_200_grocy_version.additional_properties = d
        return get_system_info_response_200_grocy_version

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
