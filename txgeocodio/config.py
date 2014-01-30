#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):
    ''' Basic config object '''
    base_uri = 'http://api.geocod.io/v1/'

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.geocode_endpoint = self.url_join(self.base_uri, 'geocode')
        self.parse_endpoint = self.url_join(self.base_uri, 'parse')

    def url_join(self, *parts):
        ''' Join url parts that may or may not have slashes '''
        return '/'.join(map(lambda k: k.strip('/'), parts))
