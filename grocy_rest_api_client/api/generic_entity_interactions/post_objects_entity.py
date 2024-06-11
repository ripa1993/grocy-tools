from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.battery import Battery
from ...models.chore import Chore
from ...models.error_400 import Error400
from ...models.exposed_entity_not_including_not_editable import ExposedEntityNotIncludingNotEditable
from ...models.location import Location
from ...models.post_objects_entity_response_200 import PostObjectsEntityResponse200
from ...models.product import Product
from ...models.product_barcode import ProductBarcode
from ...models.quantity_unit import QuantityUnit
from ...models.shopping_list_item import ShoppingListItem
from ...models.stock_entry import StockEntry
from ...types import Response


def _get_kwargs(
    entity: ExposedEntityNotIncludingNotEditable,
    *,
    body: Union[
        "Battery", "Chore", "Location", "Product", "ProductBarcode", "QuantityUnit", "ShoppingListItem", "StockEntry"
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/objects/{entity}",
    }

    _body: Dict[str, Any]
    if isinstance(body, Product):
        _body = body.to_dict()
    elif isinstance(body, Chore):
        _body = body.to_dict()
    elif isinstance(body, Battery):
        _body = body.to_dict()
    elif isinstance(body, Location):
        _body = body.to_dict()
    elif isinstance(body, QuantityUnit):
        _body = body.to_dict()
    elif isinstance(body, ShoppingListItem):
        _body = body.to_dict()
    elif isinstance(body, StockEntry):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, PostObjectsEntityResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PostObjectsEntityResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error400, PostObjectsEntityResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: ExposedEntityNotIncludingNotEditable,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Battery", "Chore", "Location", "Product", "ProductBarcode", "QuantityUnit", "ShoppingListItem", "StockEntry"
    ],
) -> Response[Union[Error400, PostObjectsEntityResponse200]]:
    """Adds a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotEditable):
        body (Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit',
            'ShoppingListItem', 'StockEntry']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, PostObjectsEntityResponse200]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: ExposedEntityNotIncludingNotEditable,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Battery", "Chore", "Location", "Product", "ProductBarcode", "QuantityUnit", "ShoppingListItem", "StockEntry"
    ],
) -> Optional[Union[Error400, PostObjectsEntityResponse200]]:
    """Adds a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotEditable):
        body (Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit',
            'ShoppingListItem', 'StockEntry']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, PostObjectsEntityResponse200]
    """

    return sync_detailed(
        entity=entity,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entity: ExposedEntityNotIncludingNotEditable,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Battery", "Chore", "Location", "Product", "ProductBarcode", "QuantityUnit", "ShoppingListItem", "StockEntry"
    ],
) -> Response[Union[Error400, PostObjectsEntityResponse200]]:
    """Adds a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotEditable):
        body (Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit',
            'ShoppingListItem', 'StockEntry']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, PostObjectsEntityResponse200]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: ExposedEntityNotIncludingNotEditable,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        "Battery", "Chore", "Location", "Product", "ProductBarcode", "QuantityUnit", "ShoppingListItem", "StockEntry"
    ],
) -> Optional[Union[Error400, PostObjectsEntityResponse200]]:
    """Adds a single object of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotEditable):
        body (Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit',
            'ShoppingListItem', 'StockEntry']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, PostObjectsEntityResponse200]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            client=client,
            body=body,
        )
    ).parsed
