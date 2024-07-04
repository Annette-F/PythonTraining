# -*- coding: utf-8 -*-
from model.addressbook import Addressbook
import pytest
from fixture.adbook_application import Adbook_application


@pytest.fixture()
def adbook_app(request):
    adbook_fixture = Adbook_application()
    request.addfinalizer(adbook_fixture.adbook_destroy)
    return adbook_fixture


def test_add_new_contact(adbook_app):
    adbook_app.adbook_session.login("admin", "secret")
    adbook_app.addressbook.add(Addressbook("Alexander", "Sergeevich", "Pyshkin", "Poet", "Title", "Company LLC",
                                "Saint-Petersburg", "1234567890", "9876543210", "1472583690", "3692580147",
                                "alex@mal.com", "alex2@mail.com", "alex3@mail.com", "http://www.pyshkin.com", "17",
                                "November", "1994", "20", "August", "1999", "Moscow", "my home", "note"))
    adbook_app.adbook_session.logout()
