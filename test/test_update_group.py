from model.group import Group


def test_update_group(app):
    app.group.update(Group(name="name2", header="header2", footer="footer2"))
