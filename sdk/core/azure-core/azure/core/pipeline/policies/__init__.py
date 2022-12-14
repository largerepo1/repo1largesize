# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from ._base import HTTPPolicy, SansIOHTTPPolicy, RequestHistory
from ._authentication import BearerTokenCredentialPolicy
from ._custom_hook import CustomHookPolicy
from ._redirect import RedirectPolicy
from ._retry import RetryPolicy
from ._distributed_tracing import DistributedTracingPolicy
from ._universal import (
    HeadersPolicy,
    UserAgentPolicy,
    NetworkTraceLoggingPolicy,
    ContentDecodePolicy,
    ProxyPolicy,
    HttpLoggingPolicy,
)

__all__ = [
    'HTTPPolicy',
    'SansIOHTTPPolicy',
    'BearerTokenCredentialPolicy',
    'HeadersPolicy',
    'UserAgentPolicy',
    'NetworkTraceLoggingPolicy',
    'ContentDecodePolicy',
    'RetryPolicy',
    'RedirectPolicy',
    'ProxyPolicy',
    'CustomHookPolicy',
    'DistributedTracingPolicy',
    'RequestHistory',
    'HttpLoggingPolicy',
]

#pylint: disable=unused-import

try:
    from ._base_async import AsyncHTTPPolicy
    from ._authentication_async import AsyncBearerTokenCredentialPolicy
    from ._redirect_async import AsyncRedirectPolicy
    from ._retry_async import AsyncRetryPolicy
    __all__.extend([
        'AsyncHTTPPolicy',
        'AsyncBearerTokenCredentialPolicy',
        'AsyncRedirectPolicy',
        'AsyncRetryPolicy'
    ])
except (ImportError, SyntaxError):
    pass  # Async not supported
