#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import User
from lib.testrail import APIClient
from tests import reqmock


client = APIClient("http://example.testrail.com")
u = User(client)


def test_get_user(reqmock):
    reqmock.get()


def test_get_user_by_email(reqmock):
    reqmock.get()


def test_get_users(reqmock):
    reqmock.get()
