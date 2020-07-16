#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Test
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
t = Test(client)


def test_get_testrun_test(reqmock):
    reqmock.get()


def test_get_testrun_tests(reqmock):
    reqmock.get()
