#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import ResultField
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
rf = ResultField(client)


def test_get_test_run(reqmock):
    reqmock.get()


def test_get_test_runs(reqmock):
    reqmock.get()


def test_add_test_run(reqmock):
    reqmock.post()


def test_update_test_run(reqmock):
    reqmock.post()


def test_close_test_run(reqmock):
    reqmock.post()


def test_delete_test_run(reqmock):
    reqmock.post()
