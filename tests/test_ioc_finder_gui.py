#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from ioc_finder_gui import ioc_finder_gui


class IocFinderGuiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = ioc_finder_gui.app.test_client()

    def test_get_index(self):
        rv = self.app.get('/')
        self.assertIn('IOC Finder GUI', rv.data.decode())
        self.assertIn('GUI for the indicator of compromise project.', rv.data.decode())

    def test_ioc_find_1(self):
        rv = self.app.post('/find', data={'text': 'foo example.com bar'})
        assert rv.status_code == 200
        assert 'example.com' in rv.data.decode()
