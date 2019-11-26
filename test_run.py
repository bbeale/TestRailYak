#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail_exception import (
    TestRailProjectException,
    TestRailTestRunException,
    TestRailNewEntityException
)

from urllib import error as E
import time


class TestRun:

    __module__ = "mh_testrail"

    def __init__(self, api):
        self.client = api

    def get_test_runs(self, project_id):
        """Get a list of test runs associated with a given project_id.

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
            result = self.client.send_get("get_runs/{}".format(project_id))
        except E.HTTPError as httpe:
            print(httpe, "- Failed to get test runs. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_runs/{}".format(project_id))
            except E.HTTPError as httpe:
                print(httpe, "- Failed to get test runs.")
        finally:
            return result

    def get_test_run(self, run_id):
        """Get a test run by run_id.

        :param run_id: ID of the test run
        :return: response from TestRail API containing the test cases
        """
        if not run_id or run_id is None:
            raise TestRailTestRunException("Invalid run_id")

        if type(run_id) not in [int, float]:
            raise TestRailTestRunException("run_id must be an int or float")

        if run_id <= 0:
            raise TestRailTestRunException("run_id must be > 0")

        result = None
        try:
            result = self.client.send_get("get_run/{}".format(run_id))
        except E.HTTPError as httpe:
            print(httpe, "- Failed to get test run. Retrying")
            time.sleep(3)
            try:
                result = self.client.send_get("get_run/{}".format(run_id))
            except E.HTTPError as httpe:
                print(httpe, "- Failed to get test run.")
        finally:
            return result

    def add_test_run(self, project_id, name):
        """Add a test run to a project.

        :param project_id: ID of the TestRail project
        :param name: name of the test case
        :return: response from TestRail API containing the newly created test run
        """
        if not project_id or project_id is None:
            raise TestRailProjectException("Invalid project_id.")

        if type(project_id) not in [int, float]:
            raise TestRailProjectException("project_id must be an int or float.")

        if project_id <= 0:
            raise TestRailProjectException("project_id must be > 0.")

        if not name or name is None:
            raise TestRailNewEntityException("Test run name value required.")

        data = dict(name=name, include_all=True)

        result = None
        try:
            result = self.client.send_post("add_run/{}".format(project_id), data)
        except E.HTTPError as httpe:
            print(httpe, "- Failed to add test run. Retrying.")
            time.sleep(3)
            try:
                result = self.client.send_post("add_run/{}".format(project_id), data)
            except E.HTTPError as httpe:
                print(httpe, "- Failed to add test run.")
        finally:
            return result
