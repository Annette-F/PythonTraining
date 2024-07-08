from model.addressbook import Addressbook


def test_delete_first_contact_from_edit_page(adbook_app):
    adbook_app.adbook_session.login("admin", "secret")
    adbook_app.addressbook.delete_from_edit_page()
    adbook_app.adbook_session.logout()


def test_del_first_contact(adbook_app):
    adbook_app.adbook_session.login("admin", "secret")
    adbook_app.addressbook.del_one_contact()
    adbook_app.adbook_session.logout()

