from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.get_print_shoppinglist_thermal_response_200 import GetPrintShoppinglistThermalResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    list_: Union[Unset, int] = 1,
    print_header: Union[Unset, bool] = True,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["list"] = list_

    params["printHeader"] = print_header

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/print/shoppinglist/thermal",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, GetPrintShoppinglistThermalResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetPrintShoppinglistThermalResponse200.from_dict(response.json())

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
) -> Response[Union[Error400, GetPrintShoppinglistThermalResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    list_: Union[Unset, int] = 1,
    print_header: Union[Unset, bool] = True,
) -> Response[Union[Error400, GetPrintShoppinglistThermalResponse200]]:
    """Prints the shoppinglist with a thermal printer

    Args:
        list_ (Union[Unset, int]):  Default: 1.
        print_header (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, GetPrintShoppinglistThermalResponse200]]
    """

    kwargs = _get_kwargs(
        list_=list_,
        print_header=print_header,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    list_: Union[Unset, int] = 1,
    print_header: Union[Unset, bool] = True,
) -> Optional[Union[Error400, GetPrintShoppinglistThermalResponse200]]:
    """Prints the shoppinglist with a thermal printer

    Args:
        list_ (Union[Unset, int]):  Default: 1.
        print_header (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, GetPrintShoppinglistThermalResponse200]
    """

    return sync_detailed(
        client=client,
        list_=list_,
        print_header=print_header,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    list_: Union[Unset, int] = 1,
    print_header: Union[Unset, bool] = True,
) -> Response[Union[Error400, GetPrintShoppinglistThermalResponse200]]:
    """Prints the shoppinglist with a thermal printer

    Args:
        list_ (Union[Unset, int]):  Default: 1.
        print_header (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, GetPrintShoppinglistThermalResponse200]]
    """

    kwargs = _get_kwargs(
        list_=list_,
        print_header=print_header,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    list_: Union[Unset, int] = 1,
    print_header: Union[Unset, bool] = True,
) -> Optional[Union[Error400, GetPrintShoppinglistThermalResponse200]]:
    """Prints the shoppinglist with a thermal printer

    Args:
        list_ (Union[Unset, int]):  Default: 1.
        print_header (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, GetPrintShoppinglistThermalResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            list_=list_,
            print_header=print_header,
        )
    ).parsed
