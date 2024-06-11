from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.post_stock_products_by_barcode_barcode_transfer_body import PostStockProductsByBarcodeBarcodeTransferBody
from ...models.stock_log_entry import StockLogEntry
from ...types import Response


def _get_kwargs(
    barcode: str,
    *,
    body: PostStockProductsByBarcodeBarcodeTransferBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/stock/products/by-barcode/{barcode}/transfer",
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
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsByBarcodeBarcodeTransferBody,
) -> Response[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the by its barcode given product from one location to another (this is
    currently not supported for tare weight handling enabled products)

    Args:
        barcode (str):
        body (PostStockProductsByBarcodeBarcodeTransferBody):  Example: {'amount': 1,
            'location_id_from': 1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, List['StockLogEntry']]]
    """

    kwargs = _get_kwargs(
        barcode=barcode,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsByBarcodeBarcodeTransferBody,
) -> Optional[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the by its barcode given product from one location to another (this is
    currently not supported for tare weight handling enabled products)

    Args:
        barcode (str):
        body (PostStockProductsByBarcodeBarcodeTransferBody):  Example: {'amount': 1,
            'location_id_from': 1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, List['StockLogEntry']]
    """

    return sync_detailed(
        barcode=barcode,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsByBarcodeBarcodeTransferBody,
) -> Response[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the by its barcode given product from one location to another (this is
    currently not supported for tare weight handling enabled products)

    Args:
        barcode (str):
        body (PostStockProductsByBarcodeBarcodeTransferBody):  Example: {'amount': 1,
            'location_id_from': 1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, List['StockLogEntry']]]
    """

    kwargs = _get_kwargs(
        barcode=barcode,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostStockProductsByBarcodeBarcodeTransferBody,
) -> Optional[Union[Error400, List["StockLogEntry"]]]:
    """Transfers the given amount of the by its barcode given product from one location to another (this is
    currently not supported for tare weight handling enabled products)

    Args:
        barcode (str):
        body (PostStockProductsByBarcodeBarcodeTransferBody):  Example: {'amount': 1,
            'location_id_from': 1, 'location_id_to': 2}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, List['StockLogEntry']]
    """

    return (
        await asyncio_detailed(
            barcode=barcode,
            client=client,
            body=body,
        )
    ).parsed
