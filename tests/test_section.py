#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Section
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
s = Section(client)


def test_get_section(reqmock):
    reqmock.get()


def test_get_sections(reqmock):
    reqmock.get()


def test_add_sprint_section(reqmock):
    reqmock.post()


def test_add_story_section(reqmock):
    reqmock.post()


def test_update_section(reqmock):
    reqmock.post()


def test_delete_section(reqmock):
    reqmock.post()
