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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import StorageCacheMgmtClientConfiguration
from .operations import Operations
from .operations import SkusOperations
from .operations import UsageModelsOperations
from .operations import CachesOperations
from .operations import StorageTargetsOperations
from . import models


class StorageCacheMgmtClient(SDKClient):
    """A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as "Storage Targets"). These operations allow you to manage caches.

    :ivar config: Configuration for client.
    :vartype config: StorageCacheMgmtClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storagecache.operations.Operations
    :ivar skus: Skus operations
    :vartype skus: azure.mgmt.storagecache.operations.SkusOperations
    :ivar usage_models: UsageModels operations
    :vartype usage_models: azure.mgmt.storagecache.operations.UsageModelsOperations
    :ivar caches: Caches operations
    :vartype caches: azure.mgmt.storagecache.operations.CachesOperations
    :ivar storage_targets: StorageTargets operations
    :vartype storage_targets: azure.mgmt.storagecache.operations.StorageTargetsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = StorageCacheMgmtClientConfiguration(credentials, subscription_id, base_url)
        super(StorageCacheMgmtClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-08-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usage_models = UsageModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.caches = CachesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_targets = StorageTargetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
