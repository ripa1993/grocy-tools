import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostBatteriesBatteryIdChargeBody")


@_attrs_define
class PostBatteriesBatteryIdChargeBody:
    """
    Attributes:
        tracked_time (Union[Unset, datetime.datetime]): The time of when the battery was charged, when omitted, the
            current time is used
    """

    tracked_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tracked_time: Union[Unset, str] = UNSET
        if not isinstance(self.tracked_time, Unset):
            tracked_time = self.tracked_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracked_time is not UNSET:
            field_dict["tracked_time"] = tracked_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tracked_time = d.pop("tracked_time", UNSET)
        tracked_time: Union[Unset, datetime.datetime]
        if isinstance(_tracked_time, Unset):
            tracked_time = UNSET
        else:
            tracked_time = isoparse(_tracked_time)

        post_batteries_battery_id_charge_body = cls(
            tracked_time=tracked_time,
        )

        post_batteries_battery_id_charge_body.additional_properties = d
        return post_batteries_battery_id_charge_body

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
