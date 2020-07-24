#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .lib.testrail import APIClient
from .attachment import Attachment
from .case import TestCase
from .case_field import CaseField
from .case_type import CaseType
from .configuration import Configuration
from .milestone import Milestone
from .plan import TestPlan
from .priority import Priority
from .project import Project
from .report import Report
from .result import TestResult
from .result_field import ResultField
from .run import TestRun
from .section import Section
from .status import Status
from .suite import TestSuite
from .template import Template
from .test import Test
from .user import User


class TestRailYak(APIClient):
    """A class to build on top of Gurock's Python interface

    https://github.com/gurock/testrail-api.git
    """
    def __init__(self, url, uname, passwd):

        super().__init__(url)

        self.client             = APIClient(url)
        self.client.user        = uname
        self.client.password    = passwd
        self.attachment         = Attachment(self.client)
        self.test_case          = TestCase(self.client)
        self.case_field         = CaseField(self.client)
        self.case_type          = CaseType(self.client)
        self.config             = Configuration(self.client)
        self.milestone          = Milestone(self.client)
        self.test_plan          = TestPlan(self.client)
        self.project            = Project(self.client)
        self.section            = Section(self.client)
        self.test               = Test(self.client)
        self.test_run           = TestRun(self.client)
        self.test_suite         = TestSuite(self.client)
        self.user               = User(self.client)
        self.test_result        = TestResult(self.client)
