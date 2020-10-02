import pytest

@pytest.fixture(scope="module")
def login():
    print("login")
    yield
    print("exit login")

@pytest.fixture(scope="module")
def pp():
    print("pp")
    pytest.assume(2==2)

def test_one(pp):
    print("case_one")
    assert 'a' in 'abc'
def test_two(login):
    print("exit pp")

def test_case0(login):

    print("case0")
    print("case_two")
    assert 'a' in 'abc'

def test_three(pp):
    print("case_three")
    assert 'a' in 'abc'

def test_forth():
    print("case_forth")
    assert 'a' in 'abc'
if __name__ == '__main__':
    pytest.main(["-v","--html=report.html","main.py"])






