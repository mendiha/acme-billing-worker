"""Tiered rating of metered workflow runs, in cents."""

# (runs up to, price per run in cents); the last tier is open-ended.
TIERS = [(10_000, 2.0), (100_000, 1.5), (None, 1.0)]


def rate(runs: int) -> float:
    total, floor = 0.0, 0
    for ceiling, price in TIERS:
        upper = runs if ceiling is None else min(runs, ceiling)
        if upper > floor:
            total += (upper - floor) * price
        if ceiling is None or runs <= ceiling:
            break
        floor = ceiling
    return total
