#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import CaseField
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
cf = CaseField(client)


def test_get_case_fields(reqmock):
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_case_fields",
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
            },
        ]''')

    res = cf.get_case_fields()
    assert res is not None


def test_add_case_field(reqmock):
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/add_case_field",
        text='''{
            "id": 33,
            "name": "my_multiselect",
            "system_name": "custom_my_multiselect",
            "entity_id": 1,
            "label": "My Multiselect",
            "description": "my custom Multiselect description",
            "type_id": 12,
            "location_id": 2,
            "display_order": 7,
            "configs": "[{\"context\":{\"is_global\":true,\"project_ids\":\"\"},\"options\":{\"is_required\":false,\"items\":\"1, One\\n2, Two\"},\"id\":\"9f105ba2-1ed0-45e0-b459-18d890bad86e\"}]",
            "is_multi": 1,
            "is_active": 1,
            "status_id": 1,
            "is_system": 0,
            "include_all": 1,
            "template_ids": []
        }''')
    data = {"type": "12", "name": "my_multiselect", "label": "My Multiselect"}
    res = cf.add_case_field(data)
    assert res is not None
    assert "name" in res.keys()
    assert res["name"] == "my_multiselect"
