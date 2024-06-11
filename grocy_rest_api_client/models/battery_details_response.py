import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery import Battery


T = TypeVar("T", bound="BatteryDetailsResponse")


@_attrs_define
class BatteryDetailsResponse:
    """
    Example:
        {'battery': {'id': '1', 'name': 'Battery1', 'description': 'Warranty ends 2023', 'used_in': 'TV remote control',
            'charge_interval_days': '0', 'row_created_timestamp': '2019-05-02 20:12:26'}, 'last_charged': '2019-03-13
            18:12:28', 'charge_cycles_count': 4, 'next_estimated_charge_time': '2999-12-31 23:59:59'}

    Attributes:
        chore (Union[Unset, Battery]):
        last_charged (Union[Unset, datetime.datetime]): When this battery was last charged
        charge_cycles_count (Union[Unset, int]): How often this battery was charged so far
        next_estimated_charge_time (Union[Unset, datetime.datetime]):
    """

    chore: Union[Unset, "Battery"] = UNSET
    last_charged: Union[Unset, datetime.datetime] = UNSET
    charge_cycles_count: Union[Unset, int] = UNSET
    next_estimated_charge_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chore: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chore, Unset):
            chore = self.chore.to_dict()

        last_charged: Union[Unset, str] = UNSET
        if not isinstance(self.last_charged, Unset):
            last_charged = self.last_charged.isoformat()

        charge_cycles_count = self.charge_cycles_count

        next_estimated_charge_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_estimated_charge_time, Unset):
            next_estimated_charge_time = self.next_estimated_charge_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chore is not UNSET:
            field_dict["chore"] = chore
        if last_charged is not UNSET:
            field_dict["last_charged"] = last_charged
        if charge_cycles_count is not UNSET:
            field_dict["charge_cycles_count"] = charge_cycles_count
        if next_estimated_charge_time is not UNSET:
            field_dict["next_estimated_charge_time"] = next_estimated_charge_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.battery import Battery

        d = src_dict.copy()
        _chore = d.pop("chore", UNSET)
        chore: Union[Unset, Battery]
        if isinstance(_chore, Unset):
            chore = UNSET
        else:
            chore = Battery.from_dict(_chore)

        _last_charged = d.pop("last_charged", UNSET)
        last_charged: Union[Unset, datetime.datetime]
        if isinstance(_last_charged, Unset):
            last_charged = UNSET
        else:
            last_charged = isoparse(_last_charged)

        charge_cycles_count = d.pop("charge_cycles_count", UNSET)

        _next_estimated_charge_time = d.pop("next_estimated_charge_time", UNSET)
        next_estimated_charge_time: Union[Unset, datetime.datetime]
        if isinstance(_next_estimated_charge_time, Unset):
            next_estimated_charge_time = UNSET
        else:
            next_estimated_charge_time = isoparse(_next_estimated_charge_time)

        battery_details_response = cls(
            chore=chore,
            last_charged=last_charged,
            charge_cycles_count=charge_cycles_count,
            next_estimated_charge_time=next_estimated_charge_time,
        )

        battery_details_response.additional_properties = d
        return battery_details_response

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
