#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Suite
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
s = Suite(client)


def test_get_test_suite(reqmock):
    suite_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_suite/{suite_id}",
        status_code=200,
        text='''{
            "description": "This is a test suite",
            "id": 1,
            "name": "Setup & Installation",
            "project_id": 1,
            "url": "http:///testrail/index.php?/suites/view/1"
        }''')

    res = s.get_test_suite(suite_id=suite_id)
    assert res is not None
    assert type(res) == dict
    assert "description" in res.keys()
    assert "id" in res.keys()
    assert "name" in res.keys()
    assert "project_id" in res.keys()
    assert "url" in res.keys()


def test_get_test_suites(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_suites/{project_id}",
        status_code=200,
        text='''[{
            "description": "This is a test suite",
            "id": 1,
            "name": "Setup & Installation",
            "project_id": 1,
            "url": "http:///testrail/index.php?/suites/view/1"
        }]''')

    res = s.get_test_suites(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add_test_suite(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_suite/{project_id}",
        status_code=200,
        text='''{
            "description": "This is a test suite",
            "id": 1,
            "name": "Setup & Installation",
            "project_id": 1,
            "url": "http:///testrail/index.php?/suites/view/1"
        }''')

    data = {"name": "Setup & Installation", "description": "This is a test suite"}
    res = s.add_test_suite(project_id=project_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_update_test_suite(reqmock):
    suite_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_suite/{suite_id}",
        status_code=200,
        text='''{
            "description": "This is a better description for test suite",
            "id": 1,
            "name": "Setup & Installation",
            "project_id": 1,
            "url": "http:///testrail/index.php?/suites/view/1"
        }''')

    data = {"description": "This is a better description for test suite"}
    res = s.update_test_suite(suite_id=suite_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_delete_test_suite(reqmock):
    suite_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_suite/{suite_id}", status_code=200, text='')
    s.delete_test_suite(suite_id=suite_id)
