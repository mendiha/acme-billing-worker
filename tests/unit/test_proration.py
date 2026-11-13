from acme_billing.proration import prorated_cents


def test_half_cycle_left():
    assert prorated_cents(49_900, 15, 30) == 24_950


def test_nothing_left_on_the_last_day():
    assert prorated_cents(49_900, 30, 30) == 0
