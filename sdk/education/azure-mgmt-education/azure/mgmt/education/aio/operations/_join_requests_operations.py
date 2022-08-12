# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._join_requests_operations import build_approve_request, build_deny_request, build_get_request, build_list_request
from .._vendor import MixinABC
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class JoinRequestsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.education.aio.EducationManagementClient`'s
        :attr:`join_requests` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        include_denied: Optional[bool] = None,
        **kwargs: Any
    ) -> AsyncIterable[_models.JoinRequestList]:
        """get student join requests.

        :param billing_account_name: Billing account name.
        :type billing_account_name: str
        :param billing_profile_name: Billing profile name.
        :type billing_profile_name: str
        :param invoice_section_name: Invoice section name.
        :type invoice_section_name: str
        :param include_denied: Include denied. Default value is None.
        :type include_denied: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JoinRequestList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.education.models.JoinRequestList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-12-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JoinRequestList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    billing_account_name=billing_account_name,
                    billing_profile_name=billing_profile_name,
                    invoice_section_name=invoice_section_name,
                    api_version=api_version,
                    include_denied=include_denied,
                    template_url=self.list.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_request(
                    billing_account_name=billing_account_name,
                    billing_profile_name=billing_profile_name,
                    invoice_section_name=invoice_section_name,
                    api_version=api_version,
                    include_denied=include_denied,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JoinRequestList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Education/labs/default/joinRequests"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        join_request_name: str,
        **kwargs: Any
    ) -> _models.JoinRequestDetails:
        """get student join requests.

        :param billing_account_name: Billing account name.
        :type billing_account_name: str
        :param billing_profile_name: Billing profile name.
        :type billing_profile_name: str
        :param invoice_section_name: Invoice section name.
        :type invoice_section_name: str
        :param join_request_name: Join name.
        :type join_request_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JoinRequestDetails, or the result of cls(response)
        :rtype: ~azure.mgmt.education.models.JoinRequestDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-12-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.JoinRequestDetails]

        
        request = build_get_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            join_request_name=join_request_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('JoinRequestDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Education/labs/default/joinRequests/{joinRequestName}"}  # type: ignore


    @distributed_trace_async
    async def approve(  # pylint: disable=inconsistent-return-statements
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        join_request_name: str,
        **kwargs: Any
    ) -> None:
        """Approve student joining the redeemable lab.

        :param billing_account_name: Billing account name.
        :type billing_account_name: str
        :param billing_profile_name: Billing profile name.
        :type billing_profile_name: str
        :param invoice_section_name: Invoice section name.
        :type invoice_section_name: str
        :param join_request_name: Join name.
        :type join_request_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-12-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_approve_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            join_request_name=join_request_name,
            api_version=api_version,
            template_url=self.approve.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    approve.metadata = {'url': "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Education/labs/default/joinRequests/{joinRequestName}/approve"}  # type: ignore


    @distributed_trace_async
    async def deny(  # pylint: disable=inconsistent-return-statements
        self,
        billing_account_name: str,
        billing_profile_name: str,
        invoice_section_name: str,
        join_request_name: str,
        **kwargs: Any
    ) -> None:
        """Deny student joining the redeemable lab.

        :param billing_account_name: Billing account name.
        :type billing_account_name: str
        :param billing_profile_name: Billing profile name.
        :type billing_profile_name: str
        :param invoice_section_name: Invoice section name.
        :type invoice_section_name: str
        :param join_request_name: Join name.
        :type join_request_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-12-01-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_deny_request(
            billing_account_name=billing_account_name,
            billing_profile_name=billing_profile_name,
            invoice_section_name=invoice_section_name,
            join_request_name=join_request_name,
            api_version=api_version,
            template_url=self.deny.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseBody, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    deny.metadata = {'url': "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Education/labs/default/joinRequests/{joinRequestName}/deny"}  # type: ignore

