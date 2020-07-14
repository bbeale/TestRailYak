#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError
from marshmallow import Schema, fields, ValidationError


class Project(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def _suite_mode(self, project_id: int):
        """Figure out the suite_mode value of a given project.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the project
        """
        try:
            p = self.get_project(project_id)
        except APIError as error:
            raise error
        else:
            return p["suite_mode"]

    def get_project(self, project_id: int):
        """Get a single project from the TestRail API by passing in its project_id.

        :param project_id: project ID of the TestRail project
        :return: response from TestRail API containing the project
        """
        try:
            result = self.client.send_get(f"get_project/{project_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_projects(self):
        """Get all projects from the TestRail API."""
        try:
            result = self.client.send_get("get_projects")
        except APIError as error:
            raise error
        else:
            return result

    def add_project(self, data: dict):
        """Add a new project to TestRail.

        :param data: request data dictionary
        :return: response from TestRail API containing the newly created project
        """
        try:
            data = ProjectSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post("add_project", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def update_project(self, project_id: int, data: dict):
        """Updates an existing project (admin status required; partial updates are supported, i.e. you can submit and update specific fields only). """
        try:
            data = ProjectUpdateSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"update_project/{project_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def delete_project(self, project_id: int):
        """Deletes an existing project (admin status required). """
        try:
            result = self.client.send_post(f"delete_project/{project_id}")
        except APIError as error:
            raise error
        else:
            return result


class ProjectSchema(Schema):
    name                = fields.Str(required=True)
    announcement        = fields.Str()
    show_announcement   = fields.Bool()
    suite_mode          = fields.Int()


class ProjectUpdateSchema(Schema):
    name                = fields.Str()
    announcement        = fields.Str()
    show_announcement   = fields.Bool()
    is_completed        = fields.Bool()
