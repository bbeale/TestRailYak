#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Project
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
p = Project(client)


def test_get_project(reqmock):
    reqmock.get()


def test_get_projects(reqmock):
    reqmock.get()


def test_add_project(reqmock):
    reqmock.post()


def test_update_project(reqmock):
    reqmock.post()


def test_delete_project(reqmock):
    reqmock.post()
