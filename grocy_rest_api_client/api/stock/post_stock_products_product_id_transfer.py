from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.post_stock_products_product_id_transfer_body import PostStockProductsProductIdTransferBody
from ...models.stock_log_entry import StockLogEntry
from ...types import Response


def _get_kwargs(
    product_id: int,
    *,
    body: PostStockProductsProductIdTransferBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/stock/products/{product_id}/transfer",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, List["StockLogEntry"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = StockLogEntry.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Error400, List["StockLogEntry"]]]:
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
    body: PostStockProductsProductIdTransferBody,
) -> Response[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the given product from one location to another (this is currently not
    supported for tare weight handling enabled products)

    Args:
        product_id (int):
        body (PostStockProductsProductIdTransferBody):  Example: {'amount': 1, 'location_id_from':
            1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, List['StockLogEntry']]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsProductIdTransferBody,
) -> Optional[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the given product from one location to another (this is currently not
    supported for tare weight handling enabled products)

    Args:
        product_id (int):
        body (PostStockProductsProductIdTransferBody):  Example: {'amount': 1, 'location_id_from':
            1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, List['StockLogEntry']]
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsProductIdTransferBody,
) -> Response[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the given product from one location to another (this is currently not
    supported for tare weight handling enabled products)

    Args:
        product_id (int):
        body (PostStockProductsProductIdTransferBody):  Example: {'amount': 1, 'location_id_from':
            1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, List['StockLogEntry']]]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsProductIdTransferBody,
) -> Optional[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the given product from one location to another (this is currently not
    supported for tare weight handling enabled products)

    Args:
        product_id (int):
        body (PostStockProductsProductIdTransferBody):  Example: {'amount': 1, 'location_id_from':
            1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, List['StockLogEntry']]
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
