# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActiveDirectoryStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the Active Directory
    """

    #: Active Directory created but not in use.
    CREATED = "Created"
    #: Active Directory in use by SMB Volume.
    IN_USE = "InUse"
    #: Active Directory Deleted.
    DELETED = "Deleted"
    #: Error with the Active Directory.
    ERROR = "Error"
    #: Active Directory Updating.
    UPDATING = "Updating"

class ApplicationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Application Type
    """

    SAP_HANA = "SAP-HANA"

class AvsDataStore(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies whether the volume is enabled for Azure VMware Solution (AVS) datastore purpose
    """

    #: avsDataStore is enabled.
    ENABLED = "Enabled"
    #: avsDataStore is disabled.
    DISABLED = "Disabled"

class BackupType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of backup Manual or Scheduled
    """

    #: Manual backup.
    MANUAL = "Manual"
    #: Scheduled backup.
    SCHEDULED = "Scheduled"

class CheckNameResourceTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Resource type used for verification.
    """

    MICROSOFT_NET_APP_NET_APP_ACCOUNTS = "Microsoft.NetApp/netAppAccounts"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS = "Microsoft.NetApp/netAppAccounts/capacityPools"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES_SNAPSHOTS = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots"

class CheckQuotaNameResourceTypes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Resource type used for verification.
    """

    MICROSOFT_NET_APP_NET_APP_ACCOUNTS = "Microsoft.NetApp/netAppAccounts"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS = "Microsoft.NetApp/netAppAccounts/capacityPools"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes"
    MICROSOFT_NET_APP_NET_APP_ACCOUNTS_CAPACITY_POOLS_VOLUMES_SNAPSHOTS = "Microsoft.NetApp/netAppAccounts/capacityPools/volumes/snapshots"

class ChownMode(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """This parameter specifies who is authorized to change the ownership of a file. restricted - Only
    root user can change the ownership of the file. unrestricted - Non-root users can change
    ownership of files that they own.
    """

    RESTRICTED = "Restricted"
    UNRESTRICTED = "Unrestricted"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class EnableSubvolumes(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Flag indicating whether subvolume operations are enabled on the volume
    """

    #: subvolumes are enabled.
    ENABLED = "Enabled"
    #: subvolumes are not enabled.
    DISABLED = "Disabled"

class EncryptionKeySource(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Source of key used to encrypt data in volume. Possible values (case-insensitive) are:
    'Microsoft.NetApp'
    """

    #: Microsoft-managed key encryption.
    MICROSOFT_NET_APP = "Microsoft.NetApp"

class EncryptionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Encryption type of the capacity pool, set encryption type for data at rest for this pool and
    all volumes in it. This value can only be set when creating new pool.
    """

    #: EncryptionType Single, volumes will use single encryption at rest.
    SINGLE = "Single"
    #: EncryptionType Double, volumes will use double encryption at rest.
    DOUBLE = "Double"

class EndpointType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether the local volume is the source or destination for the Volume Replication
    """

    SRC = "src"
    DST = "dst"

class InAvailabilityReasonType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """:code:`<code>Invalid</code>` indicates the name provided does not match Azure App Service
    naming requirements. :code:`<code>AlreadyExists</code>` indicates that the name is already in
    use and is therefore unavailable.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class MetricAggregationType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    AVERAGE = "Average"

class MirrorState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the replication
    """

    UNINITIALIZED = "Uninitialized"
    MIRRORED = "Mirrored"
    BROKEN = "Broken"

class NetworkFeatures(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Basic network, or Standard features available to the volume.
    """

    #: Basic network feature.
    BASIC = "Basic"
    #: Standard network feature.
    STANDARD = "Standard"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the status of the VolumeQuotaRule at the time the operation was called.
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    PATCHING = "Patching"
    DELETING = "Deleting"
    MOVING = "Moving"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"

class QosType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The qos type of the pool
    """

    #: qos type Auto.
    AUTO = "Auto"
    #: qos type Manual.
    MANUAL = "Manual"

class RelationshipStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the mirror relationship
    """

    IDLE = "Idle"
    TRANSFERRING = "Transferring"

class ReplicationSchedule(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Schedule
    """

    _10_MINUTELY = "_10minutely"
    HOURLY = "hourly"
    DAILY = "daily"

class SecurityStyle(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol
    """

    NTFS = "ntfs"
    UNIX = "unix"

class ServiceLevel(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The service level of the file system
    """

    #: Standard service level.
    STANDARD = "Standard"
    #: Premium service level.
    PREMIUM = "Premium"
    #: Ultra service level.
    ULTRA = "Ultra"
    #: Zone redundant storage service level.
    STANDARD_ZRS = "StandardZRS"

class Type(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Type of quota
    """

    #: Default user quota.
    DEFAULT_USER_QUOTA = "DefaultUserQuota"
    #: Default group quota.
    DEFAULT_GROUP_QUOTA = "DefaultGroupQuota"
    #: Individual user quota.
    INDIVIDUAL_USER_QUOTA = "IndividualUserQuota"
    #: Individual group quota.
    INDIVIDUAL_GROUP_QUOTA = "IndividualGroupQuota"

class VolumeStorageToNetworkProximity(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provides storage to network proximity information for the volume.
    """

    #: Basic storage to network connectivity.
    DEFAULT = "Default"
    #: Standard T1 storage to network connectivity.
    T1 = "T1"
    #: Standard T2 storage to network connectivity.
    T2 = "T2"
