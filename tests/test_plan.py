#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import TestPlan
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
tp = TestPlan(client)


def test_get_test_plan(reqmock):
    reqmock.get()


def test_get_test_plans(reqmock):
    reqmock.get()


def test_add_test_plan(reqmock):
    reqmock.post()


def test_add_plan_entry(reqmock):
    reqmock.post()


def test_update_plan(reqmock):
    reqmock.post()


def test_update_plan_entry(reqmock):
    reqmock.post()


def test_close_plan(reqmock):
    reqmock.post()


def test_delete_plan(reqmock):
    reqmock.post()


def test_delete_plan_entry(reqmock):
    reqmock.post()
