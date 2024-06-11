from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.exposed_entity_including_user_entities import ExposedEntityIncludingUserEntities
from ...models.get_userfields_entity_object_id_response_200 import GetUserfieldsEntityObjectIdResponse200
from ...types import Response


def _get_kwargs(
    entity: ExposedEntityIncludingUserEntities,
    object_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/userfields/{entity}/{object_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetUserfieldsEntityObjectIdResponse200.from_dict(response.json())

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
) -> Response[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity: ExposedEntityIncludingUserEntities,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]:
    """Returns all userfields with their values of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntities):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity: ExposedEntityIncludingUserEntities,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]:
    """Returns all userfields with their values of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntities):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, GetUserfieldsEntityObjectIdResponse200]
    """

    return sync_detailed(
        entity=entity,
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity: ExposedEntityIncludingUserEntities,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]:
    """Returns all userfields with their values of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntities):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]
    """

    kwargs = _get_kwargs(
        entity=entity,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity: ExposedEntityIncludingUserEntities,
    object_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error400, GetUserfieldsEntityObjectIdResponse200]]:
    """Returns all userfields with their values of the given object of the given entity

    Args:
        entity (ExposedEntityIncludingUserEntities):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, GetUserfieldsEntityObjectIdResponse200]
    """

    return (
        await asyncio_detailed(
            entity=entity,
            object_id=object_id,
            client=client,
        )
    ).parsed
