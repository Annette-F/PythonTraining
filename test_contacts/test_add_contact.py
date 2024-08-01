# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_add_new_contact(adbook_app):
    adbook_app.adbook_session.login(username="admin", password="secret")
    adbook_app.addressbook.add(
        Addressbook(firstname="Alexander", middlename="Sergeevich", lastname="Pyshkin", nickname="Poet",
                    company="Company LLC", address="Saint-Petersburg", mobile="9876543210", email="alex@mal.com",
                    note="note"))
    adbook_app.adbook_session.logout()


def test_add_second_contact(adbook_app):
    adbook_app.adbook_session.login(username="admin", password="secret")
    adbook_app.addressbook.add(Addressbook(firstname="", middlename="", lastname="", nickname="", company="",
                                           address="", mobile="", email="", note=""))
    adbook_app.adbook_session.logout()
