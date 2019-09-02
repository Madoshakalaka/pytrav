from pytrav import a_function_that_returns_one


def test_noop():
    # bump travis
    assert a_function_that_returns_one() == 1
