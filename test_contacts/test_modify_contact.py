# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Liza', lastname='Swan', address='Texas'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='Sergei', lastname='Rakhmaninov', company='Philharmonic Hall', address='Novgorod',
                      phonehome='7418529630', email='serg@mal.com')
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='', lastname=''))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname='Sergei')
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname_by_index(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='Mikhail', lastname='Lomonosov', company='University'))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname='Rakhmaninov')
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
