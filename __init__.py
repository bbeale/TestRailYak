#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .lib.testrail import APIClient
from .project import Project
from .section import Section
from .test import Test
from .test_case import TestCase
from .test_plan import TestPlan
from .test_run import TestRun
from .test_suite import TestSuite
from .user import User


class mhTestRail(APIClient):
    """A class to build on top of Gurock's Python interface

    https://github.com/gurock/testrail-api.git
    """
    def __init__(self, config, base_url):

        super().__init__(base_url)

        self.client             = APIClient(config["url"])
        self.client.user        = config["user"]
        self.client.password    = config["password"]
        self.project            = Project(self.client)
        self.section            = Section(self.client)
        self.test               = Test(self.client)
        self.test_case          = TestCase(self.client)
        self.test_plan          = TestPlan(self.client)
        self.test_run           = TestRun(self.client)
        self.test_suite         = TestSuite(self.client)
        self.user               = User(self.client)
