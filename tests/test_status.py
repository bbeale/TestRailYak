#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Status
from lib.testrail import APIClient
from tests import BASEURL, reqmock


client = APIClient(BASEURL)
s = Status(client)


def test_get_statuses(reqmock):
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_statuses",
        status_code=200,
        text='''[
            {
                "color_bright": 12709313,
                "color_dark": 6667107,
                "color_medium": 9820525,
                "id": 1,
                "is_final": true,
                "is_system": true,
                "is_untested": false,
                "label": "Passed",
                "name": "passed"
            },
            {
                "color_bright": 16631751,
                "color_dark": 14250867,
                "color_medium": 15829135,
                "id": 5,
                "is_final": true,
                "is_system": true,
                "is_untested": false,
                "label": "Failed",
                "name": "failed"
            },
            {
                "color_bright": 13684944,
                "color_dark": 0,
                "color_medium": 10526880,
                "id": 6,
                "is_final": false,
                "is_system": false,
                "is_untested": false,
                "label": "Custom",
                "name": "custom_status1"
            }
        ]''')

    res = s.get_statuses()
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "color_bright" in res[0].keys()
    assert "color_dark" in res[0].keys()
    assert "color_medium" in res[0].keys()
    assert "id" in res[0].keys()
    assert "is_final" in res[0].keys()
    assert "is_system" in res[0].keys()
    assert "is_untested" in res[0].keys()
    assert "label" in res[0].keys()
    assert "name" in res[0].keys()
