# -*- coding: utf-8 -*-
from sys import maxsize

from model.addressbook import Addressbook


def test_add_new_contact(adbook_app):
    old_contacts = adbook_app.addressbook.get_contact_list()
    contact = Addressbook(firstname="Alexander", lastname="Pyshkin", company="Company LLC", address="Saint-Petersburg",
                    phonehome="9876543210", email="alex@mal.com")
    adbook_app.addressbook.add(contact)
    assert len(old_contacts) + 1 == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)


# def test_add_second_contact(adbook_app):
#     old_contacts = adbook_app.addressbook.get_contact_list()
#     contact = Addressbook(firstname="", lastname="", company="", address="", phonehome="", email="")
#     adbook_app.addressbook.add(contact)
#     new_contacts = adbook_app.addressbook.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)