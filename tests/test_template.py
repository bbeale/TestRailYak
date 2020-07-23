#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Template
from lib.testrail import APIClient
from tests import BASEURL, reqmock


client = APIClient(BASEURL)
t = Template(client)


def test_get_templates(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_templates/{project_id}",
        status_code=200,
        text='''[
            {
                "id": 1,
                "is_default": true,
                "name": "Test Case (Text)"
            },
            {
                "id": 2,
                "is_default": false,
                "name": "Test Case (Steps)"
            },
            {
                "id": 3,
                "is_default": false,
                "name": "Exploratory Session"
            }
        ]''')

    res = t.get_templates(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "id" in res[0].keys()
    assert "is_default" in res[0].keys()
    assert "name" in res[0].keys()
