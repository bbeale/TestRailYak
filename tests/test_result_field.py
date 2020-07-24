#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import ResultField
from testrail_yak.lib.testrail import APIClient
from tests import BASEURL, reqmock

client = APIClient(BASEURL)
rf = ResultField(client)


def test_get_result_fields(reqmock):
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_result_fields",
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
                            "format": "markdown",
                            "has_actual": false,
                            "has_expected": true,
                            "is_required": false
                        }
                    }
                ],
                "description": null,
                "display_order": 1,
                "id": 5,
                "label": "Steps",
                "name": "step_results",
                "system_name": "custom_step_results",
                "type_id": 11
            }
        ]''')

    res = rf.get_result_fields()
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "configs" in res[0].keys()
    assert type(res[0]["configs"]) == list
    assert type(res[0]["configs"][0]) == dict
    assert "context" in res[0]["configs"][0]
    assert "id" in res[0]["configs"][0]
    assert "options" in res[0]["configs"][0]
    assert "description" in res[0].keys()
    assert "display_order" in res[0].keys()
    assert "id" in res[0].keys()
    assert "label" in res[0].keys()
    assert "name" in res[0].keys()
    assert "system_name" in res[0].keys()
    assert "type_id" in res[0].keys()
