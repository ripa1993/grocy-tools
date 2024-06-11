import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.task_category import TaskCategory
    from ..models.user_dto import UserDto


T = TypeVar("T", bound="CurrentTaskResponse")


@_attrs_define
class CurrentTaskResponse:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        done (Union[Unset, int]):
        done_timestamp (Union[Unset, datetime.datetime]):
        category_id (Union[Unset, int]):
        assigned_to_user_id (Union[Unset, int]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
        assigned_to_user (Union[Unset, UserDto]): A user object without the *password* and with an additional
            *display_name* property
        category (Union[Unset, TaskCategory]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    done: Union[Unset, int] = UNSET
    done_timestamp: Union[Unset, datetime.datetime] = UNSET
    category_id: Union[Unset, int] = UNSET
    assigned_to_user_id: Union[Unset, int] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    assigned_to_user: Union[Unset, "UserDto"] = UNSET
    category: Union[Unset, "TaskCategory"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        done = self.done

        done_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.done_timestamp, Unset):
            done_timestamp = self.done_timestamp.isoformat()

        category_id = self.category_id

        assigned_to_user_id = self.assigned_to_user_id

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        assigned_to_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assigned_to_user, Unset):
            assigned_to_user = self.assigned_to_user.to_dict()

        category: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if done is not UNSET:
            field_dict["done"] = done
        if done_timestamp is not UNSET:
            field_dict["done_timestamp"] = done_timestamp
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if assigned_to_user is not UNSET:
            field_dict["assigned_to_user"] = assigned_to_user
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.task_category import TaskCategory
        from ..models.user_dto import UserDto

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        done = d.pop("done", UNSET)

        _done_timestamp = d.pop("done_timestamp", UNSET)
        done_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_done_timestamp, Unset):
            done_timestamp = UNSET
        else:
            done_timestamp = isoparse(_done_timestamp)

        category_id = d.pop("category_id", UNSET)

        assigned_to_user_id = d.pop("assigned_to_user_id", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        _assigned_to_user = d.pop("assigned_to_user", UNSET)
        assigned_to_user: Union[Unset, UserDto]
        if isinstance(_assigned_to_user, Unset):
            assigned_to_user = UNSET
        else:
            assigned_to_user = UserDto.from_dict(_assigned_to_user)

        _category = d.pop("category", UNSET)
        category: Union[Unset, TaskCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = TaskCategory.from_dict(_category)

        current_task_response = cls(
            id=id,
            name=name,
            description=description,
            due_date=due_date,
            done=done,
            done_timestamp=done_timestamp,
            category_id=category_id,
            assigned_to_user_id=assigned_to_user_id,
            row_created_timestamp=row_created_timestamp,
            assigned_to_user=assigned_to_user,
            category=category,
        )

        current_task_response.additional_properties = d
        return current_task_response

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
