#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Project
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
p = Project(client)


def test_get(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_project/{project_id}",
        status_code=200,
        text='''{
            "announcement": "..",
            "completed_on": null,
            "id": 1,
            "is_completed": false,
            "name": "Datahub",
            "show_announcement": true,
            "url": "http:///testrail/index.php?/projects/overview/1"
        }''')

    res = p.get(project_id=project_id)
    assert res is not None
    assert type(res) == dict
    assert "announcement" in res.keys()
    assert "completed_on" in res.keys()
    assert "id" in res.keys()
    assert "is_completed" in res.keys()
    assert "name" in res.keys()
    assert "show_announcement" in res.keys()
    assert "url" in res.keys()


def test_get_all(reqmock):
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_projects",
        status_code=200,
        text='''[{
            "announcement": "..",
            "completed_on": null,
            "id": 1,
            "is_completed": false,
            "name": "Datahub",
            "show_announcement": true,
            "url": "http:///testrail/index.php?/projects/overview/1"
        }]''')
    res = p.get_all()
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add(reqmock):
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_project",
        status_code=200,
        text='''{
            "announcement": "This is the description for the project",
            "completed_on": null,
            "id": 1,
            "is_completed": false,
            "name": "This is a new project",
            "show_announcement": true,
            "url": "http:///testrail/index.php?/projects/overview/1"
        }''')

    data = {
        "name": "This is a new project",
        "announcement": "This is the description for the project",
        "show_announcement": True
    }

    res = p.add(data=data)
    assert res is not None
    assert type(res) == dict
    assert res["name"] == "This is a new project"
    assert res["announcement"] == "This is the description for the project"


def test_update(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_project/{project_id}",
        status_code=200,
        text='''{
            "announcement": "..",
            "completed_on": null,
            "id": 1,
            "is_completed": true,
            "name": "Datahub",
            "show_announcement": true,
            "url": "http:///testrail/index.php?/projects/overview/1"
        }''')

    data = {
        "is_completed": True
    }

    res = p.update(project_id=project_id, data=data)
    assert res is not None
    assert res["is_completed"] is True


def test_delete(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_project/{project_id}", status_code=200, text="")
    p.delete(project_id=project_id)
