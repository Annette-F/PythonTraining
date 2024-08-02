# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_modify_first_contact(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.add(Addressbook(firstname='Liza', lastname='Swan', address='Texas'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    adbook_app.addressbook.modify_first_contact(
        Addressbook(firstname="Sergei", middlename="Vasilievich", lastname="Rakhmaninov", nickname="Composer",
                    company="Philharmonic Hall", address="Novgorod", mobile="7418529630", email="serg@mal.com",
                    note="notes"))
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_firstname(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.add(Addressbook(firstname='', middlename='', lastname=''))
    old_contacts = adbook_app.addressbook.get_contact_list()
    adbook_app.addressbook.modify_first_contact(Addressbook(firstname="Sergei"))
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_first_contact_lastname(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.add(Addressbook(firstname='Mikhail', lastname='Lomonosov', company='University'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    adbook_app.addressbook.modify_first_contact(Addressbook(lastname="Rakhmaninov"))
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
