from fibonacci import fibonacci, r_fibonacci


def test_fibonacci_small():
    assert fibonacci(2) == 1


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_mid():
    assert fibonacci(11) == 89


def test_fibonacci_large():
    assert fibonacci(20) == 6765


def test_r_fibonacci_small():
    assert r_fibonacci(2) == 1


def test_r_fibonacci_zero():
    assert r_fibonacci(0) == 0


def test_r_fibonacci_mid():
    assert r_fibonacci(11) == 89


def test_r_fibonacci_large():
    assert r_fibonacci(20) == 6765
