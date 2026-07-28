"""Validate journal balance and control-account sanity checks."""

from __future__ import annotations

import sys

from src import TXN, fnum, read_csv, trial_balance
from src.reconciliations import (
    accrual_recon,
    ap_subledger_balance,
    ar_subledger_balance,
    bank_recon_1010,
    deferred_waterfall,
    fa_recon,
    prepaid_recon,
)


def main() -> int:
    rows = read_csv(TXN / "journal_entries.csv")
    deb = sum(fnum(r["debit"]) for r in rows)
    cred = sum(fnum(r["credit"]) for r in rows)
    ok = abs(deb - cred) < 0.05
    print(f"Journals Dr={deb:.2f} Cr={cred:.2f} balanced={ok}")

    tb = trial_balance()
    print(f"TB accounts: {len(tb)}")

    checks = []
    ar, _ = ar_subledger_balance()
    checks.append(("AR", abs(ar - tb.get("1100", 0)) < 0.05))
    ap, _ = ap_subledger_balance()
    checks.append(("AP", abs(ap - (-tb.get("2100", 0))) < 0.05))
    de, _ = deferred_waterfall()
    checks.append(("Deferred", abs(de - (-tb.get("2400", 0))) < 0.05))
    checks.append(("Bank", bank_recon_1010()["status"] == "TIED"))
    checks.append(("FA", fa_recon()["status"] == "TIED"))
    checks.append(("Prepaid", prepaid_recon()["status"] == "TIED"))
    checks.append(("Accruals", accrual_recon()["status"] == "TIED"))

    for name, passed in checks:
        print(f"  {name}: {'PASS' if passed else 'FAIL'}")

    all_ok = ok and all(p for _, p in checks)
    print("OVERALL:", "PASS" if all_ok else "FAIL")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
