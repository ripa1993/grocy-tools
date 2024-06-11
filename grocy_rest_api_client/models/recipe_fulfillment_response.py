from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecipeFulfillmentResponse")


@_attrs_define
class RecipeFulfillmentResponse:
    """
    Example:
        {'recipe_id': '1', 'need_fulfilled': '0', 'need_fulfilled_with_shopping_list': '0', 'missing_products_count':
            '2', 'costs': '17.74'}

    Attributes:
        recipe_id (Union[Unset, int]):
        need_fulfilled (Union[Unset, bool]):
        need_fulfilled_with_shopping_list (Union[Unset, bool]):
        missing_products_count (Union[Unset, int]):
        costs (Union[Unset, float]):
    """

    recipe_id: Union[Unset, int] = UNSET
    need_fulfilled: Union[Unset, bool] = UNSET
    need_fulfilled_with_shopping_list: Union[Unset, bool] = UNSET
    missing_products_count: Union[Unset, int] = UNSET
    costs: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recipe_id = self.recipe_id

        need_fulfilled = self.need_fulfilled

        need_fulfilled_with_shopping_list = self.need_fulfilled_with_shopping_list

        missing_products_count = self.missing_products_count

        costs = self.costs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recipe_id is not UNSET:
            field_dict["recipe_id"] = recipe_id
        if need_fulfilled is not UNSET:
            field_dict["need_fulfilled"] = need_fulfilled
        if need_fulfilled_with_shopping_list is not UNSET:
            field_dict["need_fulfilled_with_shopping_list"] = need_fulfilled_with_shopping_list
        if missing_products_count is not UNSET:
            field_dict["missing_products_count"] = missing_products_count
        if costs is not UNSET:
            field_dict["costs"] = costs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recipe_id = d.pop("recipe_id", UNSET)

        need_fulfilled = d.pop("need_fulfilled", UNSET)

        need_fulfilled_with_shopping_list = d.pop("need_fulfilled_with_shopping_list", UNSET)

        missing_products_count = d.pop("missing_products_count", UNSET)

        costs = d.pop("costs", UNSET)

        recipe_fulfillment_response = cls(
            recipe_id=recipe_id,
            need_fulfilled=need_fulfilled,
            need_fulfilled_with_shopping_list=need_fulfilled_with_shopping_list,
            missing_products_count=missing_products_count,
            costs=costs,
        )

        recipe_fulfillment_response.additional_properties = d
        return recipe_fulfillment_response

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
