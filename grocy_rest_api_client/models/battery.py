import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.battery_userfields import BatteryUserfields


T = TypeVar("T", bound="Battery")


@_attrs_define
class Battery:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        used_in (Union[Unset, str]):
        charge_interval_days (Union[Unset, int]):  Default: 0.
        row_created_timestamp (Union[Unset, datetime.datetime]):
        userfields (Union[Unset, BatteryUserfields]): Key/value pairs of userfields
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    used_in: Union[Unset, str] = UNSET
    charge_interval_days: Union[Unset, int] = 0
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    userfields: Union[Unset, "BatteryUserfields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        used_in = self.used_in

        charge_interval_days = self.charge_interval_days

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
        if used_in is not UNSET:
            field_dict["used_in"] = used_in
        if charge_interval_days is not UNSET:
            field_dict["charge_interval_days"] = charge_interval_days
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if userfields is not UNSET:
            field_dict["userfields"] = userfields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.battery_userfields import BatteryUserfields

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        used_in = d.pop("used_in", UNSET)

        charge_interval_days = d.pop("charge_interval_days", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        _userfields = d.pop("userfields", UNSET)
        userfields: Union[Unset, BatteryUserfields]
        if isinstance(_userfields, Unset):
            userfields = UNSET
        else:
            userfields = BatteryUserfields.from_dict(_userfields)

        battery = cls(
            id=id,
            name=name,
            description=description,
            used_in=used_in,
            charge_interval_days=charge_interval_days,
            row_created_timestamp=row_created_timestamp,
            userfields=userfields,
        )

        battery.additional_properties = d
        return battery

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
