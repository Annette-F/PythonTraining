# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='Alexander', lastname='Pyshkin', company='Company LLC', address='Saint-Petersburg',
                      phonehome='9876543210', email='alex@mal.com')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

