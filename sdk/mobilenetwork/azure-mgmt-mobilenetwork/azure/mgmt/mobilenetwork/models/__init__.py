# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import Ambr
from ._models_py3 import Arp
from ._models_py3 import AttachedDataNetwork
from ._models_py3 import AttachedDataNetworkListResult
from ._models_py3 import AttachedDataNetworkResourceId
from ._models_py3 import AzureStackEdgeDeviceResourceId
from ._models_py3 import ConnectedClusterResourceId
from ._models_py3 import CustomLocationResourceId
from ._models_py3 import DataNetwork
from ._models_py3 import DataNetworkConfiguration
from ._models_py3 import DataNetworkListResult
from ._models_py3 import DataNetworkResourceId
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import InterfaceProperties
from ._models_py3 import KeyVaultCertificate
from ._models_py3 import KeyVaultKey
from ._models_py3 import LocalDiagnosticsAccessConfiguration
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import MobileNetwork
from ._models_py3 import MobileNetworkListResult
from ._models_py3 import MobileNetworkResourceId
from ._models_py3 import NaptConfiguration
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationList
from ._models_py3 import PacketCoreControlPlane
from ._models_py3 import PacketCoreControlPlaneListResult
from ._models_py3 import PacketCoreControlPlaneVersion
from ._models_py3 import PacketCoreControlPlaneVersionListResult
from ._models_py3 import PacketCoreDataPlane
from ._models_py3 import PacketCoreDataPlaneListResult
from ._models_py3 import PccRuleConfiguration
from ._models_py3 import PccRuleQosPolicy
from ._models_py3 import PinholeTimeouts
from ._models_py3 import PlatformConfiguration
from ._models_py3 import PlmnId
from ._models_py3 import PortRange
from ._models_py3 import PortReuseHoldTimes
from ._models_py3 import ProxyResource
from ._models_py3 import QosPolicy
from ._models_py3 import Resource
from ._models_py3 import Service
from ._models_py3 import ServiceDataFlowTemplate
from ._models_py3 import ServiceListResult
from ._models_py3 import ServiceResourceId
from ._models_py3 import Sim
from ._models_py3 import SimGroup
from ._models_py3 import SimGroupListResult
from ._models_py3 import SimGroupResourceId
from ._models_py3 import SimIdListResult
from ._models_py3 import SimListResult
from ._models_py3 import SimPolicy
from ._models_py3 import SimPolicyListResult
from ._models_py3 import SimPolicyResourceId
from ._models_py3 import SimStaticIpProperties
from ._models_py3 import SimStaticIpPropertiesStaticIp
from ._models_py3 import Site
from ._models_py3 import SiteListResult
from ._models_py3 import Slice
from ._models_py3 import SliceConfiguration
from ._models_py3 import SliceListResult
from ._models_py3 import SliceResourceId
from ._models_py3 import Snssai
from ._models_py3 import SubResource
from ._models_py3 import SystemData
from ._models_py3 import TagsObject
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity


from ._mobile_network_management_client_enums import (
    BillingSku,
    CoreNetworkType,
    CreatedByType,
    ManagedServiceIdentityType,
    NaptEnabled,
    PduSessionType,
    PlatformType,
    PreemptionCapability,
    PreemptionVulnerability,
    ProvisioningState,
    RecommendedVersion,
    SdfDirection,
    SimState,
    TrafficControlPermission,
    VersionState,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'Ambr',
    'Arp',
    'AttachedDataNetwork',
    'AttachedDataNetworkListResult',
    'AttachedDataNetworkResourceId',
    'AzureStackEdgeDeviceResourceId',
    'ConnectedClusterResourceId',
    'CustomLocationResourceId',
    'DataNetwork',
    'DataNetworkConfiguration',
    'DataNetworkListResult',
    'DataNetworkResourceId',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'InterfaceProperties',
    'KeyVaultCertificate',
    'KeyVaultKey',
    'LocalDiagnosticsAccessConfiguration',
    'ManagedServiceIdentity',
    'MobileNetwork',
    'MobileNetworkListResult',
    'MobileNetworkResourceId',
    'NaptConfiguration',
    'Operation',
    'OperationDisplay',
    'OperationList',
    'PacketCoreControlPlane',
    'PacketCoreControlPlaneListResult',
    'PacketCoreControlPlaneVersion',
    'PacketCoreControlPlaneVersionListResult',
    'PacketCoreDataPlane',
    'PacketCoreDataPlaneListResult',
    'PccRuleConfiguration',
    'PccRuleQosPolicy',
    'PinholeTimeouts',
    'PlatformConfiguration',
    'PlmnId',
    'PortRange',
    'PortReuseHoldTimes',
    'ProxyResource',
    'QosPolicy',
    'Resource',
    'Service',
    'ServiceDataFlowTemplate',
    'ServiceListResult',
    'ServiceResourceId',
    'Sim',
    'SimGroup',
    'SimGroupListResult',
    'SimGroupResourceId',
    'SimIdListResult',
    'SimListResult',
    'SimPolicy',
    'SimPolicyListResult',
    'SimPolicyResourceId',
    'SimStaticIpProperties',
    'SimStaticIpPropertiesStaticIp',
    'Site',
    'SiteListResult',
    'Slice',
    'SliceConfiguration',
    'SliceListResult',
    'SliceResourceId',
    'Snssai',
    'SubResource',
    'SystemData',
    'TagsObject',
    'TrackedResource',
    'UserAssignedIdentity',
    'BillingSku',
    'CoreNetworkType',
    'CreatedByType',
    'ManagedServiceIdentityType',
    'NaptEnabled',
    'PduSessionType',
    'PlatformType',
    'PreemptionCapability',
    'PreemptionVulnerability',
    'ProvisioningState',
    'RecommendedVersion',
    'SdfDirection',
    'SimState',
    'TrafficControlPermission',
    'VersionState',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()