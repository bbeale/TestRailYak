#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Test
from lib.testrail import APIClient
from tests import BASEURL, reqmock


client = APIClient(BASEURL)
t = Test(client)


def test_get_testrun_test(reqmock):
    test_id = 100
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_test/{test_id}",
        status_code=200,
        text='''{
            "assignedto_id": 1,
            "case_id": 1,
            "custom_expected": "..",
            "custom_preconds": "..",
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
            "id": 100,
            "priority_id": 2,
            "run_id": 1,
            "status_id": 5,
            "title": "Verify line spacing on multi-page document",
            "type_id": 4
        }''')

    res = t.get_testrun_test(test_id=test_id)
    assert res is not None
    assert type(res) == dict
    assert "assignedto_id" in res.keys()
    assert "case_id" in res.keys()
    assert "custom_expected" in res.keys()
    assert "custom_preconds" in res.keys()
    assert "custom_steps_separated" in res.keys()
    assert "estimate" in res.keys()
    assert "estimate_forecast" in res.keys()
    assert "id" in res.keys()
    assert "priority_id" in res.keys()
    assert "run_id" in res.keys()
    assert "status_id" in res.keys()
    assert "title" in res.keys()
    assert "type_id" in res.keys()


def test_get_testrun_tests(reqmock):
    run_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_tests/{run_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 1,
            "case_id": 1,
            "custom_expected": "..",
            "custom_preconds": "..",
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
            "id": 100,
            "priority_id": 2,
            "run_id": 1,
            "status_id": 5,
            "title": "Verify line spacing on multi-page document",
            "type_id": 4
        }]''')

    res = t.get_testrun_tests(run_id=run_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
