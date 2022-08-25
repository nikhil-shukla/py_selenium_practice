import pytest

"""One way to define fixtures"""
# def setup_module(module):
#     print('Open DB port')
#
#
# def teardown_module(module):
#     print('Close DB port')
#
#
# def setup_function(function):
#     print('Launching browser')
#
#
# def teardown_function(function):
#     print("Closing browser")

"""Second way to do the same using decorators"""


@pytest.fixture(scope='function')
def setup():
    print('launch browser')

    yield
    print('close browser')


def test_1(setup):
    print('test 1')


@pytest.mark.usefixtures('setup')
def test_2():
    print('test 2')
