"""Invoice lines sent to Stripe for a billing cycle."""

from acme_billing.rating import rate


def usage_line(customer: str, runs: int) -> dict[str, object]:
    return {"customer": customer, "description": f"{runs:,} workflow runs", "amount_cents": round(rate(runs))}
