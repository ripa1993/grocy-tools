import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="CurrentChoreResponse")


@_attrs_define
class CurrentChoreResponse:
    """
    Attributes:
        chore_id (Union[Unset, int]):
        chore_name (Union[Unset, str]):
        last_tracked_time (Union[Unset, datetime.datetime]):
        track_date_only (Union[Unset, bool]):
        next_estimated_execution_time (Union[Unset, datetime.datetime]): The next estimated execution time of this
            chore, 2999-12-31 23:59:59 when the given chore has a period_type of manually
        next_execution_assigned_to_user_id (Union[Unset, int]):
        is_rescheduled (Union[Unset, bool]):
        is_reassigned (Union[Unset, bool]):
        next_execution_assigned_user (Union[Unset, UserDto]): A user object without the *password* and with an
            additional *display_name* property
    """

    chore_id: Union[Unset, int] = UNSET
    chore_name: Union[Unset, str] = UNSET
    last_tracked_time: Union[Unset, datetime.datetime] = UNSET
    track_date_only: Union[Unset, bool] = UNSET
    next_estimated_execution_time: Union[Unset, datetime.datetime] = UNSET
    next_execution_assigned_to_user_id: Union[Unset, int] = UNSET
    is_rescheduled: Union[Unset, bool] = UNSET
    is_reassigned: Union[Unset, bool] = UNSET
    next_execution_assigned_user: Union[Unset, "UserDto"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chore_id = self.chore_id

        chore_name = self.chore_name

        last_tracked_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_tracked_time, Unset):
            last_tracked_time = self.last_tracked_time.isoformat()

        track_date_only = self.track_date_only

        next_estimated_execution_time: Union[Unset, str] = UNSET
        if not isinstance(self.next_estimated_execution_time, Unset):
            next_estimated_execution_time = self.next_estimated_execution_time.isoformat()

        next_execution_assigned_to_user_id = self.next_execution_assigned_to_user_id

        is_rescheduled = self.is_rescheduled

        is_reassigned = self.is_reassigned

        next_execution_assigned_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.next_execution_assigned_user, Unset):
            next_execution_assigned_user = self.next_execution_assigned_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chore_id is not UNSET:
            field_dict["chore_id"] = chore_id
        if chore_name is not UNSET:
            field_dict["chore_name"] = chore_name
        if last_tracked_time is not UNSET:
            field_dict["last_tracked_time"] = last_tracked_time
        if track_date_only is not UNSET:
            field_dict["track_date_only"] = track_date_only
        if next_estimated_execution_time is not UNSET:
            field_dict["next_estimated_execution_time"] = next_estimated_execution_time
        if next_execution_assigned_to_user_id is not UNSET:
            field_dict["next_execution_assigned_to_user_id"] = next_execution_assigned_to_user_id
        if is_rescheduled is not UNSET:
            field_dict["is_rescheduled"] = is_rescheduled
        if is_reassigned is not UNSET:
            field_dict["is_reassigned"] = is_reassigned
        if next_execution_assigned_user is not UNSET:
            field_dict["next_execution_assigned_user"] = next_execution_assigned_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_dto import UserDto

        d = src_dict.copy()
        chore_id = d.pop("chore_id", UNSET)

        chore_name = d.pop("chore_name", UNSET)

        _last_tracked_time = d.pop("last_tracked_time", UNSET)
        last_tracked_time: Union[Unset, datetime.datetime]
        if isinstance(_last_tracked_time, Unset):
            last_tracked_time = UNSET
        else:
            last_tracked_time = isoparse(_last_tracked_time)

        track_date_only = d.pop("track_date_only", UNSET)

        _next_estimated_execution_time = d.pop("next_estimated_execution_time", UNSET)
        next_estimated_execution_time: Union[Unset, datetime.datetime]
        if isinstance(_next_estimated_execution_time, Unset):
            next_estimated_execution_time = UNSET
        else:
            next_estimated_execution_time = isoparse(_next_estimated_execution_time)

        next_execution_assigned_to_user_id = d.pop("next_execution_assigned_to_user_id", UNSET)

        is_rescheduled = d.pop("is_rescheduled", UNSET)

        is_reassigned = d.pop("is_reassigned", UNSET)

        _next_execution_assigned_user = d.pop("next_execution_assigned_user", UNSET)
        next_execution_assigned_user: Union[Unset, UserDto]
        if isinstance(_next_execution_assigned_user, Unset):
            next_execution_assigned_user = UNSET
        else:
            next_execution_assigned_user = UserDto.from_dict(_next_execution_assigned_user)

        current_chore_response = cls(
            chore_id=chore_id,
            chore_name=chore_name,
            last_tracked_time=last_tracked_time,
            track_date_only=track_date_only,
            next_estimated_execution_time=next_estimated_execution_time,
            next_execution_assigned_to_user_id=next_execution_assigned_to_user_id,
            is_rescheduled=is_rescheduled,
            is_reassigned=is_reassigned,
            next_execution_assigned_user=next_execution_assigned_user,
        )

        current_chore_response.additional_properties = d
        return current_chore_response

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
