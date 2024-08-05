# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_modify_first_contact(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='Liza', lastname='Swan', address='Texas'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    contact = Addressbook(firstname="Sergei", lastname="Rakhmaninov", company="Philharmonic Hall", address="Novgorod",
                    phonehome="7418529630", email="serg@mal.com")
    adbook_app.addressbook.modify_first_contact(contact)
    assert len(old_contacts) == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)


def test_modify_first_contact_firstname(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='', lastname=''))
    old_contacts = adbook_app.addressbook.get_contact_list()
    contact = Addressbook(firstname="Sergei")
    adbook_app.addressbook.modify_first_contact(contact)
    assert len(old_contacts) == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)

def test_modify_first_contact_lastname(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='Mikhail', lastname='Lomonosov', company='University'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    contact = Addressbook(lastname="Rakhmaninov")
    adbook_app.addressbook.modify_first_contact(contact)
    assert len(old_contacts) == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)