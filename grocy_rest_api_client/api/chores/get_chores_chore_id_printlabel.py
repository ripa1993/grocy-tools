from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.get_chores_chore_id_printlabel_response_200 import GetChoresChoreIdPrintlabelResponse200
from ...types import Response


def _get_kwargs(
    chore_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/chores/{chore_id}/printlabel",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetChoresChoreIdPrintlabelResponse200.from_dict(response.json())

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
) -> Response[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]:
    """Prints the Grocycode label of the given chore on the configured label printer

    Args:
        chore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]
    """

    kwargs = _get_kwargs(
        chore_id=chore_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]:
    """Prints the Grocycode label of the given chore on the configured label printer

    Args:
        chore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, GetChoresChoreIdPrintlabelResponse200]
    """

    return sync_detailed(
        chore_id=chore_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]:
    """Prints the Grocycode label of the given chore on the configured label printer

    Args:
        chore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]
    """

    kwargs = _get_kwargs(
        chore_id=chore_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error400, GetChoresChoreIdPrintlabelResponse200]]:
    """Prints the Grocycode label of the given chore on the configured label printer

    Args:
        chore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, GetChoresChoreIdPrintlabelResponse200]
    """

    return (
        await asyncio_detailed(
            chore_id=chore_id,
            client=client,
        )
    ).parsed
