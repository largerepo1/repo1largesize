# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import json
import os

from azure.identity import CertificateCredential
from six.moves.urllib_parse import urlparse
from helpers import urlsafeb64_decode, mock_response

try:
    from unittest.mock import Mock, patch
except ImportError:  # python < 3.3
    from mock import Mock, patch  # type: ignore

CERT_PATH = os.path.join(os.path.dirname(__file__), "certificate.pem")


def test_request_url():
    authority = "authority.com"
    tenant_id = "expected_tenant"
    access_token = "***"

    def validate_url(url):
        scheme, netloc, path, _, _, _ = urlparse(url)
        assert scheme == "https"
        assert netloc == authority
        assert path.startswith("/" + tenant_id)

    def mock_send(request, **kwargs):
        validate_url(request.url)
        return mock_response(json_payload={"token_type": "Bearer", "expires_in": 42, "access_token": access_token})

    cred = CertificateCredential(tenant_id, "client_id", CERT_PATH, transport=Mock(send=mock_send), authority=authority)
    token = cred.get_token("scope")
    assert token.token == access_token


def test_request_body():
    access_token = "***"
    authority = "authority.com"
    tenant_id = "tenant"

    def validate_url(url):
        scheme, netloc, path, _, _, _ = urlparse(url)
        assert scheme == "https"
        assert netloc == authority
        assert path.startswith("/" + tenant_id)

    def mock_send(request, **kwargs):
        jwt = request.body["client_assertion"]
        header, payload, signature = (urlsafeb64_decode(s) for s in jwt.split("."))
        claims = json.loads(payload.decode("utf-8"))
        validate_url(claims["aud"])
        return mock_response(json_payload={"token_type": "Bearer", "expires_in": 42, "access_token": access_token})

    cred = CertificateCredential(tenant_id, "client_id", CERT_PATH, transport=Mock(send=mock_send), authority=authority)
    token = cred.get_token("scope")
    assert token.token == access_token
