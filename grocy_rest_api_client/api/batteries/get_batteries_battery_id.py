from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.battery_details_response import BatteryDetailsResponse
from ...models.error_400 import Error400
from ...types import Response


def _get_kwargs(
    battery_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/batteries/{battery_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BatteryDetailsResponse, Error400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BatteryDetailsResponse.from_dict(response.json())

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
) -> Response[Union[BatteryDetailsResponse, Error400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    battery_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BatteryDetailsResponse, Error400]]:
    """Returns details of the given battery

    Args:
        battery_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BatteryDetailsResponse, Error400]]
    """

    kwargs = _get_kwargs(
        battery_id=battery_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    battery_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[BatteryDetailsResponse, Error400]]:
    """Returns details of the given battery

    Args:
        battery_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BatteryDetailsResponse, Error400]
    """

    return sync_detailed(
        battery_id=battery_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    battery_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[BatteryDetailsResponse, Error400]]:
    """Returns details of the given battery

    Args:
        battery_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BatteryDetailsResponse, Error400]]
    """

    kwargs = _get_kwargs(
        battery_id=battery_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    battery_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[BatteryDetailsResponse, Error400]]:
    """Returns details of the given battery

    Args:
        battery_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BatteryDetailsResponse, Error400]
    """

    return (
        await asyncio_detailed(
            battery_id=battery_id,
            client=client,
        )
    ).parsed
