#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Report
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
p = Project(client)


def test_get_reports(reqmock):
    reqmock.get()


def test_run_report(reqmock):
    reqmock.post()
