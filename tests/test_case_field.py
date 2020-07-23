#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import CaseField
from lib.testrail import APIClient
from tests import BASEURL, reqmock


client = APIClient(BASEURL)
cf = CaseField(client)


def test_get_case_fields(reqmock):
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_case_fields",
        status_code=200,
        text='''[
            {
                "configs": [
                    {
                        "context": {
                            "is_global": true,
                            "project_ids": null
                        },
                        "id": "..",
                        "options": {
                            "default_value": "",
                            "format": "markdown",
                            "is_required": false,
                            "rows": "5"
                        }
                    }
                ],
                "description": "The preconditions of this test case. ..",
                "display_order": 1,
                "id": 1,
                "label": "Preconditions",
                "name": "preconds",
                "system_name": "custom_preconds",
                "type_id": 3
            }
        ]''')

    res = cf.get_case_fields()
    assert res is not None
    assert "configs" in res[0].keys()
    assert "context" in res[0]["configs"][0].keys()
    assert "options" in res[0]["configs"][0].keys()
    assert "id" in res[0]["configs"][0].keys()
    assert "description" in res[0].keys()
    assert "display_order" in res[0].keys()
    assert "id" in res[0].keys()
    assert "label" in res[0].keys()
    assert "name" in res[0].keys()
    assert "system_name" in res[0].keys()
    assert "type_id" in res[0].keys()


def test_add_case_field(reqmock):

    reqmock.post(f"{BASEURL}/index.php?/api/v2/add_case_field",
        status_code=200,
        text="""{
            "id": 33,
            "name": "My New Field",
            "system_name": "my_new_field",
            "entity_id": 1,
            "label": "My Multiselect",
            "description": "my custom Multiselect description",
            "type_id": 12,
            "location_id": 2,
            "display_order": 7,
            "configs": [{\"context\":{\"is_global\":true,\"project_ids\":\"\"},\"options\":{\"is_required\":false,\"items\":\"1, One\\n2, Two\"},\"id\":\"9f105ba2-1ed0-45e0-b459-18d890bad86e\"}],
            "is_multi": 1,
            "is_active": 1,
            "status_id": 1,
            "is_system": 0,
            "include_all": 1,
            "template_ids": []
        }""")

    data = {
        "type": "12",
        "name": "my_multiselect",
        "label": "My Multiselect",
        "include_all": "true",
        "configs": [{
                "context": {
                    "is_global": "true",
                    "project_ids": ""
                },
                "options": {
                    "is_required": "false",
                    "items": "1, One\n2, Two"
                },
                "id": "9f105ba2-1ed0-45e0-b459-18d890bad86e"
        }]
    }

    res = cf.add_case_field(data)
    assert res is not None
    assert "description" in res.keys()
    assert "display_order" in res.keys()
    assert "id" in res.keys()
    assert "label" in res.keys()
    assert "name" in res.keys()
    assert "system_name" in res.keys()
    assert "type_id" in res.keys()
    assert "entity_id" in res.keys()
    assert "location_id" in res.keys()
    assert "is_multi" in res.keys()
    assert "is_active" in res.keys()
    assert "status_id" in res.keys()
    assert "is_system" in res.keys()
    assert "include_all" in res.keys()
    assert "template_ids" in res.keys()
    assert res["id"] == 33
    assert res["name"] == "My New Field"
    assert res["system_name"] == "my_new_field"
