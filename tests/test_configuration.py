#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import Configuration
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
conf = Configuration(client)


def test_get_configs(reqmock):
    reqmock.get()


def test_add_config_group(reqmock):
    reqmock.post()


def test_add_config(reqmock):
    reqmock.post()


def test_update_config_group(reqmock):
    reqmock.post()


def test_update_config(reqmock):
    reqmock.post()


def test_delete_config_group(reqmock):
    reqmock.post()


def test_delete_config(reqmock):
    reqmock.post()
