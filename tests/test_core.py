from statkit import mean


def test_mean_of_integers() -> None:
    assert mean([1, 2, 3]) == 2


def test_mean_of_floats() -> None:
    assert mean([0.5, 1.5]) == 1.0


def test_mean_accepts_any_iterable() -> None:
    assert mean(x for x in (2, 4, 6)) == 4
