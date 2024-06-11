import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTasksTaskIdCompleteBody")


@_attrs_define
class PostTasksTaskIdCompleteBody:
    """
    Attributes:
        done_time (Union[Unset, datetime.datetime]): The time of when the task was completed, when omitted, the current
            time is used
    """

    done_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        done_time: Union[Unset, str] = UNSET
        if not isinstance(self.done_time, Unset):
            done_time = self.done_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if done_time is not UNSET:
            field_dict["done_time"] = done_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _done_time = d.pop("done_time", UNSET)
        done_time: Union[Unset, datetime.datetime]
        if isinstance(_done_time, Unset):
            done_time = UNSET
        else:
            done_time = isoparse(_done_time)

        post_tasks_task_id_complete_body = cls(
            done_time=done_time,
        )

        post_tasks_task_id_complete_body.additional_properties = d
        return post_tasks_task_id_complete_body

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
