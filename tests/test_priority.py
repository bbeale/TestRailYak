#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Priority
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
p = Priority(client)


def test_get_priorities(reqmock):
    reqmock.get()
