#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError, APIValidationError


class Project:

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_projects(self):
        """Get all projects from the TestRail API."""
        try:
            result = self.client.send_get("get_projects")
        except APIError as error:
            raise error
        else:
            return result

    def get_project(self, project_id):
        """Get a single project from the TestRail API by passing in its project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the project
        """
        if not project_id or project_id is None:
            raise APIValidationError("[*] Invalid project_id")

        if type(project_id) not in [int, float]:
            raise APIValidationError("[*] project_id must be an int or float")

        if project_id <= 0:
            raise APIValidationError("[*] project_id must be > 0")

        try:
            result = self.client.send_get("get_project/{}".format(project_id))
        except APIError as error:
            raise error
        else:
            return result

    def add_project(self, name, announcement=None, show_announcement=True, suite_mode=1):
        """Add a new project to TestRail.

        :param name: name of the new TestRail project
        :param announcement: brief description of the TestRail project
        :param show_announcement: a truthy value or True show the announcement, a falsey value or False hides it
        :param suite_mode: suite mode of the project (1 for single suite mode, 2 for single suite + baselines, 3 for multiple suites)
        :return: response from TestRail API containing the newly created project
        """
        if not name or name is None:
            raise APIValidationError("[*] Invalid project name. Unable to create new project.")

        proj_data = dict(
            name                = name,
            announcement        = announcement,
            show_announcement   = show_announcement,
            suite_mode          = suite_mode
        )

        try:
            result = self.client.send_post("add_project", proj_data)
        except APIError as error:
            raise error
        else:
            return result
