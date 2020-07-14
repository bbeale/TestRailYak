#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError
from marshmallow import Schema, fields, ValidationError


class Milestone(object):

    __module__ = "testrail_yak"

    def __init__(self, api):
        self.client = api

    def get_milestone(self, milestone_id: int):
        """Returns an existing milestone. """
        try:
            result = self.client.send_get(f"get_milestone/{milestone_id}")
        except APIError as error:
            raise error
        else:
            return result

    def get_milestones(self, project_id: int):
        """Returns the list of milestones for a project. """
        try:
            result = self.client.send_get(f"get_milestones/{project_id}")
        except APIError as error:
            raise error
        else:
            return result

    def add_milestone(self, project_id: int, data: dict):
        """Creates a new milestone. """
        try:
            data = MilestoneSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"add_milestone/{project_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def update_milestone(self, milestone_id: int, data: dict):
        """Updates an existing milestone (partial updates are supported, i.e. you can submit and update specific fields only). """
        try:
            data = MilestoneUpdateSchema().load(data, partial=True)
        except ValidationError as err:
            raise err
        else:
            try:
                result = self.client.send_post(f"update_milestone/{milestone_id}", data=data)
            except APIError as error:
                raise error
            else:
                return result

    def delete_milestone(self, milestone_id: int):
        """ Deletes an existing milestone. """
        try:
            result = self.client.send_post(f"update_milestone/{milestone_id}")
        except APIError as error:
            raise error
        else:
            return result


class MilestoneSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    due_on = fields.Time()
    parent_id = fields.Int()
    start_on = fields.Time()


class MilestoneUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    due_on = fields.Time()
    parent_id = fields.Int()
    start_on = fields.Time()
    is_completed = fields.Bool()
    is_started = fields.Bool()
