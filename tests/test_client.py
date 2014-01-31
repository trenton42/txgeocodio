#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_client
----------------------------------

Tests for `txgeocodio.client` module.
"""

import mock
import os
from twisted.trial import unittest

import txgeocodio.client as client
import txgeocodio.config as config
from twisted.internet import defer
from twisted.web.client import ResponseDone
from twisted.python.failure import Failure


class TestClient(unittest.TestCase):

    def _create_deferred(self, code=200, content=None):
        response = mock.Mock()
        response.code = code
        if not content:
            content = ''
        response.length = len(content)
        response.deliverBody = self._deliverBody(content)
        return defer.succeed(response)

    def _deliverBody(self, content):
        def deliverBody(bodyCollector):
            bodyCollector.dataReceived(content)
            bodyCollector.connectionLost(Failure(ResponseDone()))
        return deliverBody

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_withoutconfig(self):
        c = client.Client()
        self.assertFailure(c.geocode('12345'), AttributeError)
        self.assertFailure(c.batch(['12345']), AttributeError)
        self.assertFailure(c.parse('12345'), AttributeError)

    def test_geocodeError(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        return_content = '{"error": "Bad things happen"}'
        ret = self._create_deferred(content=return_content)
        patch_module = 'treq.client.HTTPClient.request'
        with mock.patch(patch_module, return_value=ret):
            response = c.geocode('12345')
            self.assertFailure(response, client.AddressError)
        return response

    def test_batchError(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        return_content = '{"error": "Bad things happen"}'
        ret = self._create_deferred(content=return_content)
        patch_module = 'treq.client.HTTPClient.request'
        with mock.patch(patch_module, return_value=ret):
            response = c.batch(['12345'])
            self.assertFailure(response, client.AddressError)
        return response

    def test_batchTypeError(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        return_content = '{"error": "Bad things happen"}'
        ret = self._create_deferred(content=return_content)
        patch_module = 'treq.client.HTTPClient.request'
        with mock.patch(patch_module, return_value=ret):
            response = c.batch('12345')
            self.assertFailure(response, TypeError)
        return response

    def test_parseError(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        ret = self._create_deferred(content='{"error": "Bad things happen"}')
        with mock.patch('treq.client.HTTPClient.request', return_value=ret, callable=mock.Mock):
            response = c.parse('12345')
            self.assertFailure(response, client.AddressError)
        return response

    @defer.inlineCallbacks
    def test_geocode(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        path = os.path.join(os.path.dirname(__file__), 'result.json')
        with open(path) as fp:
            result_data = fp.read()

        ret = self._create_deferred(content=result_data)
        patch_module = 'treq.client.HTTPClient.request'
        with mock.patch(patch_module, return_value=ret):
            response = yield c.geocode('42370 Bob Hope Drive, Rancho Mirage CA')
            self.assertIsInstance(response, list)
            self.assertEqual(len(response), 2)

    @defer.inlineCallbacks
    def test_parse(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        path = os.path.join(os.path.dirname(__file__), 'parse.json')
        with open(path) as fp:
            result_data = fp.read()

        ret = self._create_deferred(content=result_data)
        patch_module = 'treq.client.HTTPClient.request'
        with mock.patch(patch_module, return_value=ret):
            response = yield c.parse('42370 Bob Hope Drive, Rancho Mirage CA')
            self.assertIsInstance(response, dict)
            self.assertEqual(len(response.keys()), 2)
            self.assertIn('address_components', response)
            self.assertIn('formatted_address', response)

    @defer.inlineCallbacks
    def test_batch(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")
        c.config = cfg
        path = os.path.join(os.path.dirname(__file__), 'batch.json')
        with open(path) as fp:
            result_data = fp.read()

        ret = self._create_deferred(content=result_data)
        patch_module = 'treq.client.HTTPClient.request'
        request = ["42370 Bob Hope Drive, Rancho Mirage CA",
            "1290 Northbrook Court Mall, Northbrook IL",
            "4410 S Highway 17 92, Casselberry FL",
            "15000 NE 24th Street, Redmond WA",
            "17015 Walnut Grove Drive, Morgan Hill CA"]
        with mock.patch(patch_module, return_value=ret):
            response = yield c.batch(request)
            self.assertIsInstance(response, dict)
            self.assertEqual(len(response), len(request))
