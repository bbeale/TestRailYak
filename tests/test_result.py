#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Result
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
r = Result(client)


def test_get_all(reqmock):
    test_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_results/{test_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 1,
            "comment": "This test failed: ..",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "5m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }]''')

    res = r.get_all(test_id=test_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "assignedto_id" in res[0].keys()
    assert "comment" in res[0].keys()
    assert "created_by" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "custom_step_results" in res[0].keys()
    assert "defects" in res[0].keys()
    assert "elapsed" in res[0].keys()
    assert "id" in res[0].keys()
    assert "status_id" in res[0].keys()
    assert "test_id" in res[0].keys()
    assert "version" in res[0].keys()


def test_get_all_from_test_case(reqmock):
    run_id = 1
    case_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_results_for_case/{run_id}/{case_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 1,
            "comment": "This test failed: ..",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "5m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }]''')

    res = r.get_all_from_test_case(run_id=run_id, case_id=case_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_get_all_from_test_run(reqmock):
    run_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_results_for_run/{run_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 1,
            "comment": "This test failed: ..",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "5m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }]''')

    res = r.get_all_from_test_run(run_id=run_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add(reqmock):
    test_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_result/{test_id}",
        status_code=200,
        text='''{
            "assignedto_id": 6,
            "comment": "Test comment",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "1m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }''')

    data = {
        "status_id": 5,
        "comment": "Test comment",
        "version": "1.0RC1",
        "elapsed": "1m",
        "defects": "TR-1",
        "assignedto_id": 6
    }

    res = r.add(test_id=test_id, data=data)
    assert res is not None
    assert type(res) == dict
    assert res["status_id"] == 5
    assert res["comment"] == "Test comment"
    assert res["version"] == "1.0RC1"
    assert res["elapsed"] == "1m"
    assert res["defects"] == "TR-1"
    assert res["assignedto_id"] == 6


def test_add_to_test_case(reqmock):
    run_id = 1
    case_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_result_for_case/{run_id}/{case_id}",
        status_code=200,
        text='''{
            "assignedto_id": 6,
            "comment": "Test comment",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "1m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }''')

    data = {
        "status_id": 5,
        "comment": "Test comment",
        "version": "1.0RC1",
        "elapsed": "1m",
        "defects": "TR-1",
        "assignedto_id": 6
    }

    res = r.add_to_test_case(run_id=run_id, case_id=case_id, data=data)
    assert res is not None
    assert type(res) == dict
    assert res["status_id"] == 5
    assert res["comment"] == "Test comment"
    assert res["version"] == "1.0RC1"
    assert res["elapsed"] == "1m"
    assert res["defects"] == "TR-1"
    assert res["assignedto_id"] == 6


def test_add_results(reqmock):

    run_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_results/{run_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 1,
            "comment": "This test failed: ..",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "5m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }]''')

    data = {
        "results": [
            {
                "test_id": 101,
                "status_id": 5,
                "comment": "This test failed",
                "defects": "TR-7"

            },
            {
                "test_id": 102,
                "status_id": 1,
                "comment": "This test passed",
                "elapsed": "5m",
                "version": "1.0 RC1"
            },
            {
                "test_id": 101,
                "assignedto_id": 5,
                "comment": "Assigned this test to Joe"
            }
        ]
    }

    res = r.add_results(run_id=run_id, data=data)
    assert res is not None


def test_add_results_to_case(reqmock):
    run_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_results_for_cases/{run_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 1,
            "comment": "This test failed: ..",
            "created_by": 1,
            "created_on": 1393851801,
            "custom_step_results": [{
                "..": "..."
            }],
            "defects": "TR-1",
            "elapsed": "5m",
            "id": 1,
            "status_id": 5,
            "test_id": 1,
            "version": "1.0RC1"
        }]''')

    data = {
        "results": [
            {
                "case_id": 1,
                "status_id": 5,
                "comment": "This test failed",
                "defects": "TR-7"

            },
            {
                "case_id": 2,
                "status_id": 1,
                "comment": "This test passed",
                "elapsed": "5m",
                "version": "1.0 RC1"
            },
            {
                "case_id": 1,
                "assignedto_id": 5,
                "comment": "Assigned this test to Joe"
            }
        ]
    }
    res = r.add_results_to_case(run_id=run_id, data=data)
    assert res is not None
