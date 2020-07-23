#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Section
from lib.testrail import APIClient
from tests import reqmock


BASEURL = "http://example.testrail.com"

client = APIClient(BASEURL)
s = Section(client)


def test_get_section(reqmock):
    section_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_section/{section_id}",
        status_code=200,
        text='''{
            "depth": 0,
            "description": null,
            "display_order": 1,
            "id": 1,
            "name": "Prerequisites",
            "parent_id": null,
            "suite_id": 1
        }''')

    res = s.get_section(section_id=section_id)
    assert res is not None
    assert type(res) == dict
    assert "depth" in res.keys()
    assert "description" in res.keys()
    assert "display_order" in res.keys()
    assert "id" in res.keys()
    assert "name" in res.keys()
    assert "parent_id" in res.keys()
    assert "suite_id" in res.keys()


def test_get_sections(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_sections/{project_id}",
        status_code=200,
        text='''[
            {
                "depth": 0,
                "display_order": 1,
                "id": 1,
                "name": "Prerequisites",
                "parent_id": null,
                "suite_id": 1
            },
            {
                "depth": 0,
                "display_order": 2,
                "id": 2,
                "name": "Documentation & Help",
                "parent_id": null,
                "suite_id": 1
            },
            {
                "depth": 1,
                "display_order": 3,
                "id": 3,
                "name": "Licensing & Terms",
                "parent_id": 2,
                "suite_id": 1
            }
        ]''')

    res = s.get_sections(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_get_sections_by_suite_id(reqmock):
    project_id = 1
    suite_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_sections/{project_id}&suite_id={suite_id}",
        status_code=200,
        text='''[
            {
                "depth": 0,
                "display_order": 1,
                "id": 1,
                "name": "Prerequisites",
                "parent_id": null,
                "suite_id": 1
            },
            {
                "depth": 0,
                "display_order": 2,
                "id": 2,
                "name": "Documentation & Help",
                "parent_id": null,
                "suite_id": 1
            },
            {
                "depth": 1,
                "display_order": 3,
                "id": 3,
                "name": "Licensing & Terms",
                "parent_id": 2,
                "suite_id": 1
            }
        ]''')

    res = s.get_sections_by_suite_id(project_id=project_id, suite_id=suite_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict


def test_add_section(reqmock):
    project_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_section/{project_id}",
        status_code=200,
        text='''{
            "depth": 0,
            "description": "This is the description",
            "display_order": 1,
            "id": 1,
            "name": "This is a new section",
            "parent_id": null,
            "suite_id": 5
        }''')

    data = {
        "suite_id": 5,
        "name": "This is a new section",
        "description": "This is the description"
    }

    res = s.add_section(project_id=project_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_add_child_section(reqmock):
    project_id = 1
    parent_id = 10
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_section/{project_id}",
        status_code=200,
        text='''{
            "depth": 0,
            "description": "This is the description",
            "display_order": 1,
            "id": 1,
            "name": "This is a new CHILD section", 
            "parent_id": 10,
            "suite_id": 5
        }''')

    data = {
        "suite_id": 5,
        "name": "This is a new CHILD section",
        "description": "This is the description",
        "parent_id": parent_id
    }

    res = s.add_child_section(project_id=project_id, parent_id=parent_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_update_section(reqmock):
    section_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_section/{section_id}",
        status_code=200,
        text='''{
            "depth": 0,
            "description": null,
            "display_order": 1,
            "id": 1,
            "name": "A better section name",
            "parent_id": null,
            "suite_id": 1
        }''')

    data = {
        "name": "A better section name"
    }

    res = s.update_section(section_id=section_id, data=data)
    assert res is not None
    assert type(res) == dict


def test_delete_section(reqmock):
    section_id = 1
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_section/{section_id}",
        status_code=200,
        text="")

    s.delete_section(section_id=section_id)
