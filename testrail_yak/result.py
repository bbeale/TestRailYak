#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.testrail import APIError
from lib.schema import ResultSchema, TestCaseResultSchema, SchemaError


class TestResult:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_results(self, test_id: int):
        """Get test results for a given test_id.

        :param test_id:
        :return:
        """
        try:
            result = self.client.send_get(f"get_results/{test_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_testcase_results(self, run_id: int, case_id: int):
        """Get test results for a given test case.

        :param run_id:
        :param case_id:
        :return:
        """
        try:
            result = self.client.send_get(f"get_results_for_case/{run_id}/{case_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_testrun_results(self, run_id: int):
        """Get test results for a given test run.

        :param run_id:
        :return:
        """
        try:
            result = self.client.send_get(f"get_results_for_run/{run_id}")
        except APIError as error:
            raise error
        else:
            return result

    def add_result(self, test_id: int, data: dict):
        """Adds a new test result, comment or assigns a test.

        It’s recommended to use add_results instead if you plan to add results for multiple tests.
        """
        try:
            data = ResultSchema().load(data, partial=True)
        except SchemaError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_result/{test_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def add_testcase_result(self, run_id: int, case_id: int, data: dict):
        """Adds a new test result, comment or assigns a test (for a test run and case combination).

        It’s recommended to use add_results_for_cases instead if you plan to add results for multiple test cases.
        """
        try:
            data = TestCaseResultSchema().load(data, partial=True)
        except SchemaError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_result_for_case/{run_id}/{case_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def add_results(self, run_id: int):
        raise NotImplemented

    def add_testcase_results(self, run_id: int):
        raise NotImplemented
