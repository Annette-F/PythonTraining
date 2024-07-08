# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_edit_first_contact(adbook_app):
    adbook_app.adbook_session.login("admin", "secret")
    adbook_app.addressbook.edit(Addressbook("Sergei", "Vasilievich", "Rakhmaninov", "Composer", "Music", "Philharmonic Hall",
                                "Novgorod", "1472583690", "7418529630", "112233440", "556677889",
                                "serg@mal.com", "serg2@mail.com", "serg3@mail.com", "http://www.rakhmaniniv.com", "10",
                                "May", "1973", "20", "March", "1975", "New-York", "Beverly Hills", "notes"))
    adbook_app.adbook_session.logout()