#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Configuration
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
conf = Configuration(client)


def test_get_all(reqmock):
    project_id = 100
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_configs/{project_id}",
        status_code=200,
        text='''[
            {
                "configs": [
                    {
                        "group_id": 1,
                        "id": 1,
                        "name": "Chrome"
                    },
                    {
                        "group_id": 1,
                        "id": 2,
                        "name": "Firefox"
                    },
                    {
                        "group_id": 1,
                        "id": 3,
                        "name": "Internet Explorer"
                    }
                ],
                "id": 1,
                "name": "Browsers",
                "project_id": 1
            },
            {
                "configs": [
                    {
                        "group_id": 2,
                        "id": 6,
                        "name": "Ubuntu 12"
                    },
                    {
                        "group_id": 2,
                        "id": 4,
                        "name": "Windows 7"
                    },
                    {
                        "group_id": 2,
                        "id": 5,
                        "name": "Windows 8"
                    }
                ],
                "id": 2,
                "name": "Operating Systems",
                "project_id": 1
            }
        ]''',)

    res = conf.get_all(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "configs" in res[0].keys()
    assert type(res[0]["configs"]) == list
    assert type(res[0]["configs"][0]) == dict
    assert "group_id" in res[0]["configs"][0]
    assert "id" in res[0]["configs"][0]
    assert "name" in res[0]["configs"][0]


def test_add_group(reqmock):
    project_id = 100
    name = "Browsers"
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_config_group/{project_id}",
        status_code=200,
        text='''{
            "name": "Browsers"
        }''')
    res = conf.add_group(project_id=project_id, name=name)
    assert res is not None
    assert "name" in res.keys()
    assert res["name"] == name


def test_add(reqmock):
    config_group_id = 100
    name = "Chrome"
    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_config/{config_group_id}",
        status_code=200,
        text='''{
            "name": "Chrome"
        }''')
    res = conf.add(config_group_id=config_group_id, name=name)
    assert res is not None
    assert "name" in res.keys()
    assert res["name"] == name


def test_update_group(reqmock):
    config_group_id = 100
    name = "Browsers"
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_config_group/{config_group_id}",
        status_code=200,
        text='''{
            "name": "Browsers"
        }''')
    res = conf.update_group(config_group_id=config_group_id, name=name)
    assert res is not None
    assert "name" in res.keys()
    assert res["name"] == name


def test_update(reqmock):
    config_id = 100
    name = "Chrome"
    reqmock.post(f"{BASEURL}/index.php?/api/v2/update_config/{config_id}",
        status_code=200,
        text='''{
            "name": "Chrome"
        }''')
    res = conf.update(config_id=config_id, name=name)
    assert res is not None
    assert "name" in res.keys()
    assert res["name"] == name


def test_delete_group(reqmock):
    config_group_id = 100
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_config_group/{config_group_id}",
        text='', status_code=200)
    conf.delete_group(config_group_id=config_group_id)


def test_delete(reqmock):
    config_id = 100
    reqmock.post(f"{BASEURL}/index.php?/api/v2/delete_config/{config_id}",
        text='', status_code=200)
    conf.delete(config_id=config_id)
