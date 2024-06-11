import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentBatteryResponse")


@_attrs_define
class CurrentBatteryResponse:
    """
    Attributes:
        battery_id (Union[Unset, int]):
        last_tracked_time (Union[Unset, datetime.datetime]):
        next_estimated_charge_time (Union[Unset, datetime.datetime]): The next estimated charge time of this battery,
            2999-12-31 23:59:59 when the given battery has no charge_interval_days defined
    """

    battery_id: Union[Unset, int] = UNSET
    last_tracked_time: Union[Unset, datetime.datetime] = UNSET
    next_estimated_charge_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        battery_id = self.battery_id

        last_tracked_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_tracked_time, Unset):
            last_tracked_time = self.last_tracked_time.isoformat()

        next_estimated_charge_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_estimated_charge_time, Unset):
            next_estimated_charge_time = self.next_estimated_charge_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if battery_id is not UNSET:
            field_dict["battery_id"] = battery_id
        if last_tracked_time is not UNSET:
            field_dict["last_tracked_time"] = last_tracked_time
        if next_estimated_charge_time is not UNSET:
            field_dict["next_estimated_charge_time"] = next_estimated_charge_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        battery_id = d.pop("battery_id", UNSET)

        _last_tracked_time = d.pop("last_tracked_time", UNSET)
        last_tracked_time: Union[Unset, datetime.datetime]
        if isinstance(_last_tracked_time, Unset):
            last_tracked_time = UNSET
        else:
            last_tracked_time = isoparse(_last_tracked_time)

        _next_estimated_charge_time = d.pop("next_estimated_charge_time", UNSET)
        next_estimated_charge_time: Union[Unset, datetime.datetime]
        if isinstance(_next_estimated_charge_time, Unset):
            next_estimated_charge_time = UNSET
        else:
            next_estimated_charge_time = isoparse(_next_estimated_charge_time)

        current_battery_response = cls(
            battery_id=battery_id,
            last_tracked_time=last_tracked_time,
            next_estimated_charge_time=next_estimated_charge_time,
        )

        current_battery_response.additional_properties = d
        return current_battery_response

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
