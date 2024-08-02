# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_add_new_contact(adbook_app):
    old_contacts = adbook_app.addressbook.get_contact_list()
    adbook_app.addressbook.add(
        Addressbook(firstname="Alexander", middlename="Sergeevich", lastname="Pyshkin", nickname="Poet",
                    company="Company LLC", address="Saint-Petersburg", mobile="9876543210", email="alex@mal.com",
                    note="note"))
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_second_contact(adbook_app):
    old_contacts = adbook_app.addressbook.get_contact_list()
    adbook_app.addressbook.add(Addressbook(firstname="", middlename="", lastname="", nickname="", company="",
                                           address="", mobile="", email="", note=""))
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
