# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import Operations
from ._availability_sets_operations import AvailabilitySetsOperations
from ._proximity_placement_groups_operations import ProximityPlacementGroupsOperations
from ._dedicated_host_groups_operations import DedicatedHostGroupsOperations
from ._dedicated_hosts_operations import DedicatedHostsOperations
from ._ssh_public_keys_operations import SshPublicKeysOperations
from ._virtual_machine_extension_images_operations import VirtualMachineExtensionImagesOperations
from ._virtual_machine_extensions_operations import VirtualMachineExtensionsOperations
from ._virtual_machine_images_operations import VirtualMachineImagesOperations
from ._virtual_machine_images_edge_zone_operations import VirtualMachineImagesEdgeZoneOperations
from ._usage_operations import UsageOperations
from ._virtual_machines_operations import VirtualMachinesOperations
from ._virtual_machine_scale_sets_operations import VirtualMachineScaleSetsOperations
from ._virtual_machine_sizes_operations import VirtualMachineSizesOperations
from ._images_operations import ImagesOperations
from ._restore_point_collections_operations import RestorePointCollectionsOperations
from ._restore_points_operations import RestorePointsOperations
from ._capacity_reservation_groups_operations import CapacityReservationGroupsOperations
from ._capacity_reservations_operations import CapacityReservationsOperations
from ._virtual_machine_scale_set_extensions_operations import VirtualMachineScaleSetExtensionsOperations
from ._virtual_machine_scale_set_rolling_upgrades_operations import VirtualMachineScaleSetRollingUpgradesOperations
from ._virtual_machine_scale_set_vm_extensions_operations import VirtualMachineScaleSetVMExtensionsOperations
from ._virtual_machine_scale_set_vms_operations import VirtualMachineScaleSetVMsOperations
from ._log_analytics_operations import LogAnalyticsOperations
from ._virtual_machine_run_commands_operations import VirtualMachineRunCommandsOperations
from ._virtual_machine_scale_set_vm_run_commands_operations import VirtualMachineScaleSetVMRunCommandsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'Operations',
    'AvailabilitySetsOperations',
    'ProximityPlacementGroupsOperations',
    'DedicatedHostGroupsOperations',
    'DedicatedHostsOperations',
    'SshPublicKeysOperations',
    'VirtualMachineExtensionImagesOperations',
    'VirtualMachineExtensionsOperations',
    'VirtualMachineImagesOperations',
    'VirtualMachineImagesEdgeZoneOperations',
    'UsageOperations',
    'VirtualMachinesOperations',
    'VirtualMachineScaleSetsOperations',
    'VirtualMachineSizesOperations',
    'ImagesOperations',
    'RestorePointCollectionsOperations',
    'RestorePointsOperations',
    'CapacityReservationGroupsOperations',
    'CapacityReservationsOperations',
    'VirtualMachineScaleSetExtensionsOperations',
    'VirtualMachineScaleSetRollingUpgradesOperations',
    'VirtualMachineScaleSetVMExtensionsOperations',
    'VirtualMachineScaleSetVMsOperations',
    'LogAnalyticsOperations',
    'VirtualMachineRunCommandsOperations',
    'VirtualMachineScaleSetVMRunCommandsOperations',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()