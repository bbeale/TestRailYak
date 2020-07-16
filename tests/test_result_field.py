#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import ResultField
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
rf = ResultField(client)


def test_get_result_fields(reqmock):
    reqmock.get()
