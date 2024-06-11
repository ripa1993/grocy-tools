from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.current_chore_response import CurrentChoreResponse
from ...models.error_500 import Error500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

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
        "url": "/chores",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error500, List["CurrentChoreResponse"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CurrentChoreResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error500, List["CurrentChoreResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error500, List["CurrentChoreResponse"]]]:
    """Returns all chores incl. the next estimated execution time per chore

    Args:
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error500, List['CurrentChoreResponse']]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error500, List["CurrentChoreResponse"]]]:
    """Returns all chores incl. the next estimated execution time per chore

    Args:
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error500, List['CurrentChoreResponse']]
    """

    return sync_detailed(
        client=client,
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[Error500, List["CurrentChoreResponse"]]]:
    """Returns all chores incl. the next estimated execution time per chore

    Args:
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error500, List['CurrentChoreResponse']]]
    """

    kwargs = _get_kwargs(
        query=query,
        order=order,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[Error500, List["CurrentChoreResponse"]]]:
    """Returns all chores incl. the next estimated execution time per chore

    Args:
        query (Union[Unset, List[str]]):
        order (Union[Unset, str]):
        limit (Union[Unset, int]):
        offset (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error500, List['CurrentChoreResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            order=order,
            limit=limit,
            offset=offset,
        )
    ).parsed
