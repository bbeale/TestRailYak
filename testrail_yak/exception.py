#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .testrail import APIError


# TestRail
class TestRailException(APIError):
    pass


class TestRailValidationException(TestRailException, ValueError):
    pass
