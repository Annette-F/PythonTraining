import pytest
from fixture.adbook_application import Adbook_application


@pytest.fixture()
def adbook_app(request):
    adbook_fixture = Adbook_application()
    request.addfinalizer(adbook_fixture.adbook_destroy)
    return adbook_fixture
