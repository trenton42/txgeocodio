#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):
    ''' Basic config object '''
    base_uri = 'http://api.geocod.io/v1/geocode'

    def __init__(self, api_key=None, base_uri=None):
        self.api_key = api_key
        if base_uri:
            self.base_uri = base_uri
