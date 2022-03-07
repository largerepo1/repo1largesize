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

from msrest.paging import Paged


class ApplicationSummaryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationSummary <azure.batch.models.ApplicationSummary>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationSummary]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationSummaryPaged, self).__init__(*args, **kwargs)
class PoolUsageMetricsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PoolUsageMetrics <azure.batch.models.PoolUsageMetrics>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PoolUsageMetrics]'}
    }

    def __init__(self, *args, **kwargs):

        super(PoolUsageMetricsPaged, self).__init__(*args, **kwargs)
class PoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Pool <azure.batch.models.Pool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Pool]'}
    }

    def __init__(self, *args, **kwargs):

        super(PoolPaged, self).__init__(*args, **kwargs)
class ImageInformationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ImageInformation <azure.batch.models.ImageInformation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ImageInformation]'}
    }

    def __init__(self, *args, **kwargs):

        super(ImageInformationPaged, self).__init__(*args, **kwargs)
class PoolNodeCountsPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PoolNodeCounts <azure.batch.models.PoolNodeCounts>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PoolNodeCounts]'}
    }

    def __init__(self, *args, **kwargs):

        super(PoolNodeCountsPaged, self).__init__(*args, **kwargs)
class JobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Job <azure.batch.models.Job>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Job]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobPaged, self).__init__(*args, **kwargs)
class JobPreparationAndReleaseTaskExecutionInformationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobPreparationAndReleaseTaskExecutionInformation <azure.batch.models.JobPreparationAndReleaseTaskExecutionInformation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobPreparationAndReleaseTaskExecutionInformation]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobPreparationAndReleaseTaskExecutionInformationPaged, self).__init__(*args, **kwargs)
class CertificatePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Certificate <azure.batch.models.Certificate>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Certificate]'}
    }

    def __init__(self, *args, **kwargs):

        super(CertificatePaged, self).__init__(*args, **kwargs)
class NodeFilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`NodeFile <azure.batch.models.NodeFile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NodeFile]'}
    }

    def __init__(self, *args, **kwargs):

        super(NodeFilePaged, self).__init__(*args, **kwargs)
class JobSchedulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`JobSchedule <azure.batch.models.JobSchedule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[JobSchedule]'}
    }

    def __init__(self, *args, **kwargs):

        super(JobSchedulePaged, self).__init__(*args, **kwargs)
class TaskPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Task <azure.batch.models.Task>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Task]'}
    }

    def __init__(self, *args, **kwargs):

        super(TaskPaged, self).__init__(*args, **kwargs)
class ComputeNodePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ComputeNode <azure.batch.models.ComputeNode>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ComputeNode]'}
    }

    def __init__(self, *args, **kwargs):

        super(ComputeNodePaged, self).__init__(*args, **kwargs)
class NodeVMExtensionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NodeVMExtension <azure.batch.models.NodeVMExtension>` object
    """

    _attribute_map = {
        'next_link': {'key': 'odata\\.nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NodeVMExtension]'}
    }

    def __init__(self, *args, **kwargs):

        super(NodeVMExtensionPaged, self).__init__(*args, **kwargs)
