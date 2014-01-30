#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Geocache layer, using txmongo objects '''

from txmongoobject import model


class AddressCache(model.MongoObj):
    address = model.stringProperty()
    city = model.stringProperty()
    state = model.stringProperty()
    zip_ = model.stringProperty()
