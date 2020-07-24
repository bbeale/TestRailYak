#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .lib.testrail import APIError


class Status(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_statuses(self):
        """Returns a list of available test statuses. """
        try:
            result = self.client.send_get("get_statuses")
        except APIError as error:
            raise error
        else:
            return result
