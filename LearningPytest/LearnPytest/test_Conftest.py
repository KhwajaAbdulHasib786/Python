import pytest

@pytest.fixture(autouse=True)

def setup():
    print("lunch Browser")
    print("Login")
    print("Browse Product")
    yield
    print("logoff")
    print("close browser")