# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode to create a new server.
    """

    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    GEO_RESTORE = "GeoRestore"
    REPLICA = "Replica"

class GeoRedundantBackup(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enable Geo-redundant or not for server backup.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an
    Azure Active Directory principal for the resource.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"

class InfrastructureEncryption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Add a second layer of encryption for your data using new encryption algorithm which gives
    additional data protection. Value is optional but if passed in, must be 'Disabled' or
    'Enabled'.
    """

    #: Default value for single layer of encryption for data at rest.
    ENABLED = "Enabled"
    #: Additional (2nd) layer of encryption for data at rest.
    DISABLED = "Disabled"

class MinimalTlsVersionEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enforce a minimal Tls version for the server.
    """

    TLS1_0 = "TLS1_0"
    TLS1_1 = "TLS1_1"
    TLS1_2 = "TLS1_2"
    TLS_ENFORCEMENT_DISABLED = "TLSEnforcementDisabled"

class OperationOrigin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation.
    """

    NOT_SPECIFIED = "NotSpecified"
    USER = "user"
    SYSTEM = "system"

class PrivateEndpointProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the private endpoint connection.
    """

    APPROVING = "Approving"
    READY = "Ready"
    DROPPING = "Dropping"
    FAILED = "Failed"
    REJECTING = "Rejecting"

class PrivateLinkServiceConnectionStateActionsRequire(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The actions required for private link service connection.
    """

    NONE = "None"

class PrivateLinkServiceConnectionStateStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private link service connection status.
    """

    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class PublicNetworkAccessEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether or not public network access is allowed for this server. Value is optional but if
    passed in, must be 'Enabled' or 'Disabled'
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class QueryPerformanceInsightResetDataResultState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates result of the operation.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

class SecurityAlertPolicyName(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    DEFAULT = "Default"

class ServerKeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The key type like 'AzureKeyVault'.
    """

    AZURE_KEY_VAULT = "AzureKeyVault"

class ServerSecurityAlertPolicyState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the state of the policy, whether it is enabled or disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A state of a server that is visible to user.
    """

    READY = "Ready"
    DROPPING = "Dropping"
    DISABLED = "Disabled"
    INACCESSIBLE = "Inaccessible"

class ServerVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of a server.
    """

    FIVE6 = "5.6"
    FIVE7 = "5.7"
    EIGHT0 = "8.0"

class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The tier of the particular SKU, e.g. Basic.
    """

    BASIC = "Basic"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"

class SslEnforcementEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enable ssl enforcement or not when connect to server.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class StorageAutogrow(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enable Storage Auto Grow.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class VirtualNetworkRuleState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Virtual Network Rule State
    """

    INITIALIZING = "Initializing"
    IN_PROGRESS = "InProgress"
    READY = "Ready"
    DELETING = "Deleting"
    UNKNOWN = "Unknown"
