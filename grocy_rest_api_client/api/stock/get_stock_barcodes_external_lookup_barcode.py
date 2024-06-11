from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.external_barcode_lookup_response import ExternalBarcodeLookupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    barcode: str,
    *,
    add: Union[Unset, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["add"] = add

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/stock/barcodes/external-lookup/{barcode}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, ExternalBarcodeLookupResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExternalBarcodeLookupResponse.from_dict(response.json())

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
) -> Response[Union[Error400, ExternalBarcodeLookupResponse]]:
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
    add: Union[Unset, bool] = False,
) -> Response[Union[Error400, ExternalBarcodeLookupResponse]]:
    """Executes an external barcode lookoup via the configured plugin with the given barcode

    Args:
        barcode (str):
        add (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, ExternalBarcodeLookupResponse]]
    """

    kwargs = _get_kwargs(
        barcode=barcode,
        add=add,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    add: Union[Unset, bool] = False,
) -> Optional[Union[Error400, ExternalBarcodeLookupResponse]]:
    """Executes an external barcode lookoup via the configured plugin with the given barcode

    Args:
        barcode (str):
        add (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, ExternalBarcodeLookupResponse]
    """

    return sync_detailed(
        barcode=barcode,
        client=client,
        add=add,
    ).parsed


async def asyncio_detailed(
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    add: Union[Unset, bool] = False,
) -> Response[Union[Error400, ExternalBarcodeLookupResponse]]:
    """Executes an external barcode lookoup via the configured plugin with the given barcode

    Args:
        barcode (str):
        add (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, ExternalBarcodeLookupResponse]]
    """

    kwargs = _get_kwargs(
        barcode=barcode,
        add=add,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    barcode: str,
    *,
    client: Union[AuthenticatedClient, Client],
    add: Union[Unset, bool] = False,
) -> Optional[Union[Error400, ExternalBarcodeLookupResponse]]:
    """Executes an external barcode lookoup via the configured plugin with the given barcode

    Args:
        barcode (str):
        add (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, ExternalBarcodeLookupResponse]
    """

    return (
        await asyncio_detailed(
            barcode=barcode,
            client=client,
            add=add,
        )
    ).parsed
