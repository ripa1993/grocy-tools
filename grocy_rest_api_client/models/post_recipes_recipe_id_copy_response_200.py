from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRecipesRecipeIdCopyResponse200")


@_attrs_define
class PostRecipesRecipeIdCopyResponse200:
    """
    Attributes:
        created_object_id (Union[Unset, int]): The id of the created recipe
    """

    created_object_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_object_id = self.created_object_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_object_id is not UNSET:
            field_dict["created_object_id"] = created_object_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_object_id = d.pop("created_object_id", UNSET)

        post_recipes_recipe_id_copy_response_200 = cls(
            created_object_id=created_object_id,
        )

        post_recipes_recipe_id_copy_response_200.additional_properties = d
        return post_recipes_recipe_id_copy_response_200

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
