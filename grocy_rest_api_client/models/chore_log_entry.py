import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChoreLogEntry")


@_attrs_define
class ChoreLogEntry:
    """
    Attributes:
        id (Union[Unset, int]):
        chore_id (Union[Unset, int]):
        tracked_time (Union[Unset, datetime.datetime]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    chore_id: Union[Unset, int] = UNSET
    tracked_time: Union[Unset, datetime.datetime] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        chore_id = self.chore_id

        tracked_time: Union[Unset, str] = UNSET
        if not isinstance(self.tracked_time, Unset):
            tracked_time = self.tracked_time.isoformat()

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if chore_id is not UNSET:
            field_dict["chore_id"] = chore_id
        if tracked_time is not UNSET:
            field_dict["tracked_time"] = tracked_time
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        chore_id = d.pop("chore_id", UNSET)

        _tracked_time = d.pop("tracked_time", UNSET)
        tracked_time: Union[Unset, datetime.datetime]
        if isinstance(_tracked_time, Unset):
            tracked_time = UNSET
        else:
            tracked_time = isoparse(_tracked_time)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        chore_log_entry = cls(
            id=id,
            chore_id=chore_id,
            tracked_time=tracked_time,
            row_created_timestamp=row_created_timestamp,
        )

        chore_log_entry.additional_properties = d
        return chore_log_entry

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
