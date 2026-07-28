"""Shared helpers for Meridian finance lab."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data" / "master"
TXN = ROOT / "data" / "transactions"
CLOSE = ROOT / "data" / "close"
OUTPUTS = ROOT / "outputs"

NORMAL_CREDIT = {
    "Liability",
    "Equity",
    "Revenue",
    "Other Income",
    "Contra-Asset",
    "Header",
}


def read_csv(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fnum(x: str | float | int | None) -> float:
    if x is None or x == "":
        return 0.0
    return float(x)


def load_coa() -> dict[str, dict]:
    return {r["account"]: r for r in read_csv(MASTER / "chart_of_accounts.csv")}


def trial_balance(as_of_period: str = "2026-06") -> dict[str, float]:
    """
    Net balance by account (debit positive, credit negative convention for assets).
    Includes opening JE dated 2026-05-31 and all postings through period.
    """
    rows = read_csv(TXN / "journal_entries.csv")
    bal: dict[str, float] = defaultdict(float)
    for r in rows:
        # Include opening and June activity
        if r["posting_date"] > "2026-06-30":
            continue
        if as_of_period == "2026-05" and r["posting_date"] > "2026-05-31":
            continue
        bal[r["account"]] += fnum(r["debit"]) - fnum(r["credit"])
    return dict(bal)


def signed_for_fs(account: str, net_debit_positive: float, coa: dict[str, dict]) -> float:
    """Return amount with natural sign for display (credits positive for liability/revenue)."""
    meta = coa.get(account, {})
    t = meta.get("type", "")
    if t in {"Liability", "Equity", "Revenue", "Other Income", "Contra-Asset"}:
        return -net_debit_positive
    return net_debit_positive
