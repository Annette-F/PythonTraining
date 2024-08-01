# -*- coding: utf-8 -*-
from model.addressbook import Addressbook


def test_edit_first_contact(adbook_app):
    adbook_app.adbook_session.login(username="admin", password="secret")
    adbook_app.addressbook.edit(
        Addressbook(firstname="Sergei", middlename="Vasilievich", lastname="Rakhmaninov", nickname="Composer",
                    title="Music", company="Philharmonic Hall",
                    address="Novgorod", phonehome="1472583690", mobile="7418529630", phonework="112233440",
                    fax="556677889",
                    email="serg@mal.com", email2="serg2@mail.com", email3="serg3@mail.com",
                    homepage="http://www.rakhmaniniv.com", bday="10",
                    bmonth="May", byear="1973", aday="20", amonth="March", ayear="1975", address2="New-York",
                    home="Beverly Hills", note="notes"))
    adbook_app.adbook_session.logout()
