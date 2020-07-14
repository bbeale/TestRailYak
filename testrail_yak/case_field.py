#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError
from marshmallow import Schema, fields, ValidationError


class CaseField(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_case_fields(self):
        """Returns a list of available test case custom fields. """
        try:
            result = self.client.send_get(f"get_case_fields")
        except APIError as error:
            raise error
        else:
            return result

    def add_case_field(self, data: dict):
        """Creates a new test case custom field. """

        try:
            data = CaseFieldSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_case_field", data=data)
            except APIError as error:
                raise error
            else:
                return result


class CaseFieldSchema(Schema):
    type = fields.Str(required=True)
    name = fields.Str(required=True)
    label = fields.Str(required=True)
    description = fields.Str()
    include_all = fields.Bool()
    template_ids = fields.List(fields.Int())
    configs = fields.Dict()
