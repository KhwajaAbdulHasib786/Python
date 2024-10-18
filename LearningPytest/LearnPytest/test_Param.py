import pytest
# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)
#
# def testlogin(demo_fixture):
#     print("Login Sucessfully")


@pytest.mark.parametrize("a,b,final",[(2,6,8),(8,5,15),(5,10,15)])
def testAdd(a,b,final):
    assert a+b == final