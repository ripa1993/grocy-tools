import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location import Location
    from ..models.product import Product
    from ..models.product_barcode import ProductBarcode
    from ..models.quantity_unit import QuantityUnit


T = TypeVar("T", bound="ProductDetailsResponse")


@_attrs_define
class ProductDetailsResponse:
    """
    Example:
        {'product': {'id': '1', 'name': 'Cookies', 'description': None, 'location_id': '4', 'qu_id_purchase': '3',
            'qu_id_stock': '3', 'min_stock_amount': '8', 'default_best_before_days': '0', 'row_created_timestamp':
            '2019-05-02 20:12:26', 'product_group_id': '1', 'picture_file_name': 'cookies.jpg',
            'default_best_before_days_after_open': '0', 'enable_tare_weight_handling': '0', 'tare_weight': '0.0',
            'not_check_stock_fulfillment_for_recipes': '0', 'last_shopping_location_id': None}, 'product_barcodes': [{'id':
            '1', 'product_id': '13', 'barcode': '01321230213', 'qu_id': '1', 'shopping_location_id': '2', 'amount': '10'}],
            'last_purchased': None, 'last_used': None, 'stock_amount': '2', 'stock_amount_opened': None,
            'default_quantity_unit_purchase': {'id': '3', 'name': 'Pack', 'description': None, 'row_created_timestamp':
            '2019-05-02 20:12:25', 'name_plural': 'Packs', 'plural_forms': None}, 'quantity_unit_stock': {'id': '3', 'name':
            'Pack', 'description': None, 'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural': 'Packs',
            'plural_forms': None}, 'quantity_unit_price': {'id': '3', 'name': 'Pack', 'description': None,
            'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural': 'Packs', 'plural_forms': None}, 'last_price':
            None, 'avg_price': None, 'current_price': None, 'last_shopping_location_id': None, 'next_due_date':
            '2019-07-07', 'location': {'id': '4', 'name': 'Candy cupboard', 'description': None, 'row_created_timestamp':
            '2019-05-02 20:12:25'}, 'average_shelf_life_days': -1, 'spoil_rate_percent': 0, 'default_consume_location':
            None}

    Attributes:
        product (Union[Unset, Product]):  Example: {'id': '1', 'name': 'Cookies', 'description': None, 'location_id':
            '4', 'qu_id_purchase': '3', 'qu_id_stock': '3', 'min_stock_amount': '8', 'default_best_before_days': '0',
            'row_created_timestamp': '2019-05-02 20:12:26', 'product_group_id': '1', 'picture_file_name': 'cookies.jpg',
            'default_best_before_days_after_open': '0', 'enable_tare_weight_handling': '0', 'tare_weight': '0.0',
            'not_check_stock_fulfillment_for_recipes': '0', 'shopping_location_id': None, 'userfields': None,
            'should_not_be_frozen': '1', 'default_consume_location_id': '5', 'move_on_open': '1'}.
        product_barcodes (Union[Unset, List['ProductBarcode']]):
        quantity_unit_stock (Union[Unset, QuantityUnit]):  Example: {'id': '2', 'name': 'Piece', 'description': None,
            'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural': 'Pieces', 'plural_forms': None, 'userfields':
            None}.
        default_quantity_unit_purchase (Union[Unset, QuantityUnit]):  Example: {'id': '2', 'name': 'Piece',
            'description': None, 'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural': 'Pieces', 'plural_forms':
            None, 'userfields': None}.
        default_quantity_unit_consume (Union[Unset, QuantityUnit]):  Example: {'id': '2', 'name': 'Piece',
            'description': None, 'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural': 'Pieces', 'plural_forms':
            None, 'userfields': None}.
        quantity_unit_price (Union[Unset, QuantityUnit]):  Example: {'id': '2', 'name': 'Piece', 'description': None,
            'row_created_timestamp': '2019-05-02 20:12:25', 'name_plural': 'Pieces', 'plural_forms': None, 'userfields':
            None}.
        last_purchased (Union[Unset, datetime.date]):
        last_used (Union[Unset, datetime.date]):
        stock_amount (Union[Unset, float]):
        stock_amount_opened (Union[Unset, float]):
        next_due_date (Union[Unset, datetime.date]):
        last_price (Union[Unset, float]): The price of the last purchase of the corresponding product
        avg_price (Union[Unset, float]): The average price af all stock entries currently in stock of the corresponding
            product
        current_price (Union[Unset, float]): The current price of the corresponding product, based on the stock entry to
            use next (defined by the default consume rule "Opened first, then first due first, then first in first out") or
            on the last price if the product is currently not in stock
        oldest_price (Union[Unset, float]): This field is deprecated and will be removed in a future version (currently
            returns the same as `current_price`)
        last_shopping_location_id (Union[Unset, int]):
        location (Union[Unset, Location]):  Example: {'id': '2', 'name': '0', 'description': None,
            'row_created_timestamp': '2019-05-02 20:12:25', 'userfields': None}.
        average_shelf_life_days (Union[Unset, float]):
        spoil_rate_percent (Union[Unset, float]):
        has_childs (Union[Unset, bool]): True when the product is a parent product of others
        default_location (Union[Unset, Location]):  Example: {'id': '2', 'name': '0', 'description': None,
            'row_created_timestamp': '2019-05-02 20:12:25', 'userfields': None}.
        qu_conversion_factor_purchase_to_stock (Union[Unset, float]): The conversion factor of the corresponding QU
            conversion from the product's qu_id_purchase to qu_id_stock
        qu_conversion_factor_price_to_stock (Union[Unset, float]): The conversion factor of the corresponding QU
            conversion from the product's qu_id_price to qu_id_stock
    """

    product: Union[Unset, "Product"] = UNSET
    product_barcodes: Union[Unset, List["ProductBarcode"]] = UNSET
    quantity_unit_stock: Union[Unset, "QuantityUnit"] = UNSET
    default_quantity_unit_purchase: Union[Unset, "QuantityUnit"] = UNSET
    default_quantity_unit_consume: Union[Unset, "QuantityUnit"] = UNSET
    quantity_unit_price: Union[Unset, "QuantityUnit"] = UNSET
    last_purchased: Union[Unset, datetime.date] = UNSET
    last_used: Union[Unset, datetime.date] = UNSET
    stock_amount: Union[Unset, float] = UNSET
    stock_amount_opened: Union[Unset, float] = UNSET
    next_due_date: Union[Unset, datetime.date] = UNSET
    last_price: Union[Unset, float] = UNSET
    avg_price: Union[Unset, float] = UNSET
    current_price: Union[Unset, float] = UNSET
    oldest_price: Union[Unset, float] = UNSET
    last_shopping_location_id: Union[Unset, int] = UNSET
    location: Union[Unset, "Location"] = UNSET
    average_shelf_life_days: Union[Unset, float] = UNSET
    spoil_rate_percent: Union[Unset, float] = UNSET
    has_childs: Union[Unset, bool] = UNSET
    default_location: Union[Unset, "Location"] = UNSET
    qu_conversion_factor_purchase_to_stock: Union[Unset, float] = UNSET
    qu_conversion_factor_price_to_stock: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        product_barcodes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_barcodes, Unset):
            product_barcodes = []
            for product_barcodes_item_data in self.product_barcodes:
                product_barcodes_item = product_barcodes_item_data.to_dict()
                product_barcodes.append(product_barcodes_item)

        quantity_unit_stock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quantity_unit_stock, Unset):
            quantity_unit_stock = self.quantity_unit_stock.to_dict()

        default_quantity_unit_purchase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_quantity_unit_purchase, Unset):
            default_quantity_unit_purchase = self.default_quantity_unit_purchase.to_dict()

        default_quantity_unit_consume: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_quantity_unit_consume, Unset):
            default_quantity_unit_consume = self.default_quantity_unit_consume.to_dict()

        quantity_unit_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.quantity_unit_price, Unset):
            quantity_unit_price = self.quantity_unit_price.to_dict()

        last_purchased: Union[Unset, str] = UNSET
        if not isinstance(self.last_purchased, Unset):
            last_purchased = self.last_purchased.isoformat()

        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        stock_amount = self.stock_amount

        stock_amount_opened = self.stock_amount_opened

        next_due_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_due_date, Unset):
            next_due_date = self.next_due_date.isoformat()

        last_price = self.last_price

        avg_price = self.avg_price

        current_price = self.current_price

        oldest_price = self.oldest_price

        last_shopping_location_id = self.last_shopping_location_id

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        average_shelf_life_days = self.average_shelf_life_days

        spoil_rate_percent = self.spoil_rate_percent

        has_childs = self.has_childs

        default_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_location, Unset):
            default_location = self.default_location.to_dict()

        qu_conversion_factor_purchase_to_stock = self.qu_conversion_factor_purchase_to_stock

        qu_conversion_factor_price_to_stock = self.qu_conversion_factor_price_to_stock

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if product_barcodes is not UNSET:
            field_dict["product_barcodes"] = product_barcodes
        if quantity_unit_stock is not UNSET:
            field_dict["quantity_unit_stock"] = quantity_unit_stock
        if default_quantity_unit_purchase is not UNSET:
            field_dict["default_quantity_unit_purchase"] = default_quantity_unit_purchase
        if default_quantity_unit_consume is not UNSET:
            field_dict["default_quantity_unit_consume"] = default_quantity_unit_consume
        if quantity_unit_price is not UNSET:
            field_dict["quantity_unit_price"] = quantity_unit_price
        if last_purchased is not UNSET:
            field_dict["last_purchased"] = last_purchased
        if last_used is not UNSET:
            field_dict["last_used"] = last_used
        if stock_amount is not UNSET:
            field_dict["stock_amount"] = stock_amount
        if stock_amount_opened is not UNSET:
            field_dict["stock_amount_opened"] = stock_amount_opened
        if next_due_date is not UNSET:
            field_dict["next_due_date"] = next_due_date
        if last_price is not UNSET:
            field_dict["last_price"] = last_price
        if avg_price is not UNSET:
            field_dict["avg_price"] = avg_price
        if current_price is not UNSET:
            field_dict["current_price"] = current_price
        if oldest_price is not UNSET:
            field_dict["oldest_price"] = oldest_price
        if last_shopping_location_id is not UNSET:
            field_dict["last_shopping_location_id"] = last_shopping_location_id
        if location is not UNSET:
            field_dict["location"] = location
        if average_shelf_life_days is not UNSET:
            field_dict["average_shelf_life_days"] = average_shelf_life_days
        if spoil_rate_percent is not UNSET:
            field_dict["spoil_rate_percent"] = spoil_rate_percent
        if has_childs is not UNSET:
            field_dict["has_childs"] = has_childs
        if default_location is not UNSET:
            field_dict["default_location"] = default_location
        if qu_conversion_factor_purchase_to_stock is not UNSET:
            field_dict["qu_conversion_factor_purchase_to_stock"] = qu_conversion_factor_purchase_to_stock
        if qu_conversion_factor_price_to_stock is not UNSET:
            field_dict["qu_conversion_factor_price_to_stock"] = qu_conversion_factor_price_to_stock

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location import Location
        from ..models.product import Product
        from ..models.product_barcode import ProductBarcode
        from ..models.quantity_unit import QuantityUnit

        d = src_dict.copy()
        _product = d.pop("product", UNSET)
        product: Union[Unset, Product]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = Product.from_dict(_product)

        product_barcodes = []
        _product_barcodes = d.pop("product_barcodes", UNSET)
        for product_barcodes_item_data in _product_barcodes or []:
            product_barcodes_item = ProductBarcode.from_dict(product_barcodes_item_data)

            product_barcodes.append(product_barcodes_item)

        _quantity_unit_stock = d.pop("quantity_unit_stock", UNSET)
        quantity_unit_stock: Union[Unset, QuantityUnit]
        if isinstance(_quantity_unit_stock, Unset):
            quantity_unit_stock = UNSET
        else:
            quantity_unit_stock = QuantityUnit.from_dict(_quantity_unit_stock)

        _default_quantity_unit_purchase = d.pop("default_quantity_unit_purchase", UNSET)
        default_quantity_unit_purchase: Union[Unset, QuantityUnit]
        if isinstance(_default_quantity_unit_purchase, Unset):
            default_quantity_unit_purchase = UNSET
        else:
            default_quantity_unit_purchase = QuantityUnit.from_dict(_default_quantity_unit_purchase)

        _default_quantity_unit_consume = d.pop("default_quantity_unit_consume", UNSET)
        default_quantity_unit_consume: Union[Unset, QuantityUnit]
        if isinstance(_default_quantity_unit_consume, Unset):
            default_quantity_unit_consume = UNSET
        else:
            default_quantity_unit_consume = QuantityUnit.from_dict(_default_quantity_unit_consume)

        _quantity_unit_price = d.pop("quantity_unit_price", UNSET)
        quantity_unit_price: Union[Unset, QuantityUnit]
        if isinstance(_quantity_unit_price, Unset):
            quantity_unit_price = UNSET
        else:
            quantity_unit_price = QuantityUnit.from_dict(_quantity_unit_price)

        _last_purchased = d.pop("last_purchased", UNSET)
        last_purchased: Union[Unset, datetime.date]
        if isinstance(_last_purchased, Unset) or _last_purchased is None:
            last_purchased = UNSET
        else:
            last_purchased = isoparse(_last_purchased).date()

        _last_used = d.pop("last_used", UNSET)
        last_used: Union[Unset, datetime.date]
        if isinstance(_last_used, Unset) or _last_used is None:
            last_used = UNSET
        else:
            last_used = isoparse(_last_used).date()

        stock_amount = d.pop("stock_amount", UNSET)

        stock_amount_opened = d.pop("stock_amount_opened", UNSET)

        _next_due_date = d.pop("next_due_date", UNSET)
        next_due_date: Union[Unset, datetime.date]
        if isinstance(_next_due_date, Unset) or _next_due_date is None:
            next_due_date = UNSET
        else:
            next_due_date = isoparse(_next_due_date).date()

        last_price = d.pop("last_price", UNSET)

        avg_price = d.pop("avg_price", UNSET)

        current_price = d.pop("current_price", UNSET)

        oldest_price = d.pop("oldest_price", UNSET)

        last_shopping_location_id = d.pop("last_shopping_location_id", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, Location]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Location.from_dict(_location)

        average_shelf_life_days = d.pop("average_shelf_life_days", UNSET)

        spoil_rate_percent = d.pop("spoil_rate_percent", UNSET)

        has_childs = d.pop("has_childs", UNSET)

        _default_location = d.pop("default_location", UNSET)
        default_location: Union[Unset, Location]
        if isinstance(_default_location, Unset):
            default_location = UNSET
        else:
            default_location = Location.from_dict(_default_location)

        qu_conversion_factor_purchase_to_stock = d.pop("qu_conversion_factor_purchase_to_stock", UNSET)

        qu_conversion_factor_price_to_stock = d.pop("qu_conversion_factor_price_to_stock", UNSET)

        product_details_response = cls(
            product=product,
            product_barcodes=product_barcodes,
            quantity_unit_stock=quantity_unit_stock,
            default_quantity_unit_purchase=default_quantity_unit_purchase,
            default_quantity_unit_consume=default_quantity_unit_consume,
            quantity_unit_price=quantity_unit_price,
            last_purchased=last_purchased,
            last_used=last_used,
            stock_amount=stock_amount,
            stock_amount_opened=stock_amount_opened,
            next_due_date=next_due_date,
            last_price=last_price,
            avg_price=avg_price,
            current_price=current_price,
            oldest_price=oldest_price,
            last_shopping_location_id=last_shopping_location_id,
            location=location,
            average_shelf_life_days=average_shelf_life_days,
            spoil_rate_percent=spoil_rate_percent,
            has_childs=has_childs,
            default_location=default_location,
            qu_conversion_factor_purchase_to_stock=qu_conversion_factor_purchase_to_stock,
            qu_conversion_factor_price_to_stock=qu_conversion_factor_price_to_stock,
        )

        product_details_response.additional_properties = d
        return product_details_response

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
