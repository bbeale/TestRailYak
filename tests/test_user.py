#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testrail_yak import User
from lib.testrail import APIClient
from tests import reqmock, BASEURL


client = APIClient(BASEURL)
u = User(client)


def test_get_user(reqmock):
    user_id = 1
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_user/{user_id}",
        status_code=200,
        text='''{
            "email": "alexis@example.com",
            "id": 1,
            "is_active": true,
            "name": "Alexis Gonzalez"
        }''')

    res = u.get_user(user_id=user_id)
    assert res is not None
    assert type(res) == dict
    assert "email" in res.keys()
    assert "id" in res.keys()
    assert "is_active" in res.keys()
    assert "name" in res.keys()


def test_get_user_by_email(reqmock):
    email = "alexis@example.com"
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_user_by_email&email={email}",
        status_code=200,
        text='''{
            "email": "alexis@example.com",
            "id": 1,
            "is_active": true,
            "name": "Alexis Gonzalez"
        }''')

    res = u.get_user_by_email(email_addr=email)
    assert res is not None
    assert type(res) == dict
    assert "email" in res.keys()
    assert res["email"] == email


def test_get_users(reqmock):
    reqmock.get(f"{BASEURL}/index.php?/api/v2/get_users",
        status_code=200,
        text='''[{
            "email": "alexis@example.com",
            "id": 1,
            "is_active": true,
            "name": "Alexis Gonzalez"
        }]''')

    res = u.get_users()
    assert res is not None
    assert type(res) == list
    assert type(res[0]) == dict
