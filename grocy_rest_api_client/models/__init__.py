"""Contains all the data models used in inputs/outputs"""

from .api_key import ApiKey
from .battery import Battery
from .battery_charge_cycle_entry import BatteryChargeCycleEntry
from .battery_details_response import BatteryDetailsResponse
from .battery_userfields import BatteryUserfields
from .chore import Chore
from .chore_assignment_type import ChoreAssignmentType
from .chore_details_response import ChoreDetailsResponse
from .chore_log_entry import ChoreLogEntry
from .chore_period_type import ChorePeriodType
from .chore_userfields import ChoreUserfields
from .current_battery_response import CurrentBatteryResponse
from .current_chore_response import CurrentChoreResponse
from .current_stock_response import CurrentStockResponse
from .current_task_response import CurrentTaskResponse
from .current_volatil_stock_response import CurrentVolatilStockResponse
from .current_volatil_stock_response_missing_products_item import CurrentVolatilStockResponseMissingProductsItem
from .db_changed_time_response import DbChangedTimeResponse
from .error_400 import Error400
from .error_500 import Error500
from .error_500_error_details import Error500ErrorDetails
from .exposed_entity import ExposedEntity
from .exposed_entity_edit_requires_admin import ExposedEntityEditRequiresAdmin
from .exposed_entity_including_user_entities import ExposedEntityIncludingUserEntities
from .exposed_entity_including_user_entities_not_including_not_editable import (
    ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
)
from .exposed_entity_no_delete import ExposedEntityNoDelete
from .exposed_entity_no_edit import ExposedEntityNoEdit
from .exposed_entity_no_listing import ExposedEntityNoListing
from .exposed_entity_not_including_not_deletable import ExposedEntityNotIncludingNotDeletable
from .exposed_entity_not_including_not_editable import ExposedEntityNotIncludingNotEditable
from .exposed_entity_not_including_not_listable import ExposedEntityNotIncludingNotListable
from .external_barcode_lookup_response import ExternalBarcodeLookupResponse
from .file_groups import FileGroups
from .get_batteries_battery_id_printlabel_response_200 import GetBatteriesBatteryIdPrintlabelResponse200
from .get_calendar_ical_sharing_link_response_200 import GetCalendarIcalSharingLinkResponse200
from .get_chores_chore_id_printlabel_response_200 import GetChoresChoreIdPrintlabelResponse200
from .get_files_group_file_name_force_serve_as import GetFilesGroupFileNameForceServeAs
from .get_print_shoppinglist_thermal_response_200 import GetPrintShoppinglistThermalResponse200
from .get_recipes_recipe_id_printlabel_response_200 import GetRecipesRecipeIdPrintlabelResponse200
from .get_stock_entry_entry_id_printlabel_response_200 import GetStockEntryEntryIdPrintlabelResponse200
from .get_stock_products_product_id_printlabel_response_200 import GetStockProductsProductIdPrintlabelResponse200
from .get_system_config_response_200 import GetSystemConfigResponse200
from .get_system_info_response_200 import GetSystemInfoResponse200
from .get_system_info_response_200_grocy_version import GetSystemInfoResponse200GrocyVersion
from .get_system_localization_strings_response_200 import GetSystemLocalizationStringsResponse200
from .get_user_response_200 import GetUserResponse200
from .get_user_settings_response_200 import GetUserSettingsResponse200
from .get_userfields_entity_object_id_response_200 import GetUserfieldsEntityObjectIdResponse200
from .get_users_user_id_permissions_response_200_item import GetUsersUserIdPermissionsResponse200Item
from .location import Location
from .location_userfields import LocationUserfields
from .missing_localization_request import MissingLocalizationRequest
from .post_batteries_battery_id_charge_body import PostBatteriesBatteryIdChargeBody
from .post_chores_chore_id_execute_body import PostChoresChoreIdExecuteBody
from .post_chores_executions_calculate_next_assignments_body import PostChoresExecutionsCalculateNextAssignmentsBody
from .post_objects_entity_response_200 import PostObjectsEntityResponse200
from .post_recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_body import (
    PostRecipesRecipeIdAddNotFulfilledProductsToShoppinglistBody,
)
from .post_recipes_recipe_id_copy_response_200 import PostRecipesRecipeIdCopyResponse200
from .post_stock_products_by_barcode_barcode_add_body import PostStockProductsByBarcodeBarcodeAddBody
from .post_stock_products_by_barcode_barcode_consume_body import PostStockProductsByBarcodeBarcodeConsumeBody
from .post_stock_products_by_barcode_barcode_inventory_body import PostStockProductsByBarcodeBarcodeInventoryBody
from .post_stock_products_by_barcode_barcode_open_body import PostStockProductsByBarcodeBarcodeOpenBody
from .post_stock_products_by_barcode_barcode_transfer_body import PostStockProductsByBarcodeBarcodeTransferBody
from .post_stock_products_product_id_add_body import PostStockProductsProductIdAddBody
from .post_stock_products_product_id_consume_body import PostStockProductsProductIdConsumeBody
from .post_stock_products_product_id_inventory_body import PostStockProductsProductIdInventoryBody
from .post_stock_products_product_id_open_body import PostStockProductsProductIdOpenBody
from .post_stock_products_product_id_transfer_body import PostStockProductsProductIdTransferBody
from .post_stock_shoppinglist_add_expired_products_body import PostStockShoppinglistAddExpiredProductsBody
from .post_stock_shoppinglist_add_missing_products_body import PostStockShoppinglistAddMissingProductsBody
from .post_stock_shoppinglist_add_overdue_products_body import PostStockShoppinglistAddOverdueProductsBody
from .post_stock_shoppinglist_add_product_body import PostStockShoppinglistAddProductBody
from .post_stock_shoppinglist_clear_body import PostStockShoppinglistClearBody
from .post_stock_shoppinglist_remove_product_body import PostStockShoppinglistRemoveProductBody
from .post_tasks_task_id_complete_body import PostTasksTaskIdCompleteBody
from .post_users_user_id_permissions_body import PostUsersUserIdPermissionsBody
from .product import Product
from .product_barcode import ProductBarcode
from .product_details_response import ProductDetailsResponse
from .product_price_history import ProductPriceHistory
from .product_userfields import ProductUserfields
from .product_without_userfields import ProductWithoutUserfields
from .put_stock_entry_entry_id_body import PutStockEntryEntryIdBody
from .put_users_user_id_permissions_body import PutUsersUserIdPermissionsBody
from .quantity_unit import QuantityUnit
from .quantity_unit_userfields import QuantityUnitUserfields
from .recipe_fulfillment_response import RecipeFulfillmentResponse
from .session import Session
from .shopping_list_item import ShoppingListItem
from .shopping_list_item_userfields import ShoppingListItemUserfields
from .shopping_location import ShoppingLocation
from .shopping_location_userfields import ShoppingLocationUserfields
from .stock_entry import StockEntry
from .stock_journal import StockJournal
from .stock_journal_summary import StockJournalSummary
from .stock_location import StockLocation
from .stock_log_entry import StockLogEntry
from .stock_transaction_type import StockTransactionType
from .string_enum_template import StringEnumTemplate
from .task import Task
from .task_category import TaskCategory
from .task_userfields import TaskUserfields
from .time_response import TimeResponse
from .user import User
from .user_dto import UserDto
from .user_setting import UserSetting

__all__ = (
    "ApiKey",
    "Battery",
    "BatteryChargeCycleEntry",
    "BatteryDetailsResponse",
    "BatteryUserfields",
    "Chore",
    "ChoreAssignmentType",
    "ChoreDetailsResponse",
    "ChoreLogEntry",
    "ChorePeriodType",
    "ChoreUserfields",
    "CurrentBatteryResponse",
    "CurrentChoreResponse",
    "CurrentStockResponse",
    "CurrentTaskResponse",
    "CurrentVolatilStockResponse",
    "CurrentVolatilStockResponseMissingProductsItem",
    "DbChangedTimeResponse",
    "Error400",
    "Error500",
    "Error500ErrorDetails",
    "ExposedEntity",
    "ExposedEntityEditRequiresAdmin",
    "ExposedEntityIncludingUserEntities",
    "ExposedEntityIncludingUserEntitiesNotIncludingNotEditable",
    "ExposedEntityNoDelete",
    "ExposedEntityNoEdit",
    "ExposedEntityNoListing",
    "ExposedEntityNotIncludingNotDeletable",
    "ExposedEntityNotIncludingNotEditable",
    "ExposedEntityNotIncludingNotListable",
    "ExternalBarcodeLookupResponse",
    "FileGroups",
    "GetBatteriesBatteryIdPrintlabelResponse200",
    "GetCalendarIcalSharingLinkResponse200",
    "GetChoresChoreIdPrintlabelResponse200",
    "GetFilesGroupFileNameForceServeAs",
    "GetPrintShoppinglistThermalResponse200",
    "GetRecipesRecipeIdPrintlabelResponse200",
    "GetStockEntryEntryIdPrintlabelResponse200",
    "GetStockProductsProductIdPrintlabelResponse200",
    "GetSystemConfigResponse200",
    "GetSystemInfoResponse200",
    "GetSystemInfoResponse200GrocyVersion",
    "GetSystemLocalizationStringsResponse200",
    "GetUserfieldsEntityObjectIdResponse200",
    "GetUserResponse200",
    "GetUserSettingsResponse200",
    "GetUsersUserIdPermissionsResponse200Item",
    "Location",
    "LocationUserfields",
    "MissingLocalizationRequest",
    "PostBatteriesBatteryIdChargeBody",
    "PostChoresChoreIdExecuteBody",
    "PostChoresExecutionsCalculateNextAssignmentsBody",
    "PostObjectsEntityResponse200",
    "PostRecipesRecipeIdAddNotFulfilledProductsToShoppinglistBody",
    "PostRecipesRecipeIdCopyResponse200",
    "PostStockProductsByBarcodeBarcodeAddBody",
    "PostStockProductsByBarcodeBarcodeConsumeBody",
    "PostStockProductsByBarcodeBarcodeInventoryBody",
    "PostStockProductsByBarcodeBarcodeOpenBody",
    "PostStockProductsByBarcodeBarcodeTransferBody",
    "PostStockProductsProductIdAddBody",
    "PostStockProductsProductIdConsumeBody",
    "PostStockProductsProductIdInventoryBody",
    "PostStockProductsProductIdOpenBody",
    "PostStockProductsProductIdTransferBody",
    "PostStockShoppinglistAddExpiredProductsBody",
    "PostStockShoppinglistAddMissingProductsBody",
    "PostStockShoppinglistAddOverdueProductsBody",
    "PostStockShoppinglistAddProductBody",
    "PostStockShoppinglistClearBody",
    "PostStockShoppinglistRemoveProductBody",
    "PostTasksTaskIdCompleteBody",
    "PostUsersUserIdPermissionsBody",
    "Product",
    "ProductBarcode",
    "ProductDetailsResponse",
    "ProductPriceHistory",
    "ProductUserfields",
    "ProductWithoutUserfields",
    "PutStockEntryEntryIdBody",
    "PutUsersUserIdPermissionsBody",
    "QuantityUnit",
    "QuantityUnitUserfields",
    "RecipeFulfillmentResponse",
    "Session",
    "ShoppingListItem",
    "ShoppingListItemUserfields",
    "ShoppingLocation",
    "ShoppingLocationUserfields",
    "StockEntry",
    "StockJournal",
    "StockJournalSummary",
    "StockLocation",
    "StockLogEntry",
    "StockTransactionType",
    "StringEnumTemplate",
    "Task",
    "TaskCategory",
    "TaskUserfields",
    "TimeResponse",
    "User",
    "UserDto",
    "UserSetting",
)
