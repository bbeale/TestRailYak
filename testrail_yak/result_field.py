#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError


class ResultField(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_result_fields(self):
        try:
            result = self.client.send_get("get_result_fields")
        except APIError as error:
            raise error
        else:
            return result
