#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestCase
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
tc = TestCase(client)


def test_get_test_cases(reqmock):
    project_id = 10
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_cases/{project_id}",
        status_code=200,
        text='''[{
            "created_by": 5,
            "created_on": 1392300984,
            "custom_expected": "..",
            "custom_preconds": "..",
            "custom_steps": "..",
            "custom_steps_separated": [
                {
                    "content": "Step 1",
                    "expected": "Expected Result 1"
                },
                {
                    "content": "Step 2",
                    "expected": "Expected Result 2"
                }
            ],
            "estimate": "1m 5s",
            "estimate_forecast": null,
            "id": 1,
            "milestone_id": 7,
            "priority_id": 2,
            "refs": "RF-1, RF-2",
            "section_id": 1,
            "suite_id": 1,
            "title": "Change document attributes (author, title, organization)",
            "type_id": 4,
            "updated_by": 1,
            "updated_on": 1393586511
        }]''')
    res = tc.get_test_cases(project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "created_by" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "custom_expected" in res[0].keys()
    assert "custom_preconds" in res[0].keys()
    assert "custom_steps" in res[0].keys()
    assert "custom_steps_separated" in res[0].keys()
    assert "estimate" in res[0].keys()
    assert "estimate_forecast" in res[0].keys()
    assert "id" in res[0].keys()
    assert "milestone_id" in res[0].keys()
    assert "priority_id" in res[0].keys()
    assert "refs" in res[0].keys()
    assert "section_id" in res[0].keys()
    assert "suite_id" in res[0].keys()
    assert "title" in res[0].keys()
    assert "type_id" in res[0].keys()
    assert "updated_by" in res[0].keys()
    assert "updated_on" in res[0].keys()


def test_get_test_case(reqmock):
    case_id = 1
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_case/{case_id}",
        status_code=200,
        text='''{
            "created_by": 5,
            "created_on": 1392300984,
            "custom_expected": "..",
            "custom_preconds": "..",
            "custom_steps": "..",
            "custom_steps_separated": [
                {
                    "content": "Step 1",
                    "expected": "Expected Result 1"
                },
                {
                    "content": "Step 2",
                    "expected": "Expected Result 2"
                }
            ],
            "estimate": "1m 5s",
            "estimate_forecast": null,
            "id": 1,
            "milestone_id": 7,
            "priority_id": 2,
            "refs": "RF-1, RF-2",
            "section_id": 1,
            "suite_id": 1,
            "title": "Change document attributes (author, title, organization)",
            "type_id": 4,
            "updated_by": 1,
            "updated_on": 1393586511
        }''')

    res = tc.get_test_case(case_id)
    assert res is not None
    assert type(res) == dict


def test_add_test_case(reqmock):
    section_id = 100
    data = {}
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/add_case/{section_id}",
        status_code=200,
        text='''{
            "created_by": 5,
            "created_on": 1392300984,
            "custom_expected": "..",
            "custom_preconds": "..",
            "custom_steps": "..",
            "custom_steps_separated": [
                {
                    "content": "Step 1",
                    "expected": "Expected Result 1"
                },
                {
                    "content": "Step 2",
                    "expected": "Expected Result 2"
                }
            ],
            "estimate": "1m 5s",
            "estimate_forecast": null,
            "id": 1,
            "milestone_id": 7,
            "priority_id": 2,
            "refs": "RF-1, RF-2",
            "section_id": 1,
            "suite_id": 1,
            "title": "Change document attributes (author, title, organization)",
            "type_id": 4,
            "updated_by": 1,
            "updated_on": 1393586511
        }''')

    res = tc.add_test_case(section_id, data)
    assert res is not None
    assert type(res) == dict


def test_update_test_case(reqmock):
    case_id = 100
    data = {}
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/update_case/{case_id}",
        status_code=200,
        text='''{
            "created_by": 5,
            "created_on": 1392300984,
            "custom_expected": "..",
            "custom_preconds": "..",
            "custom_steps": "..",
            "custom_steps_separated": [
                {
                    "content": "Step 1",
                    "expected": "Expected Result 1"
                },
                {
                    "content": "Step 2",
                    "expected": "Expected Result 2"
                }
            ],
            "estimate": "1m 5s",
            "estimate_forecast": null,
            "id": 1,
            "milestone_id": 7,
            "priority_id": 2,
            "refs": "RF-1, RF-2",
            "section_id": 1,
            "suite_id": 1,
            "title": "Change document attributes (author, title, organization)",
            "type_id": 4,
            "updated_by": 1,
            "updated_on": 1393586511
        }''')

    res = tc.update_test_case(case_id, data)
    assert res is not None
    assert type(res) == dict


def test_delete_test_case(reqmock):
    case_id = 100
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/delete_case/{case_id}", status_code=200, text='')
    tc.delete_test_case(case_id)
