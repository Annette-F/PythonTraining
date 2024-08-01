import pytest
from fixture.adbook_application import Adbook_application

adbook_fixture = None


@pytest.fixture
def adbook_app(request):
    global adbook_fixture
    if adbook_fixture is None:
        adbook_fixture = Adbook_application()
        adbook_fixture.adbook_session.login(username="admin", password="secret")
    else:
        if not adbook_fixture.is_valid():
            adbook_fixture = Adbook_application()
            adbook_fixture.adbook_session.login(username="admin", password="secret")
    return adbook_fixture


@pytest.fixture(scope='session', autouse=True)
def adbook_stop(request):
    def ad_fin():
        adbook_fixture.adbook_session.logout()
        adbook_fixture.adbook_destroy()

    request.addfinalizer(ad_fin)
    return adbook_fixture
