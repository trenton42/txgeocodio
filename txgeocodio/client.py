#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Geocodio client '''

import treq
from twisted.internet import defer


class AddressError(Exception):
    pass


class Client(object):

    config = None

    def __init__(self, config=None):
        self.config = config

    @defer.inlineCallbacks
    def geocode(self, address):
        ''' Geocode a specific address '''
        if not self.config:
            raise AttributeError('Config not set')
        
        params = {'q': address, 'api_key': self.config.api_key}
        endpoint = self.config.geocode_endpoint
        result = yield treq.get(endpoint, params=params)
        content = yield treq.json_content(result)
        if 'error' in content:
            raise AddressError(content['error'])
        defer.returnValue(content['results'])

    @defer.inlineCallbacks
    def parse(self, address):
        ''' Parse an address into parts '''
        if not self.config:
            raise AttributeError('Config not set')
        
        params = {'q': address, 'api_key': self.config.api_key}
        endpoint = self.config.parse_endpoint
        result = yield treq.get(endpoint, params=params)
        content = yield treq.json_content(result)
        if 'error' in content:
            raise AddressError(content['error'])
        defer.returnValue(content)
