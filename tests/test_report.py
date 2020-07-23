#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Report
from lib.testrail import APIClient
from tests import BASEURL, reqmock


client = APIClient(BASEURL)
r = Report(client)


def test_get_reports(reqmock):
    project_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_reports/{project_id}",
        status_code=200,
        text='''[{
            "id": 1,
            "name": "Activity Summary (Cases) %date%",
            "description": null,
            "notify_user": true,
            "notify_link": false,
            "notify_link_recipients": null,
            "notify_attachment": false,
            "notify_attachment_recipients": "person1@example.com,person2@example.com",
            "notify_attachment_html_format": false,
            "notify_attachment_pdf_format": false,
            "cases_groupby": "day",
            "changes_daterange": "5",
            "changes_daterange_from": null,
            "changes_daterange_to": null,
            "suites_include": "1",
            "suites_ids": null,
            "sections_include": "1",
            "sections_ids": null,
            "cases_columns": {
                "cases:id": 75,
                "cases:title": 0,
                "cases:created_by": 125,
                "cases:updated_by": 125
            },
            "cases_filters": null,
            "cases_limit": 1000,
            "content_hide_links": false,
            "cases_include_new": true,
            "cases_include_updated": true
        }]''')

    res = r.get_reports(project_id=project_id)
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
    assert "id" in res[0].keys()
    assert "name" in res[0].keys()
    assert "description" in res[0].keys()
    assert "notify_user" in res[0].keys()
    assert "notify_link" in res[0].keys()
    assert "notify_link_recipients" in res[0].keys()
    assert "notify_attachment" in res[0].keys()
    assert "notify_attachment_html_format" in res[0].keys()
    assert "notify_attachment_pdf_format" in res[0].keys()


def test_run_report(reqmock):
    report_template_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/run_report/{report_template_id}",
        status_code=200,
        text='''{
            "report_url": "https://docs.testrail.com/index.php?/reports/view/383",
            "report_html": "https://docs.testrail.com/index.php?/reports/get_html/383",
            "report_pdf": "https://docs.testrail.com/index.php?/reports/get_pdf/383"
        }''')

    res = r.run_report(report_template_id=report_template_id)
    assert res is not None
    assert type(res) == dict
    assert "report_url" in res.keys()
    assert "report_html" in res.keys()
    assert "report_pdf" in res.keys()
