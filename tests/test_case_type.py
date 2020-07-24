#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import CaseType
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
ct = CaseType(client)


def test_get_case_types(reqmock):
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_case_types",
        status_code=200,
        text='''[{
                "id": 1,
                "is_default": false,
                "name": "Automated"
            },
            {
                "id": 2,
                "is_default": false,
                "name": "Functionality"
            }]''')

    res = ct.get_case_types()
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert res[0]["id"] == 1
    assert res[0]["is_default"] is False
    assert res[0]["name"] == "Automated"
