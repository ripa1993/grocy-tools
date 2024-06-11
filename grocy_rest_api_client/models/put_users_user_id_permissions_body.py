from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutUsersUserIdPermissionsBody")


@_attrs_define
class PutUsersUserIdPermissionsBody:
    """
    Attributes:
        permissions (Union[Unset, List[int]]): A list of permission ids
    """

    permissions: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permissions: Union[Unset, List[int]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permissions = cast(List[int], d.pop("permissions", UNSET))

        put_users_user_id_permissions_body = cls(
            permissions=permissions,
        )

        put_users_user_id_permissions_body.additional_properties = d
        return put_users_user_id_permissions_body

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
