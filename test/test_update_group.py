from model.group import Group


def test_update_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update(Group(name="name2", header="header2", footer="footer2"))
    app.session.logout()