import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DbChangedTimeResponse")


@_attrs_define
class DbChangedTimeResponse:
    """
    Attributes:
        changed_time (Union[Unset, datetime.datetime]):
    """

    changed_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        changed_time: Union[Unset, str] = UNSET
        if not isinstance(self.changed_time, Unset):
            changed_time = self.changed_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if changed_time is not UNSET:
            field_dict["changed_time"] = changed_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _changed_time = d.pop("changed_time", UNSET)
        changed_time: Union[Unset, datetime.datetime]
        if isinstance(_changed_time, Unset):
            changed_time = UNSET
        else:
            changed_time = isoparse(_changed_time)

        db_changed_time_response = cls(
            changed_time=changed_time,
        )

        db_changed_time_response.additional_properties = d
        return db_changed_time_response

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
