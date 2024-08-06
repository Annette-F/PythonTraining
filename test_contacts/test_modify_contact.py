# -*- coding: utf-8 -*-
from model.addressbook import Addressbook
from random import randrange


def test_modify_contact_by_index(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='Liza', lastname='Swan', address='Texas'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Addressbook(firstname='Sergei', lastname='Rakhmaninov', company='Philharmonic Hall', address='Novgorod',
                          phonehome='7418529630', email='serg@mal.com')
    contact.id = old_contacts[index].id
    adbook_app.addressbook.modify_contact_by_index(index, contact)
    assert len(old_contacts) == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)


def test_modify_contact_firstname_by_index(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='', lastname=''))
    old_contacts = adbook_app.addressbook.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Addressbook(firstname='Sergei')
    contact.id = old_contacts[index].id
    adbook_app.addressbook.modify_contact_by_index(index, contact)
    assert len(old_contacts) == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)


def test_modify_contact_lastname_by_index(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='Mikhail', lastname='Lomonosov', company='University'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Addressbook(lastname='Rakhmaninov')
    contact.id = old_contacts[index].id
    adbook_app.addressbook.modify_contact_by_index(index, contact)
    assert len(old_contacts) == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Addressbook.id_or_max) == sorted(new_contacts, key=Addressbook.id_or_max)
