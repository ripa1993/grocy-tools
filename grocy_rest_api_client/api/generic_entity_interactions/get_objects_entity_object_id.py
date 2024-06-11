from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.battery import Battery
from ...models.chore import Chore
from ...models.error_400 import Error400
from ...models.exposed_entity_not_including_not_listable import ExposedEntityNotIncludingNotListable
from ...models.location import Location
from ...models.product import Product
from ...models.product_barcode import ProductBarcode
from ...models.quantity_unit import QuantityUnit
from ...models.shopping_list_item import ShoppingListItem
from ...models.stock_entry import StockEntry
from ...types import Response


def _get_kwargs(
    entity: ExposedEntityNotIncludingNotListable,
    object_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/objects/{entity}/{object_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Error400,
        Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Product.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = Chore.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = Battery.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = Location.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = QuantityUnit.from_dict(data)

                return response_200_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = ShoppingListItem.from_dict(data)

                return response_200_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_6 = StockEntry.from_dict(data)

                return response_200_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_7 = ProductBarcode.from_dict(data)

            return response_200_type_7

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = Error400.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Error400,
        Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: ExposedEntityNotIncludingNotListable,
    object_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        Error400,
        Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ],
    ]
]:
    """Returns a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: ExposedEntityNotIncludingNotListable,
    object_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        Error400,
        Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ],
    ]
]:
    """Returns a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]
    """

    return sync_detailed(
        entity=entity,
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity: ExposedEntityNotIncludingNotListable,
    object_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        Error400,
        Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ],
    ]
]:
    """Returns a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: ExposedEntityNotIncludingNotListable,
    object_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        Error400,
        Union[
            "Battery",
            "Chore",
            "Location",
            "Product",
            "ProductBarcode",
            "QuantityUnit",
            "ShoppingListItem",
            "StockEntry",
        ],
    ]
]:
    """Returns a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            object_id=object_id,
            client=client,
        )
    ).parsed
