#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError
from marshmallow import Schema, fields, ValidationError


class TestCase(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_test_cases(self, project_id: int):
        """Get a list of test cases associated with a given project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the test cases
        """
        try:
            result = self.client.send_get(f"get_cases/{project_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_test_case(self, case_id: int):
        """Get a test case by case_id.

        :param case_id: ID of the test case
        :return: response from TestRail API containing the test cases
        """
        try:
            result = self.client.send_get(f"get_case/{case_id}")
        except APIError as error:
            raise error
        else:
            return result

    def add_test_case(self, section_id: int, data: dict):
        """Add a test case to a project by section_id.

        :param section_id: ID of the TestRail section
        :param data:
        :return: response from TestRail API containing the newly created test case
        """
        try:
            data = TestCaseSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_case/{section_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def update_test_case(self, case_id: int, data: dict):
        """Update a test case.

        :param case_id: ID of the TestRail test case
        :param data:
        :return: response from TestRail API containing the newly created test case
        """
        try:
            data = TestCaseUpdateSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"update_case/{case_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result


class TestCaseSchema(Schema):
    title = fields.Str(required=True)
    template_id = fields.Int()
    type_id = fields.Int()
    priority_id = fields.Int()
    estimate = fields.Str()
    milestone_id = fields.Int()
    refs = fields.Str()


class TestCaseUpdateSchema(Schema):
    title = fields.Str()
    template_id = fields.Int()
    type_id = fields.Int()
    priority_id = fields.Int()
    estimate = fields.Str()
    milestone_id = fields.Int()
    refs = fields.Str()
