from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.battery import Battery
from ...models.chore import Chore
from ...models.error_400 import Error400
from ...models.error_500 import Error500
from ...models.exposed_entity_not_including_not_listable import ExposedEntityNotIncludingNotListable
from ...models.location import Location
from ...models.product import Product
from ...models.product_barcode import ProductBarcode
from ...models.quantity_unit import QuantityUnit
from ...models.shopping_list_item import ShoppingListItem
from ...models.stock_entry import StockEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity: ExposedEntityNotIncludingNotListable,
    *,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_query: Union[Unset, List[str]] = UNSET
    if not isinstance(query, Unset):
        json_query = query

    params["query[]"] = json_query

    params["order"] = order

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/objects/{entity}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Error400,
        Error500,
        List[
            Union[
                "Battery",
                "Chore",
                "Location",
                "Product",
                "ProductBarcode",
                "QuantityUnit",
                "ShoppingListItem",
                "StockEntry",
            ]
        ],
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
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
                    response_200_item_type_0 = Product.from_dict(data)

                    return response_200_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_1 = Chore.from_dict(data)

                    return response_200_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_2 = Battery.from_dict(data)

                    return response_200_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_3 = Location.from_dict(data)

                    return response_200_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_4 = QuantityUnit.from_dict(data)

                    return response_200_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_5 = ShoppingListItem.from_dict(data)

                    return response_200_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_6 = StockEntry.from_dict(data)

                    return response_200_item_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_7 = ProductBarcode.from_dict(data)

                return response_200_item_type_7

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Error400,
        Error500,
        List[
            Union[
                "Battery",
                "Chore",
                "Location",
                "Product",
                "ProductBarcode",
                "QuantityUnit",
                "ShoppingListItem",
                "StockEntry",
            ]
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
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[
    Union[
        Error400,
        Error500,
        List[
            Union[
                "Battery",
                "Chore",
                "Location",
                "Product",
                "ProductBarcode",
                "QuantityUnit",
                "ShoppingListItem",
                "StockEntry",
            ]
        ],
    ]
]:
    """Returns all objects of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, Error500, List[Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: ExposedEntityNotIncludingNotListable,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[
    Union[
        Error400,
        Error500,
        List[
            Union[
                "Battery",
                "Chore",
                "Location",
                "Product",
                "ProductBarcode",
                "QuantityUnit",
                "ShoppingListItem",
                "StockEntry",
            ]
        ],
    ]
]:
    """Returns all objects of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, Error500, List[Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]]
    """

    return sync_detailed(
        entity=entity,
        client=client,
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    entity: ExposedEntityNotIncludingNotListable,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[
    Union[
        Error400,
        Error500,
        List[
            Union[
                "Battery",
                "Chore",
                "Location",
                "Product",
                "ProductBarcode",
                "QuantityUnit",
                "ShoppingListItem",
                "StockEntry",
            ]
        ],
    ]
]:
    """Returns all objects of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, Error500, List[Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: ExposedEntityNotIncludingNotListable,
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[
    Union[
        Error400,
        Error500,
        List[
            Union[
                "Battery",
                "Chore",
                "Location",
                "Product",
                "ProductBarcode",
                "QuantityUnit",
                "ShoppingListItem",
                "StockEntry",
            ]
        ],
    ]
]:
    """Returns all objects of the given entity

    Args:
        entity (ExposedEntityNotIncludingNotListable):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, Error500, List[Union['Battery', 'Chore', 'Location', 'Product', 'ProductBarcode', 'QuantityUnit', 'ShoppingListItem', 'StockEntry']]]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            client=client,
            query=query,
            order=order,
            limit=limit,
            offset=offset,
        )
    ).parsed
