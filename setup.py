#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
from distutils.core import setup
from textwrap import dedent


setup(name="testrail_yak",
      version="0.0.1",
      packages=["testrail_yak"],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      license=dedent("""\
      Copyright (c) 2019 bbeale

      Permission is hereby granted, free of charge, to any person obtaining a copy
      of this software and associated documentation files (the "Software"), to deal
      in the Software without restriction, including without limitation the rights
      to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
      copies of the Software, and to permit persons to whom the Software is
      furnished to do so, subject to the following conditions:
      
      The above copyright notice and this permission notice shall be included in all
      copies or substantial portions of the Software.
      
      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
      IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
      FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
      AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
      LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
      OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
      SOFTWARE."""),
      description="Python library for interacting with the TestRail API, built on top of gurock\"s",
      long_description=dedent("""\
      Getting Started:
        ----------------
        To use the TestRail API via TestRailYak, install the package either by downloading the source and running
          $ python setup.py install
        or by using pip
          $ pip install testrail_yak
      """),
      author="bbeale",
      setup_requires=['wheel'],
      requires=[
            "urllib3"
      ])
