from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChoresExecutionsCalculateNextAssignmentsBody")


@_attrs_define
class PostChoresExecutionsCalculateNextAssignmentsBody:
    """
    Example:
        {'chore_id': 1}

    Attributes:
        chore_id (Union[Unset, int]): The chore id of the chore which next user assignment should be (re)calculated,
            when omitted, the next user assignments of all chores will (re)caluclated
    """

    chore_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chore_id = self.chore_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chore_id is not UNSET:
            field_dict["chore_id"] = chore_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chore_id = d.pop("chore_id", UNSET)

        post_chores_executions_calculate_next_assignments_body = cls(
            chore_id=chore_id,
        )

        post_chores_executions_calculate_next_assignments_body.additional_properties = d
        return post_chores_executions_calculate_next_assignments_body

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
