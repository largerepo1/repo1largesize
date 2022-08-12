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
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._metrics_operations import build_list_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MetricsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~$(python-base-namespace).v2016_09_01.aio.MonitorManagementClient`'s
        :attr:`metrics` attribute.
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
        resource_uri: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable[_models.MetricCollection]:
        """Lists the metric values for a resource.

        :param resource_uri: The identifier of the resource.
        :type resource_uri: str
        :param filter: Reduces the set of data collected.:code:`<br>`The filter is optional. If present
         it must contain a list of metric names to retrieve of the form: *(name.value eq 'metricName'
         [or name.value eq 'metricName' or ...])*. Optionally, the filter can contain conditions for the
         following attributes *aggregationType*\ , *startTime*\ , *endTime*\ , and *timeGrain* of the
         form *attributeName operator value*. Where operator is one of *ne*\ , *eq*\ , *gt*\ ,
         *lt*.:code:`<br>`Several conditions can be combined with parentheses and logical operators,
         e.g: *and*\ , *or*.:code:`<br>`Some example filter expressions are::code:`<br>`-
         $filter=(name.value eq 'RunsSucceeded') and aggregationType eq 'Total' and startTime eq
         2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M',:code:`<br>`-
         $filter=(name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq
         'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq
         duration'PT1H',:code:`<br>`- $filter=(name.value eq 'ActionsCompleted' or name.value eq
         'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime
         eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq
         duration'PT1M'.:code:`<br>`:code:`<br>`\ **NOTE**\ : When a metrics query comes in with
         multiple metrics, but with no aggregation types defined, the service will pick the Primary
         aggregation type of the first metrics to be used as the default aggregation type for all the
         metrics. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MetricCollection or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~$(python-base-namespace).v2016_09_01.models.MetricCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2016-09-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.MetricCollection]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    resource_uri=resource_uri,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_request(
                    resource_uri=resource_uri,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("MetricCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/{resourceUri}/providers/microsoft.insights/metrics"}  # type: ignore
