#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .exception import TestRailException, TestRailValidationException


class TestSuite:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_suites(self, project_id):
        """Get a list of test suites associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test suites
        """
        if not project_id or project_id is None:
            raise TestRailValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestRailValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise TestRailValidationException("[*] project_id must be > 0")

        try:
            result = self.client.send_get("get_suites/{}".format(project_id))
        except TestRailException("[!] Failed to get test suites.") as error:
            raise error
        else:
            return result

    def get_test_suite(self, suite_id):
        """Get a test suite by suite_id.

        :param suite_id: ID of the test suite
        :return: response from TestRail API containing the test suites
        """
        if not suite_id or suite_id is None:
            raise TestRailValidationException("[*] Invalid suite_id")

        if type(suite_id) not in [int, float]:
            raise TestRailValidationException("[*] suite_id must be an int or float")

        if suite_id <= 0:
            raise TestRailValidationException("[*] suite_id must be > 0")

        try:
            result = self.client.send_get("get_suite/{}".format(suite_id))
        except TestRailException("[!] Failed to get test suite.") as error:
            raise error
        else:
            return result

    def add_test_suite(self, project_id, name, description):
        """Add a new test suite to a TestRail project.

        :param project_id: ID of the TestRail project
        :param name: name of the new TestRail test suite
        :param description: description of the test suite
        :return: response from TestRail API containing the newly created test suite
        """
        if not project_id or project_id is None:
            raise TestRailValidationException("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise TestRailValidationException("[*] project_id must be an int or float")

        if project_id <= 0:
            raise TestRailValidationException("[*] project_id must be > 0")

        if not name or name is None:
            raise TestRailValidationException("[*] Invalid suite name. Unable to add test suite.")

        if not description or description is None:
            raise TestRailValidationException("[*] Invalid description. Unable to add test suite.")

        data = dict(name=name, description=description)

        try:
            result = self.client.send_post("add_suite/{}".format(project_id), data)
        except TestRailException("[!] Failed to add new test suite.") as error:
            raise error
        else:
            return result
