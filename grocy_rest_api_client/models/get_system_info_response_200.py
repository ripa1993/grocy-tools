from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_system_info_response_200_grocy_version import GetSystemInfoResponse200GrocyVersion


T = TypeVar("T", bound="GetSystemInfoResponse200")


@_attrs_define
class GetSystemInfoResponse200:
    """
    Attributes:
        grocy_version (Union[Unset, GetSystemInfoResponse200GrocyVersion]):
        php_version (Union[Unset, str]):
        sqlite_version (Union[Unset, str]):
    """

    grocy_version: Union[Unset, "GetSystemInfoResponse200GrocyVersion"] = UNSET
    php_version: Union[Unset, str] = UNSET
    sqlite_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grocy_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grocy_version, Unset):
            grocy_version = self.grocy_version.to_dict()

        php_version = self.php_version

        sqlite_version = self.sqlite_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grocy_version is not UNSET:
            field_dict["grocy_version"] = grocy_version
        if php_version is not UNSET:
            field_dict["php_version"] = php_version
        if sqlite_version is not UNSET:
            field_dict["sqlite_version"] = sqlite_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_system_info_response_200_grocy_version import GetSystemInfoResponse200GrocyVersion

        d = src_dict.copy()
        _grocy_version = d.pop("grocy_version", UNSET)
        grocy_version: Union[Unset, GetSystemInfoResponse200GrocyVersion]
        if isinstance(_grocy_version, Unset):
            grocy_version = UNSET
        else:
            grocy_version = GetSystemInfoResponse200GrocyVersion.from_dict(_grocy_version)

        php_version = d.pop("php_version", UNSET)

        sqlite_version = d.pop("sqlite_version", UNSET)

        get_system_info_response_200 = cls(
            grocy_version=grocy_version,
            php_version=php_version,
            sqlite_version=sqlite_version,
        )

        get_system_info_response_200.additional_properties = d
        return get_system_info_response_200

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
