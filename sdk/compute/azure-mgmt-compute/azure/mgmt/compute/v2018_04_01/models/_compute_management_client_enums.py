# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):

    NONE = "None"
    READ = "Read"

class CachingTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the caching requirements. :code:`<br>`:code:`<br>` Possible values are:
    :code:`<br>`:code:`<br>` **None** :code:`<br>`:code:`<br>` **ReadOnly**
    :code:`<br>`:code:`<br>` **ReadWrite** :code:`<br>`:code:`<br>` Default: **None for Standard
    storage. ReadOnly for Premium storage**
    """

    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"

class DiskCreateOption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This enumerates the possible sources of a disk's creation.
    """

    EMPTY = "Empty"
    ATTACH = "Attach"
    FROM_IMAGE = "FromImage"
    IMPORT_ENUM = "Import"
    COPY = "Copy"
    RESTORE = "Restore"

class DiskCreateOptionTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies how the virtual machine should be created.:code:`<br>`:code:`<br>` Possible values
    are::code:`<br>`:code:`<br>` **Attach** \u2013 This value is used when you are using a
    specialized disk to create the virtual machine.:code:`<br>`:code:`<br>` **FromImage** \u2013
    This value is used when you are using an image to create the virtual machine. If you are using
    a platform image, you also use the imageReference element described above. If you are using a
    marketplace image, you  also use the plan element previously described.
    """

    FROM_IMAGE = "FromImage"
    EMPTY = "Empty"
    ATTACH = "Attach"

class IntervalInMins(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Interval value in minutes used to create LogAnalytics call rate logs.
    """

    THREE_MINS = "ThreeMins"
    FIVE_MINS = "FiveMins"
    THIRTY_MINS = "ThirtyMins"
    SIXTY_MINS = "SixtyMins"

class IPVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Available from Api-Version 2017-03-30 onwards, it represents whether the specific
    ipconfiguration is IPv4 or IPv6. Default is taken as IPv4.  Possible values are: 'IPv4' and
    'IPv6'.
    """

    I_PV4 = "IPv4"
    I_PV6 = "IPv6"

class MaintenanceOperationResultCodeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Last Maintenance Operation Result Code.
    """

    NONE = "None"
    RETRY_LATER = "RetryLater"
    MAINTENANCE_ABORTED = "MaintenanceAborted"
    MAINTENANCE_COMPLETED = "MaintenanceCompleted"

class OperatingSystemStateTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The OS State.
    """

    GENERALIZED = "Generalized"
    SPECIALIZED = "Specialized"

class OperatingSystemTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operating system of the osDiskImage.
    """

    WINDOWS = "Windows"
    LINUX = "Linux"

class ProtocolTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the protocol of listener. :code:`<br>`:code:`<br>` Possible values are: :code:`<br>`\
    **http** :code:`<br>`:code:`<br>` **https**
    """

    HTTP = "Http"
    HTTPS = "Https"

class ProximityPlacementGroupType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the type of the proximity placement group. :code:`<br>`:code:`<br>` Possible values
    are: :code:`<br>`:code:`<br>` **Standard** : Co-locate resources within an Azure region or
    Availability Zone. :code:`<br>`:code:`<br>` **Ultra** : For future use.
    """

    STANDARD = "Standard"
    ULTRA = "Ultra"

class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the virtual machine. The type 'SystemAssigned, UserAssigned'
    includes both an implicitly created identity and a set of user assigned identities. The type
    'None' will remove any identities from the virtual machine.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"

class RollingUpgradeActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The last action performed on the rolling upgrade.
    """

    START = "Start"
    CANCEL = "Cancel"

class RollingUpgradeStatusCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Code indicating the current status of the upgrade.
    """

    ROLLING_FORWARD = "RollingForward"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    FAULTED = "Faulted"

class SettingNames(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the name of the setting to which the content applies. Possible values are:
    FirstLogonCommands and AutoLogon.
    """

    AUTO_LOGON = "AutoLogon"
    FIRST_LOGON_COMMANDS = "FirstLogonCommands"

class SnapshotStorageAccountTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The sku name.
    """

    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_ZRS = "Standard_ZRS"

class StatusLevelTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The level code.
    """

    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"

class StorageAccountTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the storage account type for the managed disk. Possible values are: Standard_LRS,
    Premium_LRS, and StandardSSD_LRS.
    """

    STANDARD_LRS = "Standard_LRS"
    PREMIUM_LRS = "Premium_LRS"
    STANDARD_SSD_LRS = "StandardSSD_LRS"

class UpgradeMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the mode of an upgrade to virtual machines in the scale set.:code:`<br />`:code:`<br
    />` Possible values are::code:`<br />`:code:`<br />` **Manual** - You  control the application
    of updates to virtual machines in the scale set. You do this by using the manualUpgrade
    action.:code:`<br />`:code:`<br />` **Automatic** - All virtual machines in the scale set are
    automatically updated at the same time.
    """

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    ROLLING = "Rolling"

class UpgradeOperationInvoker(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Invoker of the Upgrade Operation
    """

    UNKNOWN = "Unknown"
    USER = "User"
    PLATFORM = "Platform"

class UpgradeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Code indicating the current status of the upgrade.
    """

    ROLLING_FORWARD = "RollingForward"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    FAULTED = "Faulted"

class VirtualMachineEvictionPolicyTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the eviction policy for virtual machines in a low priority scale set.
    :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
    """

    DEALLOCATE = "Deallocate"
    DELETE = "Delete"

class VirtualMachinePriorityTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the priority for the virtual machines in the scale set.
    :code:`<br>`:code:`<br>`Minimum api-version: 2017-10-30-preview
    """

    REGULAR = "Regular"
    LOW = "Low"

class VirtualMachineScaleSetSkuScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The scale type applicable to the sku.
    """

    AUTOMATIC = "Automatic"
    NONE = "None"

class VirtualMachineSizeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the size of the virtual machine. For more information about virtual machine sizes,
    see `Sizes for virtual machines
    <https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc=%2fazure%2fvirtual-machines%2fwindows%2ftoc.json>`_.
    :code:`<br>`:code:`<br>` The available VM sizes depend on region and availability set. For a
    list of available sizes use these APIs:  :code:`<br>`:code:`<br>` `List all available virtual
    machine sizes in an availability set
    <https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes in a region
    <https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list>`_
    :code:`<br>`:code:`<br>` `List all available virtual machine sizes for resizing
    <https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes>`_
    """

    BASIC_A0 = "Basic_A0"
    BASIC_A1 = "Basic_A1"
    BASIC_A2 = "Basic_A2"
    BASIC_A3 = "Basic_A3"
    BASIC_A4 = "Basic_A4"
    STANDARD_A0 = "Standard_A0"
    STANDARD_A1 = "Standard_A1"
    STANDARD_A2 = "Standard_A2"
    STANDARD_A3 = "Standard_A3"
    STANDARD_A4 = "Standard_A4"
    STANDARD_A5 = "Standard_A5"
    STANDARD_A6 = "Standard_A6"
    STANDARD_A7 = "Standard_A7"
    STANDARD_A8 = "Standard_A8"
    STANDARD_A9 = "Standard_A9"
    STANDARD_A10 = "Standard_A10"
    STANDARD_A11 = "Standard_A11"
    STANDARD_A1_V2 = "Standard_A1_v2"
    STANDARD_A2_V2 = "Standard_A2_v2"
    STANDARD_A4_V2 = "Standard_A4_v2"
    STANDARD_A8_V2 = "Standard_A8_v2"
    STANDARD_A2_M_V2 = "Standard_A2m_v2"
    STANDARD_A4_M_V2 = "Standard_A4m_v2"
    STANDARD_A8_M_V2 = "Standard_A8m_v2"
    STANDARD_B1_S = "Standard_B1s"
    STANDARD_B1_MS = "Standard_B1ms"
    STANDARD_B2_S = "Standard_B2s"
    STANDARD_B2_MS = "Standard_B2ms"
    STANDARD_B4_MS = "Standard_B4ms"
    STANDARD_B8_MS = "Standard_B8ms"
    STANDARD_D1 = "Standard_D1"
    STANDARD_D2 = "Standard_D2"
    STANDARD_D3 = "Standard_D3"
    STANDARD_D4 = "Standard_D4"
    STANDARD_D11 = "Standard_D11"
    STANDARD_D12 = "Standard_D12"
    STANDARD_D13 = "Standard_D13"
    STANDARD_D14 = "Standard_D14"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D2_V3 = "Standard_D2_v3"
    STANDARD_D4_V3 = "Standard_D4_v3"
    STANDARD_D8_V3 = "Standard_D8_v3"
    STANDARD_D16_V3 = "Standard_D16_v3"
    STANDARD_D32_V3 = "Standard_D32_v3"
    STANDARD_D64_V3 = "Standard_D64_v3"
    STANDARD_D2_S_V3 = "Standard_D2s_v3"
    STANDARD_D4_S_V3 = "Standard_D4s_v3"
    STANDARD_D8_S_V3 = "Standard_D8s_v3"
    STANDARD_D16_S_V3 = "Standard_D16s_v3"
    STANDARD_D32_S_V3 = "Standard_D32s_v3"
    STANDARD_D64_S_V3 = "Standard_D64s_v3"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D15_V2 = "Standard_D15_v2"
    STANDARD_DS1 = "Standard_DS1"
    STANDARD_DS2 = "Standard_DS2"
    STANDARD_DS3 = "Standard_DS3"
    STANDARD_DS4 = "Standard_DS4"
    STANDARD_DS11 = "Standard_DS11"
    STANDARD_DS12 = "Standard_DS12"
    STANDARD_DS13 = "Standard_DS13"
    STANDARD_DS14 = "Standard_DS14"
    STANDARD_DS1_V2 = "Standard_DS1_v2"
    STANDARD_DS2_V2 = "Standard_DS2_v2"
    STANDARD_DS3_V2 = "Standard_DS3_v2"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_DS11_V2 = "Standard_DS11_v2"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_DS13_4_V2 = "Standard_DS13-4_v2"
    STANDARD_DS13_2_V2 = "Standard_DS13-2_v2"
    STANDARD_DS14_8_V2 = "Standard_DS14-8_v2"
    STANDARD_DS14_4_V2 = "Standard_DS14-4_v2"
    STANDARD_E2_V3 = "Standard_E2_v3"
    STANDARD_E4_V3 = "Standard_E4_v3"
    STANDARD_E8_V3 = "Standard_E8_v3"
    STANDARD_E16_V3 = "Standard_E16_v3"
    STANDARD_E32_V3 = "Standard_E32_v3"
    STANDARD_E64_V3 = "Standard_E64_v3"
    STANDARD_E2_S_V3 = "Standard_E2s_v3"
    STANDARD_E4_S_V3 = "Standard_E4s_v3"
    STANDARD_E8_S_V3 = "Standard_E8s_v3"
    STANDARD_E16_S_V3 = "Standard_E16s_v3"
    STANDARD_E32_S_V3 = "Standard_E32s_v3"
    STANDARD_E64_S_V3 = "Standard_E64s_v3"
    STANDARD_E32_16_V3 = "Standard_E32-16_v3"
    STANDARD_E32_8_S_V3 = "Standard_E32-8s_v3"
    STANDARD_E64_32_S_V3 = "Standard_E64-32s_v3"
    STANDARD_E64_16_S_V3 = "Standard_E64-16s_v3"
    STANDARD_F1 = "Standard_F1"
    STANDARD_F2 = "Standard_F2"
    STANDARD_F4 = "Standard_F4"
    STANDARD_F8 = "Standard_F8"
    STANDARD_F16 = "Standard_F16"
    STANDARD_F1_S = "Standard_F1s"
    STANDARD_F2_S = "Standard_F2s"
    STANDARD_F4_S = "Standard_F4s"
    STANDARD_F8_S = "Standard_F8s"
    STANDARD_F16_S = "Standard_F16s"
    STANDARD_F2_S_V2 = "Standard_F2s_v2"
    STANDARD_F4_S_V2 = "Standard_F4s_v2"
    STANDARD_F8_S_V2 = "Standard_F8s_v2"
    STANDARD_F16_S_V2 = "Standard_F16s_v2"
    STANDARD_F32_S_V2 = "Standard_F32s_v2"
    STANDARD_F64_S_V2 = "Standard_F64s_v2"
    STANDARD_F72_S_V2 = "Standard_F72s_v2"
    STANDARD_G1 = "Standard_G1"
    STANDARD_G2 = "Standard_G2"
    STANDARD_G3 = "Standard_G3"
    STANDARD_G4 = "Standard_G4"
    STANDARD_G5 = "Standard_G5"
    STANDARD_GS1 = "Standard_GS1"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_GS4_8 = "Standard_GS4-8"
    STANDARD_GS4_4 = "Standard_GS4-4"
    STANDARD_GS5_16 = "Standard_GS5-16"
    STANDARD_GS5_8 = "Standard_GS5-8"
    STANDARD_H8 = "Standard_H8"
    STANDARD_H16 = "Standard_H16"
    STANDARD_H8_M = "Standard_H8m"
    STANDARD_H16_M = "Standard_H16m"
    STANDARD_H16_R = "Standard_H16r"
    STANDARD_H16_MR = "Standard_H16mr"
    STANDARD_L4_S = "Standard_L4s"
    STANDARD_L8_S = "Standard_L8s"
    STANDARD_L16_S = "Standard_L16s"
    STANDARD_L32_S = "Standard_L32s"
    STANDARD_M64_S = "Standard_M64s"
    STANDARD_M64_MS = "Standard_M64ms"
    STANDARD_M128_S = "Standard_M128s"
    STANDARD_M128_MS = "Standard_M128ms"
    STANDARD_M64_32_MS = "Standard_M64-32ms"
    STANDARD_M64_16_MS = "Standard_M64-16ms"
    STANDARD_M128_64_MS = "Standard_M128-64ms"
    STANDARD_M128_32_MS = "Standard_M128-32ms"
    STANDARD_NC6 = "Standard_NC6"
    STANDARD_NC12 = "Standard_NC12"
    STANDARD_NC24 = "Standard_NC24"
    STANDARD_NC24_R = "Standard_NC24r"
    STANDARD_NC6_S_V2 = "Standard_NC6s_v2"
    STANDARD_NC12_S_V2 = "Standard_NC12s_v2"
    STANDARD_NC24_S_V2 = "Standard_NC24s_v2"
    STANDARD_NC24_RS_V2 = "Standard_NC24rs_v2"
    STANDARD_NC6_S_V3 = "Standard_NC6s_v3"
    STANDARD_NC12_S_V3 = "Standard_NC12s_v3"
    STANDARD_NC24_S_V3 = "Standard_NC24s_v3"
    STANDARD_NC24_RS_V3 = "Standard_NC24rs_v3"
    STANDARD_ND6_S = "Standard_ND6s"
    STANDARD_ND12_S = "Standard_ND12s"
    STANDARD_ND24_S = "Standard_ND24s"
    STANDARD_ND24_RS = "Standard_ND24rs"
    STANDARD_NV6 = "Standard_NV6"
    STANDARD_NV12 = "Standard_NV12"
    STANDARD_NV24 = "Standard_NV24"
