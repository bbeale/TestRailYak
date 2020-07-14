#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError
from marshmallow import Schema, fields, ValidationError


class Section:
    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_section(self, section_id: int):
        """Get test section from a test suite by section_id.

        :param section_id: section ID to grab section from
        :return: response from TestRail API containing the test section
        """
        try:
            result = self.client.send_get(f"get_section/{section_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_sections(self, project_id: int, suite_id=None):
        """Get a list of test sections associated with a project_id and an optional suite_id

        :param project_id:
        :param suite_id:
        :return: response from TestRail API containing the collection of sections
        """

        if suite_id is not None:
            if type(suite_id) not in [int, float] or suite_id <= 0:
                raise ValidationError("[*] Invalid suite_id.")

            try:
                result = self.client.send_get(f"get_sections/{project_id}&suite_id={suite_id}")
            except APIError as error:
                raise error

        else:
            try:
                result = self.client.send_get(f"get_sections/{project_id}")
            except APIError as error:
                raise error

        return result

    def add_sprint_section(self, project_id: int, data: dict):
        """Add a new section representing a "sprint" to a TestRail project.

        For readability, this separate method is just for adding parent sections (Jira sprints) vs child sections (Jira stories).

        To populate a new child section with a Jira story, use add_story_section() and give it the id value returned here.

        :param project_id: project ID of the TestRail project
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created test section
        """
        try:
            data = SectionSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_section/{project_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def add_story_section(self, project_id: int, data: dict):
        """Add a new section representing a "story" to a TestRail project.

        This section will be assigned to a parent/child relationship with a parent section, thus parent_id is required.

        Use the id value returned by add_sprint_section as the parent_id.

        Because of this parent id requirement, no suite_id will be needed. If it is ever used in the future, add_sprint_section is the more appropriate place for it.

        :param project_id: project ID of the TestRail project
        :param data: request data dictionary
        :return: response from TestRail API containing the newly created test section
        """
        if "parent_id" not in data.keys():
            raise ValidationError("[*] parent_id must be provided")
        try:
            data = SectionSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_section/{project_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def update_section(self, section_id: int, data: dict):
        """Updates an existing section (partial updates are supported, i.e. you can submit and update specific fields only). """
        try:
            data = SectionUpdateSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"update_section/{section_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def delete_section(self, section_id: int):
        """Deletes an existing section. """
        try:
            result = self.client.send_post(f"delete_section/{section_id}")
        except APIError as error:
            raise error
        else:
            return result


class SectionSchema(Schema):
    description = fields.Str()
    suite_id = fields.Int()
    parent_id = fields.Int()
    name = fields.Str(required=True)

class SectionUpdateSchema(Schema):
    description = fields.Str()
    name = fields.Str()
