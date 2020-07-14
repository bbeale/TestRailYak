#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.testrail import APIError


class Priority(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_priorities(self):
        try:
            result = self.client.send_get("get_priorities")
        except APIError as error:
            raise error
        else:
            return result
