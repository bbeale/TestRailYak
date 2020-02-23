# TestRailYak

A Python library for interacting with the TestRail REST API.

Essentially, another layer on top of gurock's Python interface: https://github.com/gurock/testrail-api.git

Install (dev version):

`pip install -i https://test.pypi.org/simple/ testrail-yak`

Use:

```
from testrail_yak import TestRailYak

testrail = TestRailYak()
projects = testrail.project.get_projects(<testrail_url>, <username>, <password>)
```
