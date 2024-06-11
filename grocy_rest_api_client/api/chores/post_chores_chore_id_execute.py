from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chore_log_entry import ChoreLogEntry
from ...models.error_400 import Error400
from ...models.post_chores_chore_id_execute_body import PostChoresChoreIdExecuteBody
from ...types import Response


def _get_kwargs(
    chore_id: int,
    *,
    body: PostChoresChoreIdExecuteBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/chores/{chore_id}/execute",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChoreLogEntry, Error400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChoreLogEntry.from_dict(response.json())

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
) -> Response[Union[ChoreLogEntry, Error400]]:
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
    body: PostChoresChoreIdExecuteBody,
) -> Response[Union[ChoreLogEntry, Error400]]:
    """Tracks an execution of the given chore

    Args:
        chore_id (int):
        body (PostChoresChoreIdExecuteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChoreLogEntry, Error400]]
    """

    kwargs = _get_kwargs(
        chore_id=chore_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChoresChoreIdExecuteBody,
) -> Optional[Union[ChoreLogEntry, Error400]]:
    """Tracks an execution of the given chore

    Args:
        chore_id (int):
        body (PostChoresChoreIdExecuteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChoreLogEntry, Error400]
    """

    return sync_detailed(
        chore_id=chore_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChoresChoreIdExecuteBody,
) -> Response[Union[ChoreLogEntry, Error400]]:
    """Tracks an execution of the given chore

    Args:
        chore_id (int):
        body (PostChoresChoreIdExecuteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChoreLogEntry, Error400]]
    """

    kwargs = _get_kwargs(
        chore_id=chore_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chore_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostChoresChoreIdExecuteBody,
) -> Optional[Union[ChoreLogEntry, Error400]]:
    """Tracks an execution of the given chore

    Args:
        chore_id (int):
        body (PostChoresChoreIdExecuteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChoreLogEntry, Error400]
    """

    return (
        await asyncio_detailed(
            chore_id=chore_id,
            client=client,
            body=body,
        )
    ).parsed
