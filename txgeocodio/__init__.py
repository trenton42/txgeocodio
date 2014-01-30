#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Trenton Broughton'
__email__ = 'trenton@kindrid.com'
__version__ = '0.1.0'

from txgeocodio.client import Client, AddressError
from txgeocodio.config import Config


def configure(api_key):
    _client.config = Config(api_key=api_key)

_client = Client(Config())

geocode = _client.geocode
parse = _client.parse

__all__ = ['geocode', 'parse', 'configure', 'AddressError']
