#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests_mock
import pytest


@pytest.fixture
def reqmock():
    with requests_mock.Mocker() as m:
        yield m
