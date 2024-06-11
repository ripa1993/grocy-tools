from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUsersUserIdPermissionsResponse200Item")


@_attrs_define
class GetUsersUserIdPermissionsResponse200Item:
    """
    Attributes:
        permission_id (Union[Unset, int]):
        user_id (Union[Unset, int]):
    """

    permission_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permission_id = self.permission_id

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission_id is not UNSET:
            field_dict["permission_id"] = permission_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        permission_id = d.pop("permission_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        get_users_user_id_permissions_response_200_item = cls(
            permission_id=permission_id,
            user_id=user_id,
        )

        get_users_user_id_permissions_response_200_item.additional_properties = d
        return get_users_user_id_permissions_response_200_item

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
