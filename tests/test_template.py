#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestSuite
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
ts = TestSuite(client)


def test_get_templates(reqmock):
    reqmock.get()
