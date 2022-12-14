# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from azure.core.credentials import AccessToken
from azure.identity import AuthorizationCodeCredential

try:
    from unittest.mock import Mock
except ImportError:  # python < 3.3
    from mock import Mock  # type: ignore


def test_auth_code_credential():
    client_id = "client id"
    tenant_id = "tenant"
    expected_code = "auth code"
    redirect_uri = "https://foo.bar"
    expected_token = AccessToken("token", 42)

    mock_client = Mock(spec=object)
    mock_client.obtain_token_by_authorization_code = Mock(return_value=expected_token)

    credential = AuthorizationCodeCredential(
        client_id=client_id,
        tenant_id=tenant_id,
        authorization_code=expected_code,
        redirect_uri=redirect_uri,
        client=mock_client,
    )

    # first call should redeem the auth code
    token = credential.get_token("scope")
    assert token is expected_token
    assert mock_client.obtain_token_by_authorization_code.call_count == 1
    _, kwargs = mock_client.obtain_token_by_authorization_code.call_args
    assert kwargs["code"] == expected_code

    # no auth code -> credential should return cached token
    mock_client.obtain_token_by_authorization_code = None  # raise if credential calls this again
    mock_client.get_cached_access_token = lambda *_: expected_token
    token = credential.get_token("scope")
    assert token is expected_token

    # no auth code, no cached token -> credential should use refresh token
    mock_client.get_cached_access_token = lambda *_: None
    mock_client.get_cached_refresh_tokens = lambda *_: ["this is a refresh token"]
    mock_client.obtain_token_by_refresh_token = lambda *_, **__: expected_token
    token = credential.get_token("scope")
    assert token is expected_token
