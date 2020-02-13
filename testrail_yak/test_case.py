#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .exception import TestRailException, TestRailValidationException


class TestCase:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_cases(self, project_id):
        """Get a list of test cases associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test cases
        """
        if not project_id or project_id is None:
            raise TestRailValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestRailValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise TestRailValidationException("[*] project_id must be > 0")

        try:
            result = self.client.send_get("get_cases/{}".format(project_id))
        except TestRailException("[!] Failed to get test cases.") as error:
            raise error
        else:
            return result

    def get_test_case(self, case_id):
        """Get a test case by case_id.

        :param case_id: ID of the test case
        :return: response from TestRail API containing the test cases
        """
        if not case_id or case_id is None:
            raise TestRailValidationException("[*] Invalid case_id")

        if type(case_id) not in [int, float]:
            raise TestRailValidationException("[*] case_id must be an int or float")

        if case_id <= 0:
            raise TestRailValidationException("[*] case_id must be > 0")

        try:
            result = self.client.send_get("get_case/{}".format(case_id))
        except TestRailException("[!] Failed to get test case.") as error:
            raise error
        else:
            return result

    def add_test_case(self, section_id, title):
        """Add a test case to a project by section_id.

        :param section_id: ID of the TestRail section
        :param title: title of the test case
        :return: response from TestRail API containing the newly created test case
        """
        if not section_id or section_id is None:
            raise TestRailValidationException("[*] Invalid section_id.")

        if type(section_id) not in [int, float]:
            raise TestRailValidationException("[*] section_id must be an int or float.")

        if section_id <= 0:
            raise TestRailValidationException("[*] section_id must be > 0.")

        if not title or title is None:
            raise TestRailValidationException("[*] Test case title required.")

        data = dict(title=title)

        try:
            result = self.client.send_post("add_case/{}".format(section_id), data)
        except TestRailException("[!] Failed to add new test case.") as error:
            raise error
        else:
            return result
