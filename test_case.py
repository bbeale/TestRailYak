#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import (
    TestRailProjectException,
    TestRailSectionException,
    TestRailTestCaseException,
    TestRailNewEntityException
)

from urllib import error as E
import time


class TestCase:

    __module__ = "mh_testrail"

    def __init__(self, api):
        self.client = api

    def get_test_cases(self, project_id):
        """Get a list of test cases associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test cases
        """
        if not project_id or project_id is None:
            raise TestRailProjectException("Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestRailProjectException("project_id must be an int or float")

        if project_id <= 0:
            raise TestRailProjectException("project_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_cases/{}".format(project_id))    # wtf? [0]
        except E.HTTPError as httpe:
            print(httpe, "- Failed to get test cases. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_cases/{}".format(project_id))    # [0]
            except E.HTTPError as httpe:
                print(httpe, "- Failed to get test cases.")
        finally:
            return result

    def get_test_case(self, case_id):
        """Get a test case by case_id.

        :param case_id: ID of the test case
        :return: response from TestRail API containing the test cases
        """
        if not case_id or case_id is None:
            raise TestRailTestCaseException("Invalid case_id")

        if type(case_id) not in [int, float]:
            raise TestRailTestCaseException("case_id must be an int or float")

        if case_id <= 0:
            raise TestRailTestCaseException("case_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_case/{}".format(case_id))
        except E.HTTPError as httpe:
            print(httpe, "- Failed to get test case. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_case/{}".format(case_id))
            except E.HTTPError as httpe:
                print(httpe, "- Failed to get test case.")
        finally:
            return result

    def add_test_case(self, section_id, title):
        """Add a test case to a project by section_id.

        :param section_id: ID of the TestRail section
        :param title: title of the test case
        :return: response from TestRail API containing the newly created test case
        """
        if not section_id or section_id is None:
            raise TestRailSectionException("Invalid section_id.")

        if type(section_id) not in [int, float]:
            raise TestRailSectionException("section_id must be an int or float.")

        if section_id <= 0:
            raise TestRailSectionException("section_id must be > 0.")

        try:
            self.get_section(section_id)["parent_id"] is not None
        except IndexError:
            raise TestRailSectionException("parent_id must not be None as that would assign a test case directly to a sprint.")

        if not title or title is None:
            raise TestRailNewEntityException("Test case title required.")

        data = dict(title=title)

        result = None
        try:
            result = self.client.send_post("add_case/{}".format(section_id), data)
        except E.HTTPError as httpe:
            print(httpe, "- Failed to add test case. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_post("add_case/{}".format(section_id), data)
            except E.HTTPError as httpe:
                print(httpe, "- Failed to add test case.")
        finally:
            return result