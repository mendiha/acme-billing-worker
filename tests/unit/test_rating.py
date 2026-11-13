import pytest

from acme_billing.rating import rate


@pytest.mark.parametrize("runs,cents", [(0, 0), (5_000, 10_000), (10_000, 20_000), (40_000, 65_000), (150_000, 205_000)])
def test_tiered_rating(runs, cents):
    assert rate(runs) == cents
