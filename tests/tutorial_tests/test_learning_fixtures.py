import pytest


@pytest.fixture()
def setup1():
    print("\nSetup1")
    yield
    print("\n Teardown")


@pytest.fixture()
def setup2(request):
    print("\n setup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("\ntest1")
    assert True

@pytest.mark.usefixtures("setup2")
def test2(setup2):
    print("\ntest2")