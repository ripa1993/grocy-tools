import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chore import Chore
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="ChoreDetailsResponse")


@_attrs_define
class ChoreDetailsResponse:
    """
    Example:
        {'chore': {'id': 0, 'name': 'string', 'description': 'string', 'period_type': 'manually', 'period_days': 0,
            'row_created_timestamp': '2019-05-04T11:31:04.563Z'}, 'last_tracked': '2019-05-04T11:31:04.563Z', 'track_count':
            0, 'last_done_by': {'id': 0, 'username': 'string', 'first_name': 'string', 'last_name': 'string',
            'display_name': 'string', 'row_created_timestamp': '2019-05-04T11:31:04.564Z'}, 'next_estimated_execution_time':
            '2019-05-04T11:31:04.564Z'}

    Attributes:
        chore (Union[Unset, Chore]):
        last_tracked (Union[Unset, datetime.datetime]): When this chore was last tracked
        track_count (Union[Unset, int]): How often this chore was tracked so far
        last_done_by (Union[Unset, UserDto]): A user object without the *password* and with an additional *display_name*
            property
        next_estimated_execution_time (Union[Unset, datetime.datetime]):
        next_execution_assigned_user (Union[Unset, UserDto]): A user object without the *password* and with an
            additional *display_name* property
        average_execution_frequency_hours (Union[Unset, int]): Contains the average past execution frequency in hours or
            `null`, when the chore was never executed before
    """

    chore: Union[Unset, "Chore"] = UNSET
    last_tracked: Union[Unset, datetime.datetime] = UNSET
    track_count: Union[Unset, int] = UNSET
    last_done_by: Union[Unset, "UserDto"] = UNSET
    next_estimated_execution_time: Union[Unset, datetime.datetime] = UNSET
    next_execution_assigned_user: Union[Unset, "UserDto"] = UNSET
    average_execution_frequency_hours: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chore: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.chore, Unset):
            chore = self.chore.to_dict()

        last_tracked: Union[Unset, str] = UNSET
        if not isinstance(self.last_tracked, Unset):
            last_tracked = self.last_tracked.isoformat()

        track_count = self.track_count

        last_done_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_done_by, Unset):
            last_done_by = self.last_done_by.to_dict()

        next_estimated_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_estimated_execution_time, Unset):
            next_estimated_execution_time = self.next_estimated_execution_time.isoformat()

        next_execution_assigned_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.next_execution_assigned_user, Unset):
            next_execution_assigned_user = self.next_execution_assigned_user.to_dict()

        average_execution_frequency_hours = self.average_execution_frequency_hours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chore is not UNSET:
            field_dict["chore"] = chore
        if last_tracked is not UNSET:
            field_dict["last_tracked"] = last_tracked
        if track_count is not UNSET:
            field_dict["track_count"] = track_count
        if last_done_by is not UNSET:
            field_dict["last_done_by"] = last_done_by
        if next_estimated_execution_time is not UNSET:
            field_dict["next_estimated_execution_time"] = next_estimated_execution_time
        if next_execution_assigned_user is not UNSET:
            field_dict["next_execution_assigned_user"] = next_execution_assigned_user
        if average_execution_frequency_hours is not UNSET:
            field_dict["average_execution_frequency_hours"] = average_execution_frequency_hours

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chore import Chore
        from ..models.user_dto import UserDto

        d = src_dict.copy()
        _chore = d.pop("chore", UNSET)
        chore: Union[Unset, Chore]
        if isinstance(_chore, Unset):
            chore = UNSET
        else:
            chore = Chore.from_dict(_chore)

        _last_tracked = d.pop("last_tracked", UNSET)
        last_tracked: Union[Unset, datetime.datetime]
        if isinstance(_last_tracked, Unset):
            last_tracked = UNSET
        else:
            last_tracked = isoparse(_last_tracked)

        track_count = d.pop("track_count", UNSET)

        _last_done_by = d.pop("last_done_by", UNSET)
        last_done_by: Union[Unset, UserDto]
        if isinstance(_last_done_by, Unset):
            last_done_by = UNSET
        else:
            last_done_by = UserDto.from_dict(_last_done_by)

        _next_estimated_execution_time = d.pop("next_estimated_execution_time", UNSET)
        next_estimated_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_next_estimated_execution_time, Unset):
            next_estimated_execution_time = UNSET
        else:
            next_estimated_execution_time = isoparse(_next_estimated_execution_time)

        _next_execution_assigned_user = d.pop("next_execution_assigned_user", UNSET)
        next_execution_assigned_user: Union[Unset, UserDto]
        if isinstance(_next_execution_assigned_user, Unset):
            next_execution_assigned_user = UNSET
        else:
            next_execution_assigned_user = UserDto.from_dict(_next_execution_assigned_user)

        average_execution_frequency_hours = d.pop("average_execution_frequency_hours", UNSET)

        chore_details_response = cls(
            chore=chore,
            last_tracked=last_tracked,
            track_count=track_count,
            last_done_by=last_done_by,
            next_estimated_execution_time=next_estimated_execution_time,
            next_execution_assigned_user=next_execution_assigned_user,
            average_execution_frequency_hours=average_execution_frequency_hours,
        )

        chore_details_response.additional_properties = d
        return chore_details_response

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
