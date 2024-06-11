from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.stock_log_entry import StockLogEntry
from ...types import Response


def _get_kwargs(
    booking_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/stock/bookings/{booking_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, StockLogEntry]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StockLogEntry.from_dict(response.json())

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
) -> Response[Union[Error400, StockLogEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    booking_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error400, StockLogEntry]]:
    """Returns the given stock booking

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, StockLogEntry]]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    booking_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error400, StockLogEntry]]:
    """Returns the given stock booking

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, StockLogEntry]
    """

    return sync_detailed(
        booking_id=booking_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    booking_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error400, StockLogEntry]]:
    """Returns the given stock booking

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, StockLogEntry]]
    """

    kwargs = _get_kwargs(
        booking_id=booking_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    booking_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error400, StockLogEntry]]:
    """Returns the given stock booking

    Args:
        booking_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, StockLogEntry]
    """

    return (
        await asyncio_detailed(
            booking_id=booking_id,
            client=client,
        )
    ).parsed
