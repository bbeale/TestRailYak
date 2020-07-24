#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestPlan
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
tp = TestPlan(client)


def test_get_test_plan(reqmock):
    plan_id = 80
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_plan/{plan_id}",
        status_code=200,
        text='''{
            "assignedto_id": null,
            "blocked_count": 2,
            "completed_on": null,
            "created_by": 1,
            "created_on": 1393845644,
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "entries": [
            {
                "id": "3933d74b-4282-4c1f-be62-a641ab427063",
                "name": "File Formats",
                "runs": [
                {
                    "assignedto_id": 6,
                    "blocked_count": 0,
                    "completed_on": null,
                    "config": "Firefox, Ubuntu 12",
                    "config_ids": [
                        2,
                        6
                    ],
                    "custom_status1_count": 0,
                    "custom_status2_count": 0,
                    "custom_status3_count": 0,
                    "custom_status4_count": 0,
                    "custom_status5_count": 0,
                    "custom_status6_count": 0,
                    "custom_status7_count": 0,
                    "description": null,
                    "entry_id": "3933d74b-4282-4c1f-be62-a641ab427063",
                    "entry_index": 1,
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
                }],
                "suite_id": 4
            }],
            "failed_count": 2,
            "id": 80,
            "is_completed": false,
            "milestone_id": 7,
            "name": "System test",
            "passed_count": 5,
            "project_id": 1,
            "retest_count": 1,
            "untested_count": 6,
            "url": "http:///testrail/index.php?/plans/view/80"
        }''')

    res = tp.get_test_plan(plan_id=plan_id)
    assert res is not None
    assert type(res) == dict
    assert "assignedto_id" in res.keys()
    assert "blocked_count" in res.keys()
    assert "completed_on" in res.keys()
    assert "created_by" in res.keys()
    assert "created_on" in res.keys()
    assert "description" in res.keys()
    assert "entries" in res.keys()
    assert "failed_count" in res.keys()
    assert "id" in res.keys()
    assert "is_completed" in res.keys()
    assert "milestone_id" in res.keys()
    assert "name" in res.keys()
    assert "passed_count" in res.keys()
    assert "project_id" in res.keys()
    assert "retest_count" in res.keys()
    assert "untested_count" in res.keys()
    assert "url" in res.keys()


def test_get_test_plans(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_plans/{project_id}",
        status_code=200,
        text='''[{
            "assignedto_id": null,
            "blocked_count": 2,
            "completed_on": null,
            "created_by": 1,
            "created_on": 1393845644,
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "entries": [
            {
                "id": "3933d74b-4282-4c1f-be62-a641ab427063",
                "name": "File Formats",
                "runs": [
                {
                    "assignedto_id": 6,
                    "blocked_count": 0,
                    "completed_on": null,
                    "config": "Firefox, Ubuntu 12",
                    "config_ids": [
                        2,
                        6
                    ],
                    "custom_status1_count": 0,
                    "custom_status2_count": 0,
                    "custom_status3_count": 0,
                    "custom_status4_count": 0,
                    "custom_status5_count": 0,
                    "custom_status6_count": 0,
                    "custom_status7_count": 0,
                    "description": null,
                    "entry_id": "3933d74b-4282-4c1f-be62-a641ab427063",
                    "entry_index": 1,
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
                }],
                "suite_id": 4
            }],
            "failed_count": 2,
            "id": 80,
            "is_completed": false,
            "milestone_id": 7,
            "name": "System test",
            "passed_count": 5,
            "project_id": 1,
            "retest_count": 1,
            "untested_count": 6,
            "url": "http:///testrail/index.php?/plans/view/80"
        }]''')

    res = tp.get_test_plans(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add_test_plan(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_plan/{project_id}",
        status_code=200,
        text='''{
            "assignedto_id": null,
            "blocked_count": 2,
            "completed_on": null,
            "created_by": 1,
            "created_on": 1393845644,
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "entries": [
            {
                "id": "3933d74b-4282-4c1f-be62-a641ab427063",
                "name": "File Formats",
                "runs": [
                {
                    "assignedto_id": 6,
                    "blocked_count": 0,
                    "completed_on": null,
                    "config": "Firefox, Ubuntu 12",
                    "config_ids": [
                        2,
                        6
                    ],
                    "custom_status1_count": 0,
                    "custom_status2_count": 0,
                    "custom_status3_count": 0,
                    "custom_status4_count": 0,
                    "custom_status5_count": 0,
                    "custom_status6_count": 0,
                    "custom_status7_count": 0,
                    "description": null,
                    "entry_id": "3933d74b-4282-4c1f-be62-a641ab427063",
                    "entry_index": 1,
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
                }],
                "suite_id": 4
            }],
            "failed_count": 2,
            "id": 80,
            "is_completed": false,
            "milestone_id": 7,
            "name": "System test",
            "passed_count": 5,
            "project_id": 1,
            "retest_count": 1,
            "untested_count": 6,
            "url": "http:///testrail/index.php?/plans/view/80"
        }''')

    data = {
        "name": "System test",
        "description": "description",
        "entries": [{
                "suite_id": 1,
                "name": "Custom run name",
                "assignedto_id": 1
            },
            {
                "suite_id": 1,
                "include_all": False,
                "case_ids": [1, 2, 3, 5]
            }
        ]}
    res = tp.add_test_plan(project_id=project_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_add_plan_entry(reqmock):
    plan_id = 80
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_plan_entry/{plan_id}",
        status_code=200,
        text='''{
            "assignedto_id": null,
            "blocked_count": 2,
            "completed_on": null,
            "created_by": 1,
            "created_on": 1393845644,
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": null,
            "entries": [
            {
                "id": "3933d74b-4282-4c1f-be62-a641ab427063",
                "name": "File Formats",
                "runs": [
                {
                    "assignedto_id": 6,
                    "blocked_count": 0,
                    "completed_on": null,
                    "config": "Firefox, Ubuntu 12",
                    "config_ids": [
                        2,
                        6
                    ],
                    "custom_status1_count": 0,
                    "custom_status2_count": 0,
                    "custom_status3_count": 0,
                    "custom_status4_count": 0,
                    "custom_status5_count": 0,
                    "custom_status6_count": 0,
                    "custom_status7_count": 0,
                    "description": null,
                    "entry_id": "3933d74b-4282-4c1f-be62-a641ab427063",
                    "entry_index": 1,
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
                }],
                "suite_id": 4
            }],
            "failed_count": 2,
            "id": 80,
            "is_completed": false,
            "milestone_id": 7,
            "name": "System test",
            "passed_count": 5,
            "project_id": 1,
            "retest_count": 1,
            "untested_count": 6,
            "url": "http:///testrail/index.php?/plans/view/80"
        }''')

    data = {
        "suite_id": 1,
        "assignedto_id": 1,
        "include_all": True,
        "config_ids": [1, 2, 4, 5, 6],
        "runs": [
            {
                "include_all": False,
                "case_ids": [1, 2, 3],
                "config_ids": [2, 5]
            },
            {
                "include_all": False,
                "case_ids": [1, 2, 3, 5, 8],
                "assignedto_id": 2,
                "config_ids": [2, 6]
            }
        ]
    }

    res = tp.add_plan_entry(plan_id=plan_id, data=data)
    assert res is not None


def test_update_plan(reqmock):
    plan_id = 80
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_plan/{plan_id}",
        status_code=200,
        text='''{
            "assignedto_id": null,
            "blocked_count": 2,
            "completed_on": null,
            "created_by": 1,
            "created_on": 1393845644,
            "custom_status1_count": 0,
            "custom_status2_count": 0,
            "custom_status3_count": 0,
            "custom_status4_count": 0,
            "custom_status5_count": 0,
            "custom_status6_count": 0,
            "custom_status7_count": 0,
            "description": "description",
            "entries": [
            {
                "id": "3933d74b-4282-4c1f-be62-a641ab427063",
                "name": "File Formats",
                "runs": [
                {
                    "assignedto_id": 6,
                    "blocked_count": 0,
                    "completed_on": null,
                    "config": "Firefox, Ubuntu 12",
                    "config_ids": [
                        2,
                        6
                    ],
                    "custom_status1_count": 0,
                    "custom_status2_count": 0,
                    "custom_status3_count": 0,
                    "custom_status4_count": 0,
                    "custom_status5_count": 0,
                    "custom_status6_count": 0,
                    "custom_status7_count": 0,
                    "description": null,
                    "entry_id": "3933d74b-4282-4c1f-be62-a641ab427063",
                    "entry_index": 1,
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
                }],
                "suite_id": 4
            }],
            "failed_count": 2,
            "id": 80,
            "is_completed": false,
            "milestone_id": 7,
            "name": "System test",
            "passed_count": 5,
            "project_id": 1,
            "retest_count": 1,
            "untested_count": 6,
            "url": "http:///testrail/index.php?/plans/view/80"
        }''')

    data = {
        "name": "System test",
        "description": "description"
    }

    res = tp.update_plan(plan_id=plan_id, data=data)
    assert res is not None


def test_update_plan_entry(reqmock):
    plan_id = 80
    entry_id = 81
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_plan_entry/{plan_id}/{entry_id}",
        status_code=200,
        text='''{
                "id": "3933d74b-4282-4c1f-be62-a641ab427063",
                "name": "File Formats",
                "runs": [
                {
                    "assignedto_id": 6,
                    "blocked_count": 0,
                    "completed_on": null,
                    "config": "Firefox, Ubuntu 12",
                    "config_ids": [
                        2,
                        6
                    ],
                    "custom_status1_count": 0,
                    "custom_status2_count": 0,
                    "custom_status3_count": 0,
                    "custom_status4_count": 0,
                    "custom_status5_count": 0,
                    "custom_status6_count": 0,
                    "custom_status7_count": 0,
                    "description": null,
                    "entry_id": "3933d74b-4282-4c1f-be62-a641ab427063",
                    "entry_index": 1,
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
                }],
                "suite_id": 4
            }''')
    data = {
        "name": "System test",
        "description": "description",
        "assignedto_id": 6,
        "include_all": False,
        "case_ids": [1, 2, 3, 5],
        "refs": "",
    }

    res = tp.update_plan_entry(plan_id=plan_id, entry_id=entry_id, data=data)
    assert res is not None


def test_close_plan(reqmock):
    plan_id = 80
    reqmock.post(f"{BASEURL}/index.php?/api/v2/close_plan/{plan_id}", status_code=200, text="")
    tp.close_plan(plan_id=plan_id)


def test_delete_plan(reqmock):
    plan_id = 80
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_plan/{plan_id}", status_code=200, text="")
    tp.delete_plan(plan_id=plan_id)


def test_delete_plan_entry(reqmock):
    plan_id = 80
    entry_id = 81
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_plan_entry/{plan_id}/{entry_id}", status_code=200, text="")
    tp.delete_plan_entry(plan_id=plan_id, entry_id=entry_id)
