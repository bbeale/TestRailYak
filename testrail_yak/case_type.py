#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError


class CaseType(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_case_types(self):
        """Returns a list of available case types. """
        try:
            result = self.client.send_get(f"get_case_types")
        except APIError as error:
            raise error
        else:
            return result
