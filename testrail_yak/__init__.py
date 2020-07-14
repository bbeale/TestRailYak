#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIClient
from .attachment import Attachment
from .project import Project
from .section import Section
from .test import Test
from .case import TestCase
from .plan import TestPlan
from .run import TestRun
from .suite import TestSuite
from .user import User
from .result import TestResult


class TestRailYak(APIClient):
    """A class to build on top of Gurock's Python interface

    https://github.com/gurock/testrail-api.git
    """
    def __init__(self, url, uname, passwd):

        super().__init__(url)

        self.client             = APIClient(url)
        self.client.user        = uname
        self.client.password    = passwd
        self.project            = Project(self.client)
        self.section            = Section(self.client)
        self.test               = Test(self.client)
        self.test_case          = TestCase(self.client)
        self.test_plan          = TestPlan(self.client)
        self.test_run           = TestRun(self.client)
        self.test_suite         = TestSuite(self.client)
        self.user               = User(self.client)
        self.test_result        = TestResult(self.client)
