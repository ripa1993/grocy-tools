from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.file_groups import FileGroups
from ...types import Response


def _get_kwargs(
    group: FileGroups,
    file_name: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/files/{group}/{file_name}",
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
    group: FileGroups,
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Error400]]:
    """Deletes the given file

    Args:
        group (FileGroups):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400]]
    """

    kwargs = _get_kwargs(
        group=group,
        file_name=file_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group: FileGroups,
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Error400]]:
    """Deletes the given file

    Args:
        group (FileGroups):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400]
    """

    return sync_detailed(
        group=group,
        file_name=file_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    group: FileGroups,
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Error400]]:
    """Deletes the given file

    Args:
        group (FileGroups):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400]]
    """

    kwargs = _get_kwargs(
        group=group,
        file_name=file_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group: FileGroups,
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Error400]]:
    """Deletes the given file

    Args:
        group (FileGroups):
        file_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400]
    """

    return (
        await asyncio_detailed(
            group=group,
            file_name=file_name,
            client=client,
        )
    ).parsed
