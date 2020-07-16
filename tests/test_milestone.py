#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Milestone
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
m = Milestone(client)


def test_get_milestone(reqmock):
    reqmock.get()


def test_get_milestones(reqmock):
    reqmock.get()


def test_add_milestone(reqmock):
    reqmock.post()


def test_update_milestone(reqmock):
    reqmock.post()


def test_delete_milestone(reqmock):
    reqmock.post()
