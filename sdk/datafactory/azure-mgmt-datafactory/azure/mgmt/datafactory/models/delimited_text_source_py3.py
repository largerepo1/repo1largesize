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

from .copy_source_py3 import CopySource


class DelimitedTextSource(CopySource):
    """A copy activity DelimitedText source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param store_settings: DelimitedText store settings.
    :type store_settings: ~azure.mgmt.datafactory.models.StoreReadSettings
    :param format_settings: DelimitedText format settings.
    :type format_settings:
     ~azure.mgmt.datafactory.models.DelimitedTextReadSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'store_settings': {'key': 'storeSettings', 'type': 'StoreReadSettings'},
        'format_settings': {'key': 'formatSettings', 'type': 'DelimitedTextReadSettings'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, store_settings=None, format_settings=None, **kwargs) -> None:
        super(DelimitedTextSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, **kwargs)
        self.store_settings = store_settings
        self.format_settings = format_settings
        self.type = 'DelimitedTextSource'
