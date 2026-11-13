from acme_billing.invoices import usage_line


def test_usage_line_for_globex():
    assert usage_line("Globex", 40_000) == {"customer": "Globex", "description": "40,000 workflow runs", "amount_cents": 65_000}
