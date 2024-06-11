from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...types import Response


def _get_kwargs(
    chore_id_to_keep: int,
    chore_id_to_remove: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/chores/{chore_id_to_keep}/merge/{chore_id_to_remove}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error400]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chore_id_to_keep: int,
    chore_id_to_remove: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Error400]]:
    """Merges two chores into one

    Args:
        chore_id_to_keep (int):
        chore_id_to_remove (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400]]
    """

    kwargs = _get_kwargs(
        chore_id_to_keep=chore_id_to_keep,
        chore_id_to_remove=chore_id_to_remove,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chore_id_to_keep: int,
    chore_id_to_remove: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Error400]]:
    """Merges two chores into one

    Args:
        chore_id_to_keep (int):
        chore_id_to_remove (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400]
    """

    return sync_detailed(
        chore_id_to_keep=chore_id_to_keep,
        chore_id_to_remove=chore_id_to_remove,
        client=client,
    ).parsed


async def asyncio_detailed(
    chore_id_to_keep: int,
    chore_id_to_remove: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Error400]]:
    """Merges two chores into one

    Args:
        chore_id_to_keep (int):
        chore_id_to_remove (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400]]
    """

    kwargs = _get_kwargs(
        chore_id_to_keep=chore_id_to_keep,
        chore_id_to_remove=chore_id_to_remove,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chore_id_to_keep: int,
    chore_id_to_remove: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Error400]]:
    """Merges two chores into one

    Args:
        chore_id_to_keep (int):
        chore_id_to_remove (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400]
    """

    return (
        await asyncio_detailed(
            chore_id_to_keep=chore_id_to_keep,
            chore_id_to_remove=chore_id_to_remove,
            client=client,
        )
    ).parsed
