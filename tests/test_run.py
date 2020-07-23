#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestRun
from lib.testrail import APIClient
from tests import reqmock


BASEURL = "http://example.testrail.com"

client = APIClient(BASEURL)
r = TestRun(client)


def test_get_test_run(reqmock):
    run_id = 81
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_run/{run_id}",
        status_code=200,
        text='''{
            "assignedto_id": 6,
            "blocked_count": 0,
            "completed_on": null,
            "config": "Firefox, Ubuntu 12",
            "config_ids": [
                2,
                6
            ],
            "created_by": 1,
            "created_on": 1393845644,
                "refs": "SAN-1",
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "failed_count": 2,
            "id": 81,
            "include_all": false,
            "is_completed": false,
            "milestone_id": 7,
            "name": "File Formats",
            "passed_count": 2,
            "plan_id": 80,
            "project_id": 1,
            "retest_count": 1,
            "suite_id": 4,
            "untested_count": 3,
            "url": "http:///testrail/index.php?/runs/view/81"
        }''')

    res = r.get_test_run(run_id=run_id)
    assert res is not None
    assert type(res) == dict
    assert "assignedto_id" in res.keys()
    assert "blocked_count" in res.keys()
    assert "completed_on" in res.keys()
    assert "config" in res.keys()
    assert "config_ids" in res.keys()
    assert "created_by" in res.keys()
    assert "created_on" in res.keys()
    assert "description" in res.keys()
    assert "failed_count" in res.keys()
    assert "id" in res.keys()
    assert "include_all" in res.keys()
    assert "is_completed" in res.keys()
    assert "milestone_id" in res.keys()
    assert "plan_id" in res.keys()
    assert "name" in res.keys()
    assert "passed_count" in res.keys()
    assert "project_id" in res.keys()
    assert "retest_count" in res.keys()
    assert "suite_id" in res.keys()
    assert "untested_count" in res.keys()
    assert "url" in res.keys()
    assert "refs" in res.keys()


def test_get_test_runs(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_runs/{project_id}",
        status_code=200,
        text='''[{
            "assignedto_id": 6,
            "blocked_count": 0,
            "completed_on": null,
            "config": "Firefox, Ubuntu 12",
            "config_ids": [
                2,
                6
            ],
            "created_by": 1,
            "created_on": 1393845644,
                "refs": "SAN-1",
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "failed_count": 2,
            "id": 81,
            "include_all": false,
            "is_completed": false,
            "milestone_id": 7,
            "name": "File Formats",
            "passed_count": 2,
            "plan_id": 80,
            "project_id": 1,
            "retest_count": 1,
            "suite_id": 4,
            "untested_count": 3,
            "url": "http:///testrail/index.php?/runs/view/81"
        }]''')

    res = r.get_test_runs(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add_test_run(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_run/{project_id}",
        status_code=200,
        text='''{
            "assignedto_id": 5,
            "blocked_count": 0,
            "completed_on": null,
            "config": "Firefox, Ubuntu 12",
            "config_ids": [
                2,
                6
            ],
            "created_by": 1,
            "created_on": 1393845644,
            "refs": "SAN-1, SAN-2",
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "failed_count": 2,
            "id": 81,
            "include_all": false,
            "is_completed": false,
            "milestone_id": 7,
            "name": "This is a new test run",
            "passed_count": 2,
            "plan_id": 80,
            "project_id": 1,
            "retest_count": 1,
            "suite_id": 4,
            "untested_count": 3,
            "url": "http:///testrail/index.php?/runs/view/81"
        }''')

    data = {
        "suite_id": 4,
        "name": "This is a new test run",
        "assignedto_id": 5,
        "refs": "SAN-1, SAN-2",
        "include_all": False,
        "case_ids": [1, 2, 3, 4, 7, 8]
    }

    res = r.add_test_run(project_id=project_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_update_test_run(reqmock):
    run_id = 81
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_run/{run_id}",
        status_code=200,
        text='''{
            "assignedto_id": 5,
            "blocked_count": 0,
            "completed_on": null,
            "config": "Firefox, Ubuntu 12",
            "config_ids": [
                2,
                6
            ],
            "created_by": 1,
            "created_on": 1393845644,
            "refs": "SAN-1, SAN-2",
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "failed_count": 2,
            "id": 81,
            "include_all": false,
            "is_completed": false,
            "milestone_id": 7,
            "name": "This is a new test run",
            "passed_count": 2,
            "plan_id": 80,
            "project_id": 1,
            "retest_count": 1,
            "suite_id": 4,
            "untested_count": 3,
            "url": "http:///testrail/index.php?/runs/view/81"
        }''')

    data = {
        "name": "This is a new name for our test run",
        "refs": "SAN-1, SAN-2, SAN-3",
        "include_all": False,
        "case_ids": [1, 2, 3]
    }

    res = r.update_test_run(run_id=run_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_close_test_run(reqmock):
    run_id = 81
    reqmock.post(f"{BASEURL}/index.php?/api/v2/close_run/{run_id}",
        status_code=200,
        text='''{
            "assignedto_id": 5,
            "blocked_count": 0,
            "completed_on": null,
            "config": "Firefox, Ubuntu 12",
            "config_ids": [
                2,
                6
            ],
            "created_by": 1,
            "created_on": 1393845644,
            "refs": "SAN-1, SAN-2",
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "failed_count": 2,
            "id": 81,
            "include_all": false,
            "is_completed": false,
            "milestone_id": 7,
            "name": "This is a new test run",
            "passed_count": 2,
            "plan_id": 80,
            "project_id": 1,
            "retest_count": 1,
            "suite_id": 4,
            "untested_count": 3,
            "url": "http:///testrail/index.php?/runs/view/81"
        }''')

    # res =
    r.close_test_run(run_id=run_id)
    # assert res is not None
    # assert type(res) == dict


def test_delete_test_run(reqmock):
    run_id = 81
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_run/{run_id}",
        status_code=200,
        text='''{
            "assignedto_id": 5,
            "blocked_count": 0,
            "completed_on": null,
            "config": "Firefox, Ubuntu 12",
            "config_ids": [
                2,
                6
            ],
            "created_by": 1,
            "created_on": 1393845644,
            "refs": "SAN-1, SAN-2",
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "failed_count": 2,
            "id": 81,
            "include_all": false,
            "is_completed": false,
            "milestone_id": 7,
            "name": "This is a new test run",
            "passed_count": 2,
            "plan_id": 80,
            "project_id": 1,
            "retest_count": 1,
            "suite_id": 4,
            "untested_count": 3,
            "url": "http:///testrail/index.php?/runs/view/81"
        }''')

    r.delete_test_run(run_id=run_id)
