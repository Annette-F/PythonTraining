# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_add_new_contact(adbook_app):
    adbook_app.adbook_session.login(username="admin", password="secret")
    adbook_app.addressbook.add(
        Addressbook(firstname="Alexander", middlename="Sergeevich", lastname="Pyshkin", nickname="Poet", title="Title",
                    company="Company LLC",
                    address="Saint-Petersburg", phonehome="1234567890", mobile="9876543210", phonework="1472583690",
                    fax="3692580147",
                    email="alex@mal.com", email2="alex2@mail.com", email3="alex3@mail.com",
                    homepage="http://www.pyshkin.com", bday="17",
                    bmonth="November", byear="1994", aday="20", amonth="August", ayear="1999", address2="Moscow",
                    home="my home", note="note"))
    adbook_app.adbook_session.logout()


def test_add_second_contact(adbook_app):
    adbook_app.adbook_session.login(username="admin", password="secret")
    adbook_app.addressbook.add(Addressbook(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                           address="", phonehome="", mobile="", phonework="", fax="",
                                           email="", email2="", email3="", homepage="", bday="10",
                                           bmonth="May", byear="1973", aday="20", amonth="March", ayear="1975",
                                           address2="", home="", note=""))
    adbook_app.adbook_session.logout()
