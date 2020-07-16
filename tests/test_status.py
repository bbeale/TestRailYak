#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Status
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
s = Status(client)


def test_get_statuses(reqmock):
    reqmock.get()
