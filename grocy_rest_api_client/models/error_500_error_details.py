from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Error500ErrorDetails")


@_attrs_define
class Error500ErrorDetails:
    """
    Attributes:
        stack_trace (Union[Unset, str]):
        file (Union[Unset, str]):
        line (Union[Unset, int]):
    """

    stack_trace: Union[Unset, str] = UNSET
    file: Union[Unset, str] = UNSET
    line: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stack_trace = self.stack_trace

        file = self.file

        line = self.line

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_trace is not UNSET:
            field_dict["stack_trace"] = stack_trace
        if file is not UNSET:
            field_dict["file"] = file
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stack_trace = d.pop("stack_trace", UNSET)

        file = d.pop("file", UNSET)

        line = d.pop("line", UNSET)

        error_500_error_details = cls(
            stack_trace=stack_trace,
            file=file,
            line=line,
        )

        error_500_error_details.additional_properties = d
        return error_500_error_details

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
