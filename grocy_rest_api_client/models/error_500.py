from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_500_error_details import Error500ErrorDetails


T = TypeVar("T", bound="Error500")


@_attrs_define
class Error500:
    """
    Example:
        {'error_message': 'The error message...'}

    Attributes:
        error_message (Union[Unset, str]):
        error_details (Union[Unset, Error500ErrorDetails]):
    """

    error_message: Union[Unset, str] = UNSET
    error_details: Union[Unset, "Error500ErrorDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_message = self.error_message

        error_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error_details, Unset):
            error_details = self.error_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_details is not UNSET:
            field_dict["error_details"] = error_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_500_error_details import Error500ErrorDetails

        d = src_dict.copy()
        error_message = d.pop("error_message", UNSET)

        _error_details = d.pop("error_details", UNSET)
        error_details: Union[Unset, Error500ErrorDetails]
        if isinstance(_error_details, Unset):
            error_details = UNSET
        else:
            error_details = Error500ErrorDetails.from_dict(_error_details)

        error_500 = cls(
            error_message=error_message,
            error_details=error_details,
        )

        error_500.additional_properties = d
        return error_500

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
