#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_txgeocodio
----------------------------------

Tests for `txgeocodio` module.
"""

from twisted.trial import unittest

import txgeocodio


class TestTxgeocodio(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_configure(self):
        self.assertIdentical(txgeocodio._client.config.api_key, None)
        key = 'TESTAPIKEY'
        txgeocodio.configure(key)
        self.assertEqual(txgeocodio._client.config.api_key, key)
