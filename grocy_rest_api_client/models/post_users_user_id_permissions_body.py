from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersUserIdPermissionsBody")


@_attrs_define
class PostUsersUserIdPermissionsBody:
    """
    Attributes:
        permissions_id (Union[Unset, int]): A permission ids
    """

    permissions_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permissions_id = self.permissions_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions_id is not UNSET:
            field_dict["permissions_id"] = permissions_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permissions_id = d.pop("permissions_id", UNSET)

        post_users_user_id_permissions_body = cls(
            permissions_id=permissions_id,
        )

        post_users_user_id_permissions_body.additional_properties = d
        return post_users_user_id_permissions_body

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
