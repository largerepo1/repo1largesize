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
from msrestazure.azure_exceptions import CloudError

from .. import models


class FileSharesOperations(object):
    """FileSharesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2019-06-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-06-01"

        self.config = config

    def list(
            self, resource_group_name, account_name, maxpagesize=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists all shares.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param maxpagesize: Optional. Specified maximum number of shares that
         can be included in the list.
        :type maxpagesize: str
        :param filter: Optional. When specified, only share names starting
         with the filter will be listed.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of FileShareItem
        :rtype:
         ~azure.mgmt.storage.v2019_06_01.models.FileShareItemPaged[~azure.mgmt.storage.v2019_06_01.models.FileShareItem]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1)
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)
                if maxpagesize is not None:
                    query_parameters['$maxpagesize'] = self._serialize.query("maxpagesize", maxpagesize, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.FileShareItemPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares'}

    def create(
            self, resource_group_name, account_name, share_name, metadata=None, share_quota=None, custom_headers=None, raw=False, **operation_config):
        """Creates a new share under the specified account as described by request
        body. The share resource includes metadata and properties for that
        share. It does not include a list of the files contained by the share.
        .

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified
         storage account. File share names must be between 3 and 63 characters
         in length and use numbers, lower-case letters and dash (-) only. Every
         dash (-) character must be immediately preceded and followed by a
         letter or number.
        :type share_name: str
        :param metadata: A name-value pair to associate with the share as
         metadata.
        :type metadata: dict[str, str]
        :param share_quota: The maximum size of the share, in gigabytes. Must
         be greater than 0, and less than or equal to 5TB (5120).
        :type share_quota: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FileShare or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShare or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        file_share = models.FileShare(metadata=metadata, share_quota=share_quota)

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(file_share, 'FileShare')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FileShare', response)
        if response.status_code == 201:
            deserialized = self._deserialize('FileShare', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}

    def update(
            self, resource_group_name, account_name, share_name, metadata=None, share_quota=None, custom_headers=None, raw=False, **operation_config):
        """Updates share properties as specified in request body. Properties not
        mentioned in the request will not be changed. Update fails if the
        specified share does not already exist. .

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified
         storage account. File share names must be between 3 and 63 characters
         in length and use numbers, lower-case letters and dash (-) only. Every
         dash (-) character must be immediately preceded and followed by a
         letter or number.
        :type share_name: str
        :param metadata: A name-value pair to associate with the share as
         metadata.
        :type metadata: dict[str, str]
        :param share_quota: The maximum size of the share, in gigabytes. Must
         be greater than 0, and less than or equal to 5TB (5120).
        :type share_quota: int
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FileShare or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShare or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        file_share = models.FileShare(metadata=metadata, share_quota=share_quota)

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(file_share, 'FileShare')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FileShare', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}

    def get(
            self, resource_group_name, account_name, share_name, custom_headers=None, raw=False, **operation_config):
        """Gets properties of a specified share.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified
         storage account. File share names must be between 3 and 63 characters
         in length and use numbers, lower-case letters and dash (-) only. Every
         dash (-) character must be immediately preceded and followed by a
         letter or number.
        :type share_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: FileShare or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.storage.v2019_06_01.models.FileShare or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('FileShare', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}

    def delete(
            self, resource_group_name, account_name, share_name, custom_headers=None, raw=False, **operation_config):
        """Deletes specified share under its account.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param share_name: The name of the file share within the specified
         storage account. File share names must be between 3 and 63 characters
         in length and use numbers, lower-case letters and dash (-) only. Every
         dash (-) character must be immediately preceded and followed by a
         letter or number.
        :type share_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'shareName': self._serialize.url("share_name", share_name, 'str', max_length=63, min_length=3),
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str', min_length=1)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 204]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName}'}
