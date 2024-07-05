from model.group import Group


def test_update_group(app):
    app.session.login("admin", "secret")
    app.group.update(Group("name2", "header2", "footer2"))
    app.session.logout()