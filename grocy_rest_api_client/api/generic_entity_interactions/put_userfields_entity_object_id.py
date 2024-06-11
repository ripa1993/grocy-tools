from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.exposed_entity_including_user_entities_not_including_not_editable import (
    ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
)
from ...types import Response


def _get_kwargs(
    entity: ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
    object_id: str,
    *,
    body: Any,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/userfields/{entity}/{object_id}",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    entity: ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Response[Union[Any, Error400]]:
    """Edits the given userfields of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntitiesNotIncludingNotEditable):
        object_id (str):
        body (Any): Key/value pairs of userfields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        object_id=object_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Optional[Union[Any, Error400]]:
    """Edits the given userfields of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntitiesNotIncludingNotEditable):
        object_id (str):
        body (Any): Key/value pairs of userfields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400]
    """

    return sync_detailed(
        entity=entity,
        object_id=object_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entity: ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Response[Union[Any, Error400]]:
    """Edits the given userfields of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntitiesNotIncludingNotEditable):
        object_id (str):
        body (Any): Key/value pairs of userfields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error400]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        object_id=object_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: ExposedEntityIncludingUserEntitiesNotIncludingNotEditable,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Optional[Union[Any, Error400]]:
    """Edits the given userfields of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntitiesNotIncludingNotEditable):
        object_id (str):
        body (Any): Key/value pairs of userfields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error400]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            object_id=object_id,
            client=client,
            body=body,
        )
    ).parsed
