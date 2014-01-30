#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_client
----------------------------------

Tests for `txgeocodio.client` module.
"""

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

    def test_geocode(self):
        c = client.Client()
        cfg = config.Config(api_key="TESTKEYTESTKEY")

    def test_parse(self):
        pass
