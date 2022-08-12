# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models
from ._configuration import NetworkManagementClientConfiguration
from .operations import ApplicationGatewaysOperations, BgpServiceCommunitiesOperations, ExpressRouteCircuitAuthorizationsOperations, ExpressRouteCircuitPeeringsOperations, ExpressRouteCircuitsOperations, ExpressRouteServiceProvidersOperations, LoadBalancersOperations, LocalNetworkGatewaysOperations, NetworkInterfacesOperations, NetworkManagementClientOperationsMixin, NetworkSecurityGroupsOperations, NetworkWatchersOperations, PacketCapturesOperations, PublicIPAddressesOperations, RouteFilterRulesOperations, RouteFiltersOperations, RouteTablesOperations, RoutesOperations, SecurityRulesOperations, SubnetsOperations, UsagesOperations, VirtualNetworkGatewayConnectionsOperations, VirtualNetworkGatewaysOperations, VirtualNetworkPeeringsOperations, VirtualNetworksOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class NetworkManagementClient(NetworkManagementClientOperationsMixin):    # pylint: disable=too-many-instance-attributes
    """Network Client.

    :ivar network_interfaces: NetworkInterfacesOperations operations
    :vartype network_interfaces:
     azure.mgmt.network.v2016_12_01.aio.operations.NetworkInterfacesOperations
    :ivar application_gateways: ApplicationGatewaysOperations operations
    :vartype application_gateways:
     azure.mgmt.network.v2016_12_01.aio.operations.ApplicationGatewaysOperations
    :ivar express_route_circuit_authorizations: ExpressRouteCircuitAuthorizationsOperations
     operations
    :vartype express_route_circuit_authorizations:
     azure.mgmt.network.v2016_12_01.aio.operations.ExpressRouteCircuitAuthorizationsOperations
    :ivar express_route_circuit_peerings: ExpressRouteCircuitPeeringsOperations operations
    :vartype express_route_circuit_peerings:
     azure.mgmt.network.v2016_12_01.aio.operations.ExpressRouteCircuitPeeringsOperations
    :ivar express_route_circuits: ExpressRouteCircuitsOperations operations
    :vartype express_route_circuits:
     azure.mgmt.network.v2016_12_01.aio.operations.ExpressRouteCircuitsOperations
    :ivar express_route_service_providers: ExpressRouteServiceProvidersOperations operations
    :vartype express_route_service_providers:
     azure.mgmt.network.v2016_12_01.aio.operations.ExpressRouteServiceProvidersOperations
    :ivar load_balancers: LoadBalancersOperations operations
    :vartype load_balancers: azure.mgmt.network.v2016_12_01.aio.operations.LoadBalancersOperations
    :ivar network_security_groups: NetworkSecurityGroupsOperations operations
    :vartype network_security_groups:
     azure.mgmt.network.v2016_12_01.aio.operations.NetworkSecurityGroupsOperations
    :ivar security_rules: SecurityRulesOperations operations
    :vartype security_rules: azure.mgmt.network.v2016_12_01.aio.operations.SecurityRulesOperations
    :ivar network_watchers: NetworkWatchersOperations operations
    :vartype network_watchers:
     azure.mgmt.network.v2016_12_01.aio.operations.NetworkWatchersOperations
    :ivar packet_captures: PacketCapturesOperations operations
    :vartype packet_captures:
     azure.mgmt.network.v2016_12_01.aio.operations.PacketCapturesOperations
    :ivar public_ip_addresses: PublicIPAddressesOperations operations
    :vartype public_ip_addresses:
     azure.mgmt.network.v2016_12_01.aio.operations.PublicIPAddressesOperations
    :ivar route_filters: RouteFiltersOperations operations
    :vartype route_filters: azure.mgmt.network.v2016_12_01.aio.operations.RouteFiltersOperations
    :ivar route_filter_rules: RouteFilterRulesOperations operations
    :vartype route_filter_rules:
     azure.mgmt.network.v2016_12_01.aio.operations.RouteFilterRulesOperations
    :ivar route_tables: RouteTablesOperations operations
    :vartype route_tables: azure.mgmt.network.v2016_12_01.aio.operations.RouteTablesOperations
    :ivar routes: RoutesOperations operations
    :vartype routes: azure.mgmt.network.v2016_12_01.aio.operations.RoutesOperations
    :ivar bgp_service_communities: BgpServiceCommunitiesOperations operations
    :vartype bgp_service_communities:
     azure.mgmt.network.v2016_12_01.aio.operations.BgpServiceCommunitiesOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.network.v2016_12_01.aio.operations.UsagesOperations
    :ivar virtual_networks: VirtualNetworksOperations operations
    :vartype virtual_networks:
     azure.mgmt.network.v2016_12_01.aio.operations.VirtualNetworksOperations
    :ivar subnets: SubnetsOperations operations
    :vartype subnets: azure.mgmt.network.v2016_12_01.aio.operations.SubnetsOperations
    :ivar virtual_network_peerings: VirtualNetworkPeeringsOperations operations
    :vartype virtual_network_peerings:
     azure.mgmt.network.v2016_12_01.aio.operations.VirtualNetworkPeeringsOperations
    :ivar virtual_network_gateways: VirtualNetworkGatewaysOperations operations
    :vartype virtual_network_gateways:
     azure.mgmt.network.v2016_12_01.aio.operations.VirtualNetworkGatewaysOperations
    :ivar virtual_network_gateway_connections: VirtualNetworkGatewayConnectionsOperations
     operations
    :vartype virtual_network_gateway_connections:
     azure.mgmt.network.v2016_12_01.aio.operations.VirtualNetworkGatewayConnectionsOperations
    :ivar local_network_gateways: LocalNetworkGatewaysOperations operations
    :vartype local_network_gateways:
     azure.mgmt.network.v2016_12_01.aio.operations.LocalNetworkGatewaysOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft
     Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2016-12-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = NetworkManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.application_gateways = ApplicationGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuit_authorizations = ExpressRouteCircuitAuthorizationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuit_peerings = ExpressRouteCircuitPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_circuits = ExpressRouteCircuitsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.express_route_service_providers = ExpressRouteServiceProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.load_balancers = LoadBalancersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_security_groups = NetworkSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.security_rules = SecurityRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_watchers = NetworkWatchersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.packet_captures = PacketCapturesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.public_ip_addresses = PublicIPAddressesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.route_filters = RouteFiltersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.route_filter_rules = RouteFilterRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.route_tables = RouteTablesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.routes = RoutesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.bgp_service_communities = BgpServiceCommunitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_networks = VirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.subnets = SubnetsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_peerings = VirtualNetworkPeeringsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_gateways = VirtualNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.virtual_network_gateway_connections = VirtualNetworkGatewayConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.local_network_gateways = LocalNetworkGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "NetworkManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
