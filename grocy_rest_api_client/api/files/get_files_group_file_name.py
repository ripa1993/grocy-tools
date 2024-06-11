from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.file_groups import FileGroups
from ...models.get_files_group_file_name_force_serve_as import GetFilesGroupFileNameForceServeAs
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    group: FileGroups,
    file_name: str,
    *,
    force_serve_as: Union[Unset, GetFilesGroupFileNameForceServeAs] = UNSET,
    best_fit_height: Union[Unset, float] = UNSET,
    best_fit_width: Union[Unset, float] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_force_serve_as: Union[Unset, str] = UNSET
    if not isinstance(force_serve_as, Unset):
        json_force_serve_as = force_serve_as.value

    params["force_serve_as"] = json_force_serve_as

    params["best_fit_height"] = best_fit_height

    params["best_fit_width"] = best_fit_width

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/files/{group}/{file_name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error400, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

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
) -> Response[Union[Error400, File]]:
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
    force_serve_as: Union[Unset, GetFilesGroupFileNameForceServeAs] = UNSET,
    best_fit_height: Union[Unset, float] = UNSET,
    best_fit_width: Union[Unset, float] = UNSET,
) -> Response[Union[Error400, File]]:
    """Serves the given file

     With proper Content-Type header

    Args:
        group (FileGroups):
        file_name (str):
        force_serve_as (Union[Unset, GetFilesGroupFileNameForceServeAs]):
        best_fit_height (Union[Unset, float]):
        best_fit_width (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, File]]
    """

    kwargs = _get_kwargs(
        group=group,
        file_name=file_name,
        force_serve_as=force_serve_as,
        best_fit_height=best_fit_height,
        best_fit_width=best_fit_width,
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
    force_serve_as: Union[Unset, GetFilesGroupFileNameForceServeAs] = UNSET,
    best_fit_height: Union[Unset, float] = UNSET,
    best_fit_width: Union[Unset, float] = UNSET,
) -> Optional[Union[Error400, File]]:
    """Serves the given file

     With proper Content-Type header

    Args:
        group (FileGroups):
        file_name (str):
        force_serve_as (Union[Unset, GetFilesGroupFileNameForceServeAs]):
        best_fit_height (Union[Unset, float]):
        best_fit_width (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, File]
    """

    return sync_detailed(
        group=group,
        file_name=file_name,
        client=client,
        force_serve_as=force_serve_as,
        best_fit_height=best_fit_height,
        best_fit_width=best_fit_width,
    ).parsed


async def asyncio_detailed(
    group: FileGroups,
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    force_serve_as: Union[Unset, GetFilesGroupFileNameForceServeAs] = UNSET,
    best_fit_height: Union[Unset, float] = UNSET,
    best_fit_width: Union[Unset, float] = UNSET,
) -> Response[Union[Error400, File]]:
    """Serves the given file

     With proper Content-Type header

    Args:
        group (FileGroups):
        file_name (str):
        force_serve_as (Union[Unset, GetFilesGroupFileNameForceServeAs]):
        best_fit_height (Union[Unset, float]):
        best_fit_width (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error400, File]]
    """

    kwargs = _get_kwargs(
        group=group,
        file_name=file_name,
        force_serve_as=force_serve_as,
        best_fit_height=best_fit_height,
        best_fit_width=best_fit_width,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group: FileGroups,
    file_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    force_serve_as: Union[Unset, GetFilesGroupFileNameForceServeAs] = UNSET,
    best_fit_height: Union[Unset, float] = UNSET,
    best_fit_width: Union[Unset, float] = UNSET,
) -> Optional[Union[Error400, File]]:
    """Serves the given file

     With proper Content-Type header

    Args:
        group (FileGroups):
        file_name (str):
        force_serve_as (Union[Unset, GetFilesGroupFileNameForceServeAs]):
        best_fit_height (Union[Unset, float]):
        best_fit_width (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error400, File]
    """

    return (
        await asyncio_detailed(
            group=group,
            file_name=file_name,
            client=client,
            force_serve_as=force_serve_as,
            best_fit_height=best_fit_height,
            best_fit_width=best_fit_width,
        )
    ).parsed
