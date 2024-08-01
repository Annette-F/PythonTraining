def test_delete_first_contact_from_modify_page(adbook_app):
    adbook_app.addressbook.delete_from_modify_page()


def test_del_first_contact(adbook_app):
    adbook_app.addressbook.del_one_contact()
