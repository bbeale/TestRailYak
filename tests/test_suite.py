#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestSuite
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
ts = TestSuite(client)


def test_get_test_suite(reqmock):
    reqmock.get()


def test_get_test_suites(reqmock):
    reqmock.get()


def test_add_test_suite(reqmock):
    reqmock.post()


def test_update_test_suite(reqmock):
    reqmock.post()


def test_delete_test_suite(reqmock):
    reqmock.post()
