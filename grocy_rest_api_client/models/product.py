import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_userfields import ProductUserfields


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Example:
        {'id': '1', 'name': 'Cookies', 'description': None, 'location_id': '4', 'qu_id_purchase': '3', 'qu_id_stock':
            '3', 'min_stock_amount': '8', 'default_best_before_days': '0', 'row_created_timestamp': '2019-05-02 20:12:26',
            'product_group_id': '1', 'picture_file_name': 'cookies.jpg', 'default_best_before_days_after_open': '0',
            'enable_tare_weight_handling': '0', 'tare_weight': '0.0', 'not_check_stock_fulfillment_for_recipes': '0',
            'shopping_location_id': None, 'userfields': None, 'should_not_be_frozen': '1', 'default_consume_location_id':
            '5', 'move_on_open': '1'}

    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        location_id (Union[Unset, int]):
        qu_id_purchase (Union[Unset, int]):
        qu_id_stock (Union[Unset, int]):
        enable_tare_weight_handling (Union[Unset, int]):
        not_check_stock_fulfillment_for_recipes (Union[Unset, int]):
        product_group_id (Union[Unset, int]):
        tare_weight (Union[Unset, float]):
        min_stock_amount (Union[Unset, float]):  Default: 0.0.
        default_best_before_days (Union[Unset, int]):  Default: 0.
        default_best_before_days_after_open (Union[Unset, int]):  Default: 0.
        picture_file_name (Union[Unset, str]):
        row_created_timestamp (Union[Unset, datetime.datetime]):
        shopping_location_id (Union[Unset, int]):
        treat_opened_as_out_of_stock (Union[Unset, int]):
        auto_reprint_stock_label (Union[Unset, int]):
        no_own_stock (Union[Unset, int]):
        userfields (Union[Unset, ProductUserfields]): Key/value pairs of userfields
        should_not_be_frozen (Union[Unset, int]):
        default_consume_location_id (Union[Unset, int]):
        move_on_open (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    location_id: Union[Unset, int] = UNSET
    qu_id_purchase: Union[Unset, int] = UNSET
    qu_id_stock: Union[Unset, int] = UNSET
    enable_tare_weight_handling: Union[Unset, int] = UNSET
    not_check_stock_fulfillment_for_recipes: Union[Unset, int] = UNSET
    product_group_id: Union[Unset, int] = UNSET
    tare_weight: Union[Unset, float] = UNSET
    min_stock_amount: Union[Unset, float] = 0.0
    default_best_before_days: Union[Unset, int] = 0
    default_best_before_days_after_open: Union[Unset, int] = 0
    picture_file_name: Union[Unset, str] = UNSET
    row_created_timestamp: Union[Unset, datetime.datetime] = UNSET
    shopping_location_id: Union[Unset, int] = UNSET
    treat_opened_as_out_of_stock: Union[Unset, int] = UNSET
    auto_reprint_stock_label: Union[Unset, int] = UNSET
    no_own_stock: Union[Unset, int] = UNSET
    userfields: Union[Unset, "ProductUserfields"] = UNSET
    should_not_be_frozen: Union[Unset, int] = UNSET
    default_consume_location_id: Union[Unset, int] = UNSET
    move_on_open: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        location_id = self.location_id

        qu_id_purchase = self.qu_id_purchase

        qu_id_stock = self.qu_id_stock

        enable_tare_weight_handling = self.enable_tare_weight_handling

        not_check_stock_fulfillment_for_recipes = self.not_check_stock_fulfillment_for_recipes

        product_group_id = self.product_group_id

        tare_weight = self.tare_weight

        min_stock_amount = self.min_stock_amount

        default_best_before_days = self.default_best_before_days

        default_best_before_days_after_open = self.default_best_before_days_after_open

        picture_file_name = self.picture_file_name

        row_created_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.row_created_timestamp, Unset):
            row_created_timestamp = self.row_created_timestamp.isoformat()

        shopping_location_id = self.shopping_location_id

        treat_opened_as_out_of_stock = self.treat_opened_as_out_of_stock

        auto_reprint_stock_label = self.auto_reprint_stock_label

        no_own_stock = self.no_own_stock

        userfields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.userfields, Unset):
            userfields = self.userfields.to_dict()

        should_not_be_frozen = self.should_not_be_frozen

        default_consume_location_id = self.default_consume_location_id

        move_on_open = self.move_on_open

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if qu_id_purchase is not UNSET:
            field_dict["qu_id_purchase"] = qu_id_purchase
        if qu_id_stock is not UNSET:
            field_dict["qu_id_stock"] = qu_id_stock
        if enable_tare_weight_handling is not UNSET:
            field_dict["enable_tare_weight_handling"] = enable_tare_weight_handling
        if not_check_stock_fulfillment_for_recipes is not UNSET:
            field_dict["not_check_stock_fulfillment_for_recipes"] = not_check_stock_fulfillment_for_recipes
        if product_group_id is not UNSET:
            field_dict["product_group_id"] = product_group_id
        if tare_weight is not UNSET:
            field_dict["tare_weight"] = tare_weight
        if min_stock_amount is not UNSET:
            field_dict["min_stock_amount"] = min_stock_amount
        if default_best_before_days is not UNSET:
            field_dict["default_best_before_days"] = default_best_before_days
        if default_best_before_days_after_open is not UNSET:
            field_dict["default_best_before_days_after_open"] = default_best_before_days_after_open
        if picture_file_name is not UNSET:
            field_dict["picture_file_name"] = picture_file_name
        if row_created_timestamp is not UNSET:
            field_dict["row_created_timestamp"] = row_created_timestamp
        if shopping_location_id is not UNSET:
            field_dict["shopping_location_id"] = shopping_location_id
        if treat_opened_as_out_of_stock is not UNSET:
            field_dict["treat_opened_as_out_of_stock"] = treat_opened_as_out_of_stock
        if auto_reprint_stock_label is not UNSET:
            field_dict["auto_reprint_stock_label"] = auto_reprint_stock_label
        if no_own_stock is not UNSET:
            field_dict["no_own_stock"] = no_own_stock
        if userfields is not UNSET:
            field_dict["userfields"] = userfields
        if should_not_be_frozen is not UNSET:
            field_dict["should_not_be_frozen"] = should_not_be_frozen
        if default_consume_location_id is not UNSET:
            field_dict["default_consume_location_id"] = default_consume_location_id
        if move_on_open is not UNSET:
            field_dict["move_on_open"] = move_on_open

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_userfields import ProductUserfields

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        location_id = d.pop("location_id", UNSET)

        qu_id_purchase = d.pop("qu_id_purchase", UNSET)

        qu_id_stock = d.pop("qu_id_stock", UNSET)

        enable_tare_weight_handling = d.pop("enable_tare_weight_handling", UNSET)

        not_check_stock_fulfillment_for_recipes = d.pop("not_check_stock_fulfillment_for_recipes", UNSET)

        product_group_id = d.pop("product_group_id", UNSET)

        tare_weight = d.pop("tare_weight", UNSET)

        min_stock_amount = d.pop("min_stock_amount", UNSET)

        default_best_before_days = d.pop("default_best_before_days", UNSET)

        default_best_before_days_after_open = d.pop("default_best_before_days_after_open", UNSET)

        picture_file_name = d.pop("picture_file_name", UNSET)

        _row_created_timestamp = d.pop("row_created_timestamp", UNSET)
        row_created_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_row_created_timestamp, Unset):
            row_created_timestamp = UNSET
        else:
            row_created_timestamp = isoparse(_row_created_timestamp)

        shopping_location_id = d.pop("shopping_location_id", UNSET)

        treat_opened_as_out_of_stock = d.pop("treat_opened_as_out_of_stock", UNSET)

        auto_reprint_stock_label = d.pop("auto_reprint_stock_label", UNSET)

        no_own_stock = d.pop("no_own_stock", UNSET)

        _userfields = d.pop("userfields", UNSET)
        userfields: Union[Unset, ProductUserfields]
        if isinstance(_userfields, Unset):
            userfields = UNSET
        else:
            userfields = ProductUserfields.from_dict(_userfields)

        should_not_be_frozen = d.pop("should_not_be_frozen", UNSET)

        default_consume_location_id = d.pop("default_consume_location_id", UNSET)

        move_on_open = d.pop("move_on_open", UNSET)

        product = cls(
            id=id,
            name=name,
            description=description,
            location_id=location_id,
            qu_id_purchase=qu_id_purchase,
            qu_id_stock=qu_id_stock,
            enable_tare_weight_handling=enable_tare_weight_handling,
            not_check_stock_fulfillment_for_recipes=not_check_stock_fulfillment_for_recipes,
            product_group_id=product_group_id,
            tare_weight=tare_weight,
            min_stock_amount=min_stock_amount,
            default_best_before_days=default_best_before_days,
            default_best_before_days_after_open=default_best_before_days_after_open,
            picture_file_name=picture_file_name,
            row_created_timestamp=row_created_timestamp,
            shopping_location_id=shopping_location_id,
            treat_opened_as_out_of_stock=treat_opened_as_out_of_stock,
            auto_reprint_stock_label=auto_reprint_stock_label,
            no_own_stock=no_own_stock,
            userfields=userfields,
            should_not_be_frozen=should_not_be_frozen,
            default_consume_location_id=default_consume_location_id,
            move_on_open=move_on_open,
        )

        product.additional_properties = d
        return product

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
