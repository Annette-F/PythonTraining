from random import randrange

from model.addressbook import Addressbook


# def test_delete_first_contact_from_modify_page(adbook_app):
#     if adbook_app.addressbook.count() == 0:
#         adbook_app.addressbook.add(Addressbook(firstname='Alex', lastname='Subbotin'))
#     old_contacts = adbook_app.addressbook.get_contact_list()
#     adbook_app.addressbook.delete_from_modify_page()
#     new_contacts = adbook_app.addressbook.get_contact_list()
#     assert len(old_contacts) - 1 == len(new_contacts)


def test_del_some_contact(adbook_app):
    if adbook_app.addressbook.count() == 0:
        adbook_app.addressbook.create(Addressbook(firstname='Tom', lastname='Soyer'))
    old_contacts = adbook_app.addressbook.get_contact_list()
    index = randrange(len(old_contacts))
    adbook_app.addressbook.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == adbook_app.addressbook.count()
    new_contacts = adbook_app.addressbook.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
