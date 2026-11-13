"""Prorate a plan change mid-cycle."""


def prorated_cents(monthly_cents: int, days_used: int, days_in_cycle: int) -> int:
    return round(monthly_cents * (days_in_cycle - days_used) / days_in_cycle)
