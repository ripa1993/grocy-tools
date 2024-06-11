import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.chore_assignment_type import ChoreAssignmentType
from ..models.chore_period_type import ChorePeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chore_userfields import ChoreUserfields


T = TypeVar("T", bound="Chore")


@_attrs_define
class Chore:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        period_type (Union[Unset, ChorePeriodType]):
        period_config (Union[Unset, str]):
        period_days (Union[Unset, int]):
        track_date_only (Union[Unset, bool]):
        rollover (Union[Unset, bool]):
        assignment_type (Union[Unset, ChoreAssignmentType]):
        assignment_config (Union[Unset, str]):
        next_execution_assigned_to_user_id (Union[Unset, int]):
        start_date (Union[Unset, datetime.datetime]):
        rescheduled_date (Union[Unset, datetime.datetime]):
        rescheduled_next_execution_assigned_to_user_id (Union[Unset, int]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
        userfields (Union[Unset, ChoreUserfields]): Key/value pairs of userfields
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    period_type: Union[Unset, ChorePeriodType] = UNSET
    period_config: Union[Unset, str] = UNSET
    period_days: Union[Unset, int] = UNSET
    track_date_only: Union[Unset, bool] = UNSET
    rollover: Union[Unset, bool] = UNSET
    assignment_type: Union[Unset, ChoreAssignmentType] = UNSET
    assignment_config: Union[Unset, str] = UNSET
    next_execution_assigned_to_user_id: Union[Unset, int] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    rescheduled_date: Union[Unset, datetime.datetime] = UNSET
    rescheduled_next_execution_assigned_to_user_id: Union[Unset, int] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    userfields: Union[Unset, "ChoreUserfields"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        period_type: Union[Unset, str] = UNSET
        if not isinstance(self.period_type, Unset):
            period_type = self.period_type.value

        period_config = self.period_config

        period_days = self.period_days

        track_date_only = self.track_date_only

        rollover = self.rollover

        assignment_type: Union[Unset, str] = UNSET
        if not isinstance(self.assignment_type, Unset):
            assignment_type = self.assignment_type.value

        assignment_config = self.assignment_config

        next_execution_assigned_to_user_id = self.next_execution_assigned_to_user_id

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        rescheduled_date: Union[Unset, str] = UNSET
        if not isinstance(self.rescheduled_date, Unset):
            rescheduled_date = self.rescheduled_date.isoformat()

        rescheduled_next_execution_assigned_to_user_id = self.rescheduled_next_execution_assigned_to_user_id

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
        if period_type is not UNSET:
            field_dict["period_type"] = period_type
        if period_config is not UNSET:
            field_dict["period_config"] = period_config
        if period_days is not UNSET:
            field_dict["period_days"] = period_days
        if track_date_only is not UNSET:
            field_dict["track_date_only"] = track_date_only
        if rollover is not UNSET:
            field_dict["rollover"] = rollover
        if assignment_type is not UNSET:
            field_dict["assignment_type"] = assignment_type
        if assignment_config is not UNSET:
            field_dict["assignment_config"] = assignment_config
        if next_execution_assigned_to_user_id is not UNSET:
            field_dict["next_execution_assigned_to_user_id"] = next_execution_assigned_to_user_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if rescheduled_date is not UNSET:
            field_dict["rescheduled_date"] = rescheduled_date
        if rescheduled_next_execution_assigned_to_user_id is not UNSET:
            field_dict["rescheduled_next_execution_assigned_to_user_id"] = (
                rescheduled_next_execution_assigned_to_user_id
            )
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if userfields is not UNSET:
            field_dict["userfields"] = userfields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chore_userfields import ChoreUserfields

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _period_type = d.pop("period_type", UNSET)
        period_type: Union[Unset, ChorePeriodType]
        if isinstance(_period_type, Unset):
            period_type = UNSET
        else:
            period_type = ChorePeriodType(_period_type)

        period_config = d.pop("period_config", UNSET)

        period_days = d.pop("period_days", UNSET)

        track_date_only = d.pop("track_date_only", UNSET)

        rollover = d.pop("rollover", UNSET)

        _assignment_type = d.pop("assignment_type", UNSET)
        assignment_type: Union[Unset, ChoreAssignmentType]
        if isinstance(_assignment_type, Unset):
            assignment_type = UNSET
        else:
            assignment_type = ChoreAssignmentType(_assignment_type)

        assignment_config = d.pop("assignment_config", UNSET)

        next_execution_assigned_to_user_id = d.pop("next_execution_assigned_to_user_id", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _rescheduled_date = d.pop("rescheduled_date", UNSET)
        rescheduled_date: Union[Unset, datetime.datetime]
        if isinstance(_rescheduled_date, Unset):
            rescheduled_date = UNSET
        else:
            rescheduled_date = isoparse(_rescheduled_date)

        rescheduled_next_execution_assigned_to_user_id = d.pop("rescheduled_next_execution_assigned_to_user_id", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        _userfields = d.pop("userfields", UNSET)
        userfields: Union[Unset, ChoreUserfields]
        if isinstance(_userfields, Unset):
            userfields = UNSET
        else:
            userfields = ChoreUserfields.from_dict(_userfields)

        chore = cls(
            id=id,
            name=name,
            description=description,
            period_type=period_type,
            period_config=period_config,
            period_days=period_days,
            track_date_only=track_date_only,
            rollover=rollover,
            assignment_type=assignment_type,
            assignment_config=assignment_config,
            next_execution_assigned_to_user_id=next_execution_assigned_to_user_id,
            start_date=start_date,
            rescheduled_date=rescheduled_date,
            rescheduled_next_execution_assigned_to_user_id=rescheduled_next_execution_assigned_to_user_id,
            row_created_timestamp=row_created_timestamp,
            userfields=userfields,
        )

        chore.additional_properties = d
        return chore

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
