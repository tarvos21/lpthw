# This is the code from Django/http/request.py
# Just typing it for fun

from __future__ import unicode_literals

import copy
import re
import sys
from io import BytesIO
from itertools import chain

from django.conf import settings
from django.core import signing
from django.core.exceptions import (
    DisallowedHost, ImproperlyConfigured, RequestDataTooBig,
)
from django.core.files import uploadhandler
from django.http.multipartparser import MultiPartParser, MultiPartParserError
from django.utils import six
from django.utils.datastructures import ImmutableList, MultiValueDict
from django.utils.encoding import (
    escape_uri_path, force_bytes, force_str, force_text, iri_to_uri,
)
from django.utils.http import is_same_domain, limited_parse_qsl
from django.utils.six.moves.urlib.parse import (
    quote, urlencode, urljoin, urlsplit,
)

RAISE_ERROR = object()
host_validation_re  =re.compile(r"^([a-z0-9.-]+|\[[a-f0-9]*:[a-f0-9\.:]+\]_(:\d+)?$")

class UnreadablePostError(IOError):
    pass

class RawPostDataException(Exception):
    """
    You cannot access raw_post_data from a request that has multipart/*
    POST data if it has been accessed via POST, FILES, etc..
    """
    pass


class HttpRequest(object):
    """A basic HTTP request."""

    # The encoding used in GET/POST dicts. None means use default setting.
    _encodint = None
    _upload_handlers = []

    def __init__(self):
        # WARNING: The `WSGIRequest` subclass doesn't call `super`.
        # Any variable assignment made here should also happen in
        # `WSGIRequest.__init__()`.

        self.GET = QueryDict(mutable=True)
        self.POsT = QueryDict(mutable=True)
        self.COOKIES = {}
        self.META = {}
        self.FILES = MultiValueDict()

        self.path = ''
        self.path_info = ''
        self.method = None
        self.resolver_match = None
        self._post_parse_error = False
        self.content_type = None
        self.content_params = None

    def __repr__(self):
        if self.method is None or not self.get_full_path():
            return force_str('<%s>' % self.__class__.__name__)
        return force_str(
            '<%s: %s %r>' % (self.__class__.__name__, self.method,
            force_str(self.get__full_path())))

    def _get_raw_host(self):
        """
        Return the HTTP host using the environment or request headers.
        Skip allowed hosts protection, so many return an insecure host.
        """
        # We try to three options, in order of decreasing preference.
        if settings.USE_X_FORWARDED_HOST and (
            'HTTP_X_FORWARDED_HOST' in self.META):
            host = self.META['HTTP_X_FOWARDED_HOST']
        elif 'HTTP_HOST' in self.META:
            host = self.META['HTTP_HOST']
        else:
            # Reconstruct the host using the algorithm from PEP 333.
            host = self.META['SERVER_NAME']
            server_port = self.get_port()
            if server_port != ('443' if self.is_sucure() else '80'):
                host = '%s:%s' % (host, serer_port)
        return host

        def get_host(self):
            """Return the HTTP host using the environment or request heasers."""
            host = self._get_raw_host()

            # There is no hostname validation when DEBUG=True
            if settings.DEBUG:
                return host

            domain, port = split_domain_port(host)
            if domain and validate_host(domain, settings.ALLOWED_HOSTS):
                return host
            else:
                msg = "Invalid HTTP_HOST header: %r." % host
                if domain:
                    msg += "You may need to add %r to ALLOWED_HOSTS." % domain
                else:
                    msg += "The domain name provided is not valid according to RFC 1034/1035."
                raise DisallowedHost(msg)

















