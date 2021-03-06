#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Milestone
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
m = Milestone(client)


def test_get(reqmock):
    milestone_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_milestone/{milestone_id}",
        status_code=200,
        text='''{
            "completed_on": 1389968184,
            "description": "...",
            "due_on": 1391968184,
            "id": 1,
            "is_completed": true,
            "name": "Release 1.5",
            "project_id": 1,
            "url": "http:///testrail/index.php?/milestones/view/1"
        }''')

    res = m.get(milestone_id=milestone_id)
    assert res is not None
    assert type(res) == dict
    assert "completed_on" in res.keys()
    assert "description" in res.keys()
    assert "due_on" in res.keys()
    assert "id" in res.keys()
    assert "is_completed" in res.keys()
    assert "name" in res.keys()
    assert "project_id" in res.keys()
    assert "url" in res.keys()


def test_get_all(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_milestones/{project_id}",
        status_code=200,
        text='''[{
            "completed_on": 1389968184,
            "description": "...",
            "due_on": 1391968184,
            "id": 1,
            "is_completed": true,
            "name": "Release 1.5",
            "project_id": 1,
            "url": "http:///testrail/index.php?/milestones/view/1"
        }]''')
    res = m.get_all(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_milestone/{project_id}",
        status_code=200,
        text='''{
            "completed_on": 1389968184,
            "description": "...",
            "due_on": 1391968184,
            "id": 1,
            "is_completed": true,
            "name": "Release 1.5",
            "project_id": 1,
            "url": "http:///testrail/index.php?/milestones/view/1"
        }''')

    data = {"name": "Release 1.5", "description": "...", "due_on": 1391968184}
    res = m.add(project_id=project_id, data=data)
    assert res is not None


def test_update(reqmock):
    milestone_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_milestone/{milestone_id}",
        status_code=200,
        text='''{
                "completed_on": 1389968184,
                "description": "...",
                "due_on": 1391968184,
                "id": 1,
                "is_completed": true,
                "name": "Release 1.5",
                "project_id": 1,
                "url": "http:///testrail/index.php?/milestones/view/1"
            }''')

    data = {"name": "Release 1.5", "description": "...", "due_on": 1391968184}
    res = m.update(milestone_id=milestone_id, data=data)
    assert res is not None


def test_delete(reqmock):
    milestone_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_milestone/{milestone_id}",
        status_code=200,
        text='')
    res = m.delete(milestone_id=milestone_id)
    assert res is not None
