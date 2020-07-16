#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestResult
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
tr = TestResult(client)


def test_get_test_results(reqmock):
    reqmock.get()


def test_get_testcase_results(reqmock):
    reqmock.get()


def test_get_testrun_results(reqmock):
    reqmock.get()


def test_add_result(reqmock):
    reqmock.post()


def test_add_testcase_result(reqmock):
    reqmock.post()


def test_add_results(reqmock):
    reqmock.post()


def test_add_testcase_results(reqmock):
    reqmock.post()
