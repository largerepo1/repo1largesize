# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ComputeNodeExtensionOperations(object):
    """ComputeNodeExtensionOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for the request. Constant value: "2022-03-01.16.0".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2022-03-01.16.0"

        self.config = config

    def get(
            self, pool_id, node_id, extension_name, compute_node_extension_get_options=None, custom_headers=None, raw=False, **operation_config):
        """Gets information about the specified Compute Node Extension.

        :param pool_id: The ID of the Pool that contains the Compute Node.
        :type pool_id: str
        :param node_id: The ID of the Compute Node that contains the
         extensions.
        :type node_id: str
        :param extension_name: The name of the of the Compute Node Extension
         that you want to get information about.
        :type extension_name: str
        :param compute_node_extension_get_options: Additional parameters for
         the operation
        :type compute_node_extension_get_options:
         ~azure.batch.models.ComputeNodeExtensionGetOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: NodeVMExtension or ClientRawResponse if raw=true
        :rtype: ~azure.batch.models.NodeVMExtension or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        select = None
        if compute_node_extension_get_options is not None:
            select = compute_node_extension_get_options.select
        timeout = None
        if compute_node_extension_get_options is not None:
            timeout = compute_node_extension_get_options.timeout
        client_request_id = None
        if compute_node_extension_get_options is not None:
            client_request_id = compute_node_extension_get_options.client_request_id
        return_client_request_id = None
        if compute_node_extension_get_options is not None:
            return_client_request_id = compute_node_extension_get_options.return_client_request_id
        ocp_date = None
        if compute_node_extension_get_options is not None:
            ocp_date = compute_node_extension_get_options.ocp_date

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True),
            'poolId': self._serialize.url("pool_id", pool_id, 'str'),
            'nodeId': self._serialize.url("node_id", node_id, 'str'),
            'extensionName': self._serialize.url("extension_name", extension_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if client_request_id is not None:
            header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
        if return_client_request_id is not None:
            header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
        if ocp_date is not None:
            header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.BatchErrorException(self._deserialize, response)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('NodeVMExtension', response)
            header_dict = {
                'client-request-id': 'str',
                'request-id': 'str',
                'ETag': 'str',
                'Last-Modified': 'rfc-1123',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/pools/{poolId}/nodes/{nodeId}/extensions/{extensionName}'}

    def list(
            self, pool_id, node_id, compute_node_extension_list_options=None, custom_headers=None, raw=False, **operation_config):
        """Lists the Compute Nodes Extensions in the specified Pool.

        :param pool_id: The ID of the Pool that contains Compute Node.
        :type pool_id: str
        :param node_id: The ID of the Compute Node that you want to list
         extensions.
        :type node_id: str
        :param compute_node_extension_list_options: Additional parameters for
         the operation
        :type compute_node_extension_list_options:
         ~azure.batch.models.ComputeNodeExtensionListOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of NodeVMExtension
        :rtype:
         ~azure.batch.models.NodeVMExtensionPaged[~azure.batch.models.NodeVMExtension]
        :raises:
         :class:`BatchErrorException<azure.batch.models.BatchErrorException>`
        """
        select = None
        if compute_node_extension_list_options is not None:
            select = compute_node_extension_list_options.select
        max_results = None
        if compute_node_extension_list_options is not None:
            max_results = compute_node_extension_list_options.max_results
        timeout = None
        if compute_node_extension_list_options is not None:
            timeout = compute_node_extension_list_options.timeout
        client_request_id = None
        if compute_node_extension_list_options is not None:
            client_request_id = compute_node_extension_list_options.client_request_id
        return_client_request_id = None
        if compute_node_extension_list_options is not None:
            return_client_request_id = compute_node_extension_list_options.return_client_request_id
        ocp_date = None
        if compute_node_extension_list_options is not None:
            ocp_date = compute_node_extension_list_options.ocp_date

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'batchUrl': self._serialize.url("self.config.batch_url", self.config.batch_url, 'str', skip_quote=True),
                    'poolId': self._serialize.url("pool_id", pool_id, 'str'),
                    'nodeId': self._serialize.url("node_id", node_id, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, 'str')
                if max_results is not None:
                    query_parameters['maxresults'] = self._serialize.query("max_results", max_results, 'int', maximum=1000, minimum=1)
                if timeout is not None:
                    query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if return_client_request_id is not None:
                header_parameters['return-client-request-id'] = self._serialize.header("return_client_request_id", return_client_request_id, 'bool')
            if ocp_date is not None:
                header_parameters['ocp-date'] = self._serialize.header("ocp_date", ocp_date, 'rfc-1123')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.BatchErrorException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.NodeVMExtensionPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/pools/{poolId}/nodes/{nodeId}/extensions'}
