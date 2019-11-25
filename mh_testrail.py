#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.testrail import APIClient
from src.project import Project
from src.section import Section
from src.test import Test
from src.test_case import TestCase
from src.test_plan import TestPlan
from src.test_run import TestRun
from src.test_suite import TestSuite
from src.user import User


class mhTestRail(APIClient):

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
