#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Attachment
from lib.testrail import APIClient
import os
from tests import reqmock


def check_file(file):
    try:
        assert (os.path.exists(file) and os.path.isfile(file))
    except AssertionError:
        print(f"[!] File {file} does not exist. Creating it.")
        make_file(file)


def make_file(file):
    try:
        with open(file, "w") as f:
            print(f"[+] Created new file {f.name}")
    except FileExistsError as err:
        print(f"[!] File {file} already exists.")
        raise err


client = APIClient("http://example.testrail.com")
a = Attachment(client)


def test_attach_to_plan(reqmock):
    file_path = "attachment.txt"
    plan_id = 100
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/add_attachment_to_plan/{plan_id}",
        text="""{
            "attachment_id": 443
        }""")

    res = a.attach_to_plan(plan_id, file_path)
    assert res is not None
    assert type(res) == dict
    assert "attachment_id" in res.keys()
    assert res["attachment_id"] == 443


def test_attach_to_plan_entry(reqmock):
    file_path = "attachment.txt"
    plan_id = 100
    entry_id = 200
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/add_attachment_to_plan_entry/{plan_id}/{entry_id}",
        text="""{
            "attachment_id": 443
        }""")

    res = a.attach_to_plan_entry(plan_id, entry_id, file_path)
    assert res is not None
    assert type(res) == dict
    assert "attachment_id" in res.keys()
    assert res["attachment_id"] == 443


def test_attach_to_result(reqmock):
    file_path = "attachment.txt"
    result_id = 100
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/add_attachment_to_result/{result_id}",
        text="""{
            "attachment_id": 443
        }""")

    res = a.attach_to_result(result_id, file_path)
    assert res is not None
    assert type(res) == dict
    assert "attachment_id" in res.keys()
    assert res["attachment_id"] == 443


def test_attach_to_run(reqmock):
    file_path = "attachment.txt"
    run_id = 100
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/add_attachment_to_run/{run_id}",
        text="""{
            "attachment_id": 443
        }""")

    res = a.attach_to_run(run_id, file_path)
    assert res is not None
    assert type(res) == dict
    assert "attachment_id" in res.keys()
    assert res["attachment_id"] == 443


def test_get_case_attachments(reqmock):
    case_id = 100
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_attachments_for_case/{case_id}",
        text="""[
            {
                "id": 444,
                "name": "What-Testers-Should-Be-Automating.jpg",
                "filename": "444.what_testers_should_be_automating.jpg",
                "size": 166994,
                "created_on": 1554737184,
                "project_id": 14,
                "case_id": 3414,
                "test_change_id": 17899,
                "user_id": 10
            }
        ]""")

    res = a.get_case_attachments(case_id)
    assert res is not None
    assert "id" in res[0].keys()
    assert "name" in res[0].keys()
    assert "filename" in res[0].keys()
    assert "size" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "project_id" in res[0].keys()
    assert "case_id" in res[0].keys()
    assert "test_change_id" in res[0].keys()
    assert "user_id" in res[0].keys()


def test_get_plan_attachments(reqmock):
    plan_id = 100
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_attachments_for_plan/{plan_id}",
        text="""[
            {
                "id": 444,
                "name": "What-Testers-Should-Be-Automating.jpg",
                "filename": "444.what_testers_should_be_automating.jpg",
                "size": 166994,
                "created_on": 1554737184,
                "project_id": 14,
                "case_id": 3414,
                "test_change_id": 17899,
                "user_id": 10
            }
        ]""")

    res = a.get_plan_attachments(plan_id)
    assert res is not None
    assert "id" in res[0].keys()
    assert "name" in res[0].keys()
    assert "filename" in res[0].keys()
    assert "size" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "project_id" in res[0].keys()
    assert "case_id" in res[0].keys()
    assert "test_change_id" in res[0].keys()
    assert "user_id" in res[0].keys()


def test_get_plan_entry_attachments(reqmock):
    plan_id = 444
    entry_id = 444
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_attachments_for_plan_entry/{plan_id}/{entry_id}",
        text="""[
            {
                "id": 444,
                "name": "What-Testers-Should-Be-Automating.jpg",
                "filename": "444.what_testers_should_be_automating.jpg",
                "size": 166994,
                "created_on": 1554737184,
                "project_id": 14,
                "case_id": 3414,
                "test_change_id": 17899,
                "user_id": 10
            }
        ]""")

    res = a.get_plan_entry_attachments(plan_id, entry_id)
    assert res is not None
    assert "id" in res[0].keys()
    assert "name" in res[0].keys()
    assert "filename" in res[0].keys()
    assert "size" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "project_id" in res[0].keys()
    assert "case_id" in res[0].keys()
    assert "test_change_id" in res[0].keys()
    assert "user_id" in res[0].keys()


def test_get_run_attachments(reqmock):
    run_id = 444
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_attachments_for_run/{run_id}",
        text="""[
            {
                "id": 444,
                "name": "What-Testers-Should-Be-Automating.jpg",
                "filename": "444.what_testers_should_be_automating.jpg",
                "size": 166994,
                "created_on": 1554737184,
                "project_id": 14,
                "case_id": 3414,
                "test_change_id": 17899,
                "user_id": 10
            }
        ]""")

    res = a.get_run_attachments(run_id)
    assert res is not None
    assert "id" in res[0].keys()
    assert "name" in res[0].keys()
    assert "filename" in res[0].keys()
    assert "size" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "project_id" in res[0].keys()
    assert "case_id" in res[0].keys()
    assert "test_change_id" in res[0].keys()
    assert "user_id" in res[0].keys()


def test_get_test_attachments(reqmock):
    test_id = 444
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_attachments_for_test/{test_id}",
        text="""[
            {
                "id": 444,
                "name": "What-Testers-Should-Be-Automating.jpg",
                "filename": "444.what_testers_should_be_automating.jpg",
                "size": 166994,
                "created_on": 1554737184,
                "project_id": 14,
                "case_id": 3414,
                "test_change_id": 17899,
                "user_id": 10
            }
        ]""")

    res = a.get_test_attachments(test_id)
    assert res is not None
    assert "id" in res[0].keys()
    assert "name" in res[0].keys()
    assert "filename" in res[0].keys()
    assert "size" in res[0].keys()
    assert "created_on" in res[0].keys()
    assert "project_id" in res[0].keys()
    assert "case_id" in res[0].keys()
    assert "test_change_id" in res[0].keys()
    assert "user_id" in res[0].keys()


def test_get_attachment(reqmock):
    attachment_id = 444
    file_path = '../data/new_attachment.txt'
    check_file(file_path)
    reqmock.get(f"http://example.testrail.com/index.php?/api/v2/get_attachment/{attachment_id}",
        text='''Test''')

    res = a.get_attachment(attachment_id, file_path)
    assert res is not None
    assert os.path.exists(res)
    assert os.path.isfile(res)
    os.remove(file_path)


def test_delete_attachment(reqmock):
    attachment_id = 444
    reqmock.post(f"http://example.testrail.com/index.php?/api/v2/delete_attachment/{attachment_id}", text="""{}""")
    res = a.delete_attachment(attachment_id)
    assert res is not None
    assert type(res) == dict
