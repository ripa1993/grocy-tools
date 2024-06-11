import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeResponse")


@_attrs_define
class TimeResponse:
    """
    Attributes:
        timezone (Union[Unset, str]):
        time_local (Union[Unset, datetime.datetime]):
        time_local_sqlite3 (Union[Unset, datetime.datetime]):
        time_utc (Union[Unset, datetime.datetime]):
        timestamp (Union[Unset, int]):
        offset (Union[Unset, int]):
    """

    timezone: Union[Unset, str] = UNSET
    time_local: Union[Unset, datetime.datetime] = UNSET
    time_local_sqlite3: Union[Unset, datetime.datetime] = UNSET
    time_utc: Union[Unset, datetime.datetime] = UNSET
    timestamp: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timezone = self.timezone

        time_local: Union[Unset, str] = UNSET
        if not isinstance(self.time_local, Unset):
            time_local = self.time_local.isoformat()

        time_local_sqlite3: Union[Unset, str] = UNSET
        if not isinstance(self.time_local_sqlite3, Unset):
            time_local_sqlite3 = self.time_local_sqlite3.isoformat()

        time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.time_utc, Unset):
            time_utc = self.time_utc.isoformat()

        timestamp = self.timestamp

        offset = self.offset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if time_local is not UNSET:
            field_dict["time_local"] = time_local
        if time_local_sqlite3 is not UNSET:
            field_dict["time_local_sqlite3"] = time_local_sqlite3
        if time_utc is not UNSET:
            field_dict["time_utc"] = time_utc
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timezone = d.pop("timezone", UNSET)

        _time_local = d.pop("time_local", UNSET)
        time_local: Union[Unset, datetime.datetime]
        if isinstance(_time_local, Unset):
            time_local = UNSET
        else:
            time_local = isoparse(_time_local)

        _time_local_sqlite3 = d.pop("time_local_sqlite3", UNSET)
        time_local_sqlite3: Union[Unset, datetime.datetime]
        if isinstance(_time_local_sqlite3, Unset):
            time_local_sqlite3 = UNSET
        else:
            time_local_sqlite3 = isoparse(_time_local_sqlite3)

        _time_utc = d.pop("time_utc", UNSET)
        time_utc: Union[Unset, datetime.datetime]
        if isinstance(_time_utc, Unset):
            time_utc = UNSET
        else:
            time_utc = isoparse(_time_utc)

        timestamp = d.pop("timestamp", UNSET)

        offset = d.pop("offset", UNSET)

        time_response = cls(
            timezone=timezone,
            time_local=time_local,
            time_local_sqlite3=time_local_sqlite3,
            time_utc=time_utc,
            timestamp=timestamp,
            offset=offset,
        )

        time_response.additional_properties = d
        return time_response

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
