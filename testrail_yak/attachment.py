#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError


class Attachment(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def attach_to_plan(self, plan_id: int):
        """Adds an attachment to a test plan. The maximum allowable upload size is set to 256mb. """
        try:
            result = self.client.send_post(f"add_attachment_to_plan/{plan_id}")
        except APIError as error:
            raise error
        else:
            return result

    def attach_to_plan_entry(self, plan_id: int, entry_id: int):
        """Adds an attachment to a test plan entry. The maximum allowable upload size is set to 256mb. """
        try:
            result = self.client.send_post(f"add_attachment_to_plan_entry/{plan_id}/{entry_id}")
        except APIError as error:
            raise error
        else:
            return result

    def attach_to_result(self, result_id: int):
        """Adds attachment to a result based on the result ID. The maximum allowable upload size is set to 256mb. """
        try:
            result = self.client.send_post(f"add_attachment_to_result/{result_id}")
        except APIError as error:
            raise error
        else:
            return result

    def attach_to_run(self, run_id: int):
        """Adds attachment to test run. The maximum allowable upload size is set to 256mb. """
        try:
            result = self.client.send_post(f"add_attachment_to_run/{run_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_case_attachments(self, case_id: int):
        """Returns a list of attachments for a test case. """
        try:
            result = self.client.send_get(f"get_attachments_for_case/{case_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_plan_attachments(self, plan_id: int):
        """Returns a list of attachments for a test plan. """
        try:
            result = self.client.send_get(f"get_attachments_for_plan/{plan_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_plan_entry_attachments(self, plan_id: int, entry_id: int):
        """Returns a list of attachments for a test plan entry. """
        try:
            result = self.client.send_get(f"get_attachments_for_plan_entry/{plan_id}/{entry_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_run_attachments(self, run_id: int):
        """Returns a list of attachments for a test run. """
        try:
            result = self.client.send_get(f"get_attachments_for_run/{run_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_test_attachments(self, test_id: int):
        """Returns a list of attachments for a test’s results. """
        try:
            result = self.client.send_get(f"get_attachments_for_test/{test_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_attachment(self, attachment_id: int):
        """Retrieves the requested file identified by :attachment_id. """
        try:
            result = self.client.send_get(f"get_attachment/{attachment_id}")
        except APIError as error:
            raise error
        else:
            return result

    def delete_attachment(self, attachment_id: int):
        """Deletes the specified attachment identified by :attachment_id. """
        try:
            result = self.client.send_get(f"delete_attachment/{attachment_id}")
        except APIError as error:
            raise error
        else:
            return result
