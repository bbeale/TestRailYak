#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Priority
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
p = Priority(client)


def test_get_priorities(reqmock):
    reqmock.get("http://example.testrail.com/index.php?/api/v2/get_priorities",
        status_code=200,
        text='''[{
                "id": 1,
                "is_default": false,
                "name": "1 - Don't Test",
                "priority": 1,
                "short_name": "1 - Don't"
            }]''')
    res = p.get_priorities()
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "id" in res[0].keys()
    assert "is_default" in res[0].keys()
    assert "name" in res[0].keys()
    assert "priority" in res[0].keys()
    assert "short_name" in res[0].keys()
