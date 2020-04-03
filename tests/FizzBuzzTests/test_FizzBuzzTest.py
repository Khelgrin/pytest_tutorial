from FizzBuzz import fizzBuzz
import pytest

@pytest.fixture(params=[x for x in range(1,16)])
def setup(request):
    retVal = request.param
    print("running setup of a test with parameter value {}".format(retVal))
    return retVal


def checkFizzBuzz( value, expectedRetVal ):
    retVal = fizzBuzz(value)
    assert retVal == expectedRetVal

## Napisałem FizzBuzza, który sprawdza FizzBuzza xD
def test_FizzBuzz(setup):
    if setup % 3 ==0 and setup % 5 == 0:
        checkFizzBuzz(setup, "FizzBuzz")
    elif setup % 3 == 0:
        checkFizzBuzz(setup, "Fizz")
    elif setup % 5 == 0:
        checkFizzBuzz(setup, "Buzz")
    else:
        checkFizzBuzz(setup, setup)

### ============== OLD TEST CASES ======================
#
# def test_returns1with1passedIn():
#     checkFizzBuzz(1, 1)
#
# def test_return2with2passedIn():
#     checkFizzBuzz(2, 2)
#
# def test_returnFizzWith3PassedIn():
#     checkFizzBuzz(3, "Fizz")
#
# def test_returnBuzzWith5PassedIn():
#     checkFizzBuzz(5, "Buzz")
#
# def test_returnsFizzWithMultiplesOf3():
#     checkFizzBuzz(6, "Fizz")
#
# def test_returnsBuzzWithMultiplesOf5():
#     checkFizzBuzz(10, "Buzz")
#
# def test_returnsFizzBuzzWith15PassedIn():
#     checkFizzBuzz(15, "FizzBuzz")