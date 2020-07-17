#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Configuration
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
conf = Configuration(client)


def test_get_configs(reqmock):
    project_id = 100
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_configs/{project_id}", text='''[
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
    ]''')

    res = conf.get_configs(project_id=project_id)
    assert res is not None
    assert type(res) == list


def test_add_config_group(reqmock):
    reqmock.post()


def test_add_config(reqmock):
    reqmock.post()


def test_update_config_group(reqmock):
    reqmock.post()


def test_update_config(reqmock):
    reqmock.post()


def test_delete_config_group(reqmock):
    reqmock.post()


def test_delete_config(reqmock):
    reqmock.post()
