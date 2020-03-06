#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError
from marshmallow import Schema, fields, ValidationError


class TestResult:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_results(self, test_id):
        """Get test results for a given test_id.

        :param test_id:
        :return:
        """
        if not test_id or test_id is None:
            raise APIValidationError("[!] Invalid test_id.")

        if type(test_id) not in [int, float]:
            raise APIValidationError("[!] test_id must be an int or float.")

        if test_id <= 0:
            raise APIValidationError("[*] test_id must be > 0")

        try:
            result = self.client.send_get("get_results/{}".format(test_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_testcase_test_results(self, run_id, case_id):
        """Get test results for a given test case.

        :param run_id:
        :param case_id:
        :return:
        """
        if not run_id or run_id is None:
            raise APIValidationError("[!] Invalid run_id.")

        if type(run_id) not in [int, float]:
            raise APIValidationError("[!] run_id must be an int or float.")

        if run_id <= 0:
            raise APIValidationError("[*] run_id must be > 0.")

        if not case_id or case_id is None:
            raise APIValidationError("[!] Invalid case_id.")

        if type(case_id) not in [int, float]:
            raise APIValidationError("[!] case_id must be an int or float.")

        if case_id <= 0:
            raise APIValidationError("[*] case_id must be > 0.")

        try:
            result = self.client.send_get("get_results_for_case/{}/{}".format(run_id, case_id))
        except APIError as error:
            raise error
        else:
            return result

    def get_testrun_test_results(self, run_id):
        """Get test results for a given test run.

        :param run_id:
        :return:
        """
        if not run_id or run_id is None:
            raise APIValidationError("[!] Invalid run_id.")

        if type(run_id) not in [int, float]:
            raise APIValidationError("[!] run_id must be an int or float.")

        if run_id <= 0:
            raise APIValidationError("[*] run_id must be > 0.")

        try:
            result = self.client.send_get("get_results_for_run/{}".format(run_id))
        except APIError as error:
            raise error
        else:
            return result
