from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRecipesRecipeIdAddNotFulfilledProductsToShoppinglistBody")


@_attrs_define
class PostRecipesRecipeIdAddNotFulfilledProductsToShoppinglistBody:
    """
    Attributes:
        excluded_product_ids (Union[Unset, List[int]]): An optional array of product ids to exclude them from being put
            on the shopping list
    """

    excluded_product_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        excluded_product_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.excluded_product_ids, Unset):
            excluded_product_ids = self.excluded_product_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excluded_product_ids is not UNSET:
            field_dict["excludedProductIds"] = excluded_product_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        excluded_product_ids = cast(List[int], d.pop("excludedProductIds", UNSET))

        post_recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_body = cls(
            excluded_product_ids=excluded_product_ids,
        )

        post_recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_body.additional_properties = d
        return post_recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_body

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
