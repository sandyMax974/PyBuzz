from FizzBuzz import fizzBuzz


def test_one():
    assert fizzBuzz(3) == "Fizz"


def test_two():
    assert fizzBuzz(5) == "Buzz"


def test_three():
    assert fizzBuzz(15) == "FizzBuzz"


def test_four():
    assert fizzBuzz(7) == 7
