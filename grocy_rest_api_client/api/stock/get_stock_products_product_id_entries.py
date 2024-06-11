from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_500 import Error500
from ...models.stock_entry import StockEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: int,
    *,
    include_sub_products: Union[Unset, bool] = UNSET,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["include_sub_products"] = include_sub_products

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
        "url": f"/stock/products/{product_id}/entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, Error500, List["StockEntry"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StockEntry.from_dict(response_200_item_data)

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
) -> Response[Union[Error400, Error500, List["StockEntry"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sub_products: Union[Unset, bool] = UNSET,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error400, Error500, List["StockEntry"]]]:
    """Returns all stock entries of the given product in order of next use (Opened first, then first due
    first, then first in first out)

    Args:
        product_id (int):
        include_sub_products (Union[Unset, bool]):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, Error500, List['StockEntry']]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        include_sub_products=include_sub_products,
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
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sub_products: Union[Unset, bool] = UNSET,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error400, Error500, List["StockEntry"]]]:
    """Returns all stock entries of the given product in order of next use (Opened first, then first due
    first, then first in first out)

    Args:
        product_id (int):
        include_sub_products (Union[Unset, bool]):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, Error500, List['StockEntry']]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        include_sub_products=include_sub_products,
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sub_products: Union[Unset, bool] = UNSET,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error400, Error500, List["StockEntry"]]]:
    """Returns all stock entries of the given product in order of next use (Opened first, then first due
    first, then first in first out)

    Args:
        product_id (int):
        include_sub_products (Union[Unset, bool]):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, Error500, List['StockEntry']]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        include_sub_products=include_sub_products,
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    include_sub_products: Union[Unset, bool] = UNSET,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error400, Error500, List["StockEntry"]]]:
    """Returns all stock entries of the given product in order of next use (Opened first, then first due
    first, then first in first out)

    Args:
        product_id (int):
        include_sub_products (Union[Unset, bool]):
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, Error500, List['StockEntry']]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            include_sub_products=include_sub_products,
            query=query,
            order=order,
            limit=limit,
            offset=offset,
        )
    ).parsed
