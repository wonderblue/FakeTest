"""
Meridian CloudWorks — synthetic finance data generator.

Produces reconcilable master data, subledger transactions, journals,
and opening balances for the June 2026 R2R learning lab.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "data" / "master"
TXN = ROOT / "data" / "transactions"
CLOSE = ROOT / "data" / "close"

PERIOD = "2026-06"
PERIOD_END = date(2026, 6, 30)
PERIOD_START = date(2026, 6, 1)


def write_csv(path: Path, rows: list[dict], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("")
        return
    fields = fieldnames or list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def money(x: float) -> str:
    return f"{x:.2f}"


def build_chart_of_accounts() -> list[dict]:
    rows = [
        # Assets
        ("1000", "Current Assets", "Header", "Debit", "BS", "Y"),
        ("1010", "Cash - Operating", "Asset", "Debit", "BS", "Y"),
        ("1020", "Cash - Payroll", "Asset", "Debit", "BS", "Y"),
        ("1100", "Accounts Receivable", "Asset", "Debit", "BS", "Y"),
        ("1150", "Allowance for Doubtful Accounts", "Contra-Asset", "Credit", "BS", "Y"),
        ("1200", "Unbilled AR (Contract Asset)", "Asset", "Debit", "BS", "Y"),
        ("1300", "Prepaid Expenses", "Asset", "Debit", "BS", "Y"),
        ("1400", "Fixed Assets - Gross", "Asset", "Debit", "BS", "Y"),
        ("1450", "Accumulated Depreciation", "Contra-Asset", "Credit", "BS", "Y"),
        # Liabilities
        ("2000", "Current Liabilities", "Header", "Credit", "BS", "Y"),
        ("2100", "Accounts Payable", "Liability", "Credit", "BS", "Y"),
        ("2200", "Accrued Expenses", "Liability", "Credit", "BS", "Y"),
        ("2300", "Accrued Payroll & Taxes", "Liability", "Credit", "BS", "Y"),
        ("2400", "Deferred Revenue", "Liability", "Credit", "BS", "Y"),
        ("2500", "Sales Tax Payable", "Liability", "Credit", "BS", "Y"),
        # Equity
        ("3000", "Equity", "Header", "Credit", "BS", "Y"),
        ("3100", "Common Stock", "Equity", "Credit", "BS", "Y"),
        ("3200", "Retained Earnings", "Equity", "Credit", "BS", "Y"),
        # Revenue
        ("4000", "Revenue", "Header", "Credit", "IS", "Y"),
        ("4100", "SaaS Subscription Revenue", "Revenue", "Credit", "IS", "Y"),
        ("4200", "Professional Services Revenue", "Revenue", "Credit", "IS", "Y"),
        ("4300", "Other Revenue", "Revenue", "Credit", "IS", "Y"),
        # COGS / direct
        ("5000", "Cost of Revenue", "Header", "Debit", "IS", "Y"),
        ("5100", "Hosting Cost of Revenue", "Expense", "Debit", "IS", "Y"),
        ("5200", "Services Delivery Cost", "Expense", "Debit", "IS", "Y"),
        # OpEx
        ("6000", "Operating Expenses", "Header", "Debit", "IS", "Y"),
        ("6100", "Salaries & Wages", "Expense", "Debit", "IS", "Y"),
        ("6110", "Payroll Taxes & Benefits", "Expense", "Debit", "IS", "Y"),
        ("6120", "Bonus Expense", "Expense", "Debit", "IS", "Y"),
        ("6200", "Cloud Hosting (non-COR)", "Expense", "Debit", "IS", "Y"),
        ("6300", "Software & Tools", "Expense", "Debit", "IS", "Y"),
        ("6400", "Marketing & Advertising", "Expense", "Debit", "IS", "Y"),
        ("6450", "Travel & Entertainment", "Expense", "Debit", "IS", "Y"),
        ("6500", "Depreciation Expense", "Expense", "Debit", "IS", "Y"),
        ("6550", "Facilities & Office", "Expense", "Debit", "IS", "Y"),
        ("6600", "Bad Debt Expense", "Expense", "Debit", "IS", "Y"),
        ("6700", "Professional Fees", "Expense", "Debit", "IS", "Y"),
        ("6900", "Miscellaneous Expense", "Expense", "Debit", "IS", "Y"),
        # Other
        ("7100", "Interest Income", "Other Income", "Credit", "IS", "Y"),
        ("7200", "Interest Expense", "Other Expense", "Debit", "IS", "Y"),
    ]
    return [
        {
            "account": a,
            "name": n,
            "type": t,
            "normal_balance": nb,
            "fs_caption": fs,
            "active": act,
            "control_account": "Y"
            if a
            in {
                "1010",
                "1020",
                "1100",
                "1150",
                "1200",
                "1300",
                "1400",
                "1450",
                "2100",
                "2200",
                "2300",
                "2400",
                "2500",
            }
            else "N",
        }
        for a, n, t, nb, fs, act in rows
    ]


def build_entities() -> list[dict]:
    return [
        {
            "entity_id": "MCW-US",
            "legal_name": "Meridian CloudWorks, Inc.",
            "country": "US",
            "currency": "USD",
            "fy_end": "12-31",
            "gaap": "US GAAP",
        }
    ]


def build_cost_centers() -> list[dict]:
    return [
        {"cost_center": "CC-100", "name": "Executive", "function": "G&A"},
        {"cost_center": "CC-200", "name": "Engineering", "function": "R&D"},
        {"cost_center": "CC-300", "name": "Sales", "function": "S&M"},
        {"cost_center": "CC-400", "name": "Customer Success", "function": "S&M"},
        {"cost_center": "CC-500", "name": "Professional Services", "function": "Services"},
        {"cost_center": "CC-600", "name": "Finance & Ops", "function": "G&A"},
        {"cost_center": "CC-700", "name": "Marketing", "function": "S&M"},
    ]


def build_products() -> list[dict]:
    return [
        {
            "product_id": "PL-SAAS",
            "name": "Nimbus Platform SaaS",
            "revenue_account": "4100",
            "recognition": "ratable",
        },
        {
            "product_id": "PL-SVC",
            "name": "Forge Professional Services",
            "revenue_account": "4200",
            "recognition": "as_delivered",
        },
    ]


def build_vendors() -> list[dict]:
    return [
        {"vendor_id": "V001", "name": "CloudRail Hosting", "payment_terms": "Net30", "category": "Hosting"},
        {"vendor_id": "V002", "name": "Northstar CRM Soft", "payment_terms": "Net30", "category": "Software"},
        {"vendor_id": "V003", "name": "Beacon Marketing Co", "payment_terms": "Net45", "category": "Marketing"},
        {"vendor_id": "V004", "name": "Austin Workspace REIT", "payment_terms": "Due on receipt", "category": "Facilities"},
        {"vendor_id": "V005", "name": "PixelForge Laptops", "payment_terms": "Net30", "category": "Hardware"},
        {"vendor_id": "V006", "name": "Summit Legal LLP", "payment_terms": "Net30", "category": "Professional"},
        {"vendor_id": "V007", "name": "PayCore Payroll Inc", "payment_terms": "Due on receipt", "category": "Payroll"},
        {"vendor_id": "V008", "name": "Delta Travel Desk", "payment_terms": "Net15", "category": "T&E"},
        {"vendor_id": "V009", "name": "SecureShield MSSP", "payment_terms": "Net30", "category": "Security"},
        {"vendor_id": "V010", "name": "OfficeKit Supplies", "payment_terms": "Net30", "category": "Office"},
        {"vendor_id": "V011", "name": "DataPipe Analytics", "payment_terms": "Net30", "category": "Software"},
        {"vendor_id": "V012", "name": "BrightLine Recruiting", "payment_terms": "Net30", "category": "HR"},
        {"vendor_id": "V013", "name": "City Utilities Austin", "payment_terms": "Net15", "category": "Utilities"},
        {"vendor_id": "V014", "name": "Kontrol Audit Partners", "payment_terms": "Net30", "category": "Professional"},
        {"vendor_id": "V015", "name": "Slackline Collab", "payment_terms": "Net30", "category": "Software"},
        {"vendor_id": "V016", "name": "Zoomspan Comms", "payment_terms": "Net30", "category": "Software"},
        {"vendor_id": "V017", "name": "FleetCourier Express", "payment_terms": "Net30", "category": "Logistics"},
        {"vendor_id": "V018", "name": "GreenLeaf Catering", "payment_terms": "Net15", "category": "Facilities"},
    ]


def build_customers() -> list[dict]:
    sectors = [
        ("C001", "Acme Industrial", "Manufacturing", "Net30"),
        ("C002", "BlueHarbor Bank", "Financial Services", "Net45"),
        ("C003", "Cedar Health Systems", "Healthcare", "Net30"),
        ("C004", "Delta Logistics NA", "Logistics", "Net30"),
        ("C005", "Evergreen Retail Co", "Retail", "Net30"),
        ("C006", "Falcon Aerospace", "Aerospace", "Net45"),
        ("C007", "Granite Municipal", "Public Sector", "Net60"),
        ("C008", "HarborPoint Energy", "Energy", "Net30"),
        ("C009", "Ivory Education Group", "Education", "Net30"),
        ("C010", "Jade Foods Inc", "CPG", "Net30"),
        ("C011", "Keystone Insurance", "Insurance", "Net45"),
        ("C012", "Lumen Media Holdings", "Media", "Net30"),
        ("C013", "Maple Forestry REIT", "Real Estate", "Net30"),
        ("C014", "Nova Biotech", "Life Sciences", "Net30"),
        ("C015", "Orion Telecom", "Telecom", "Net45"),
        ("C016", "Pioneer Construction", "Construction", "Net30"),
        ("C017", "Quartz Mining PLC", "Materials", "Net60"),
        ("C018", "Riverbend Utilities", "Utilities", "Net30"),
        ("C019", "Summit Hotels Group", "Hospitality", "Net30"),
        ("C020", "Titan Automotive", "Automotive", "Net45"),
        ("C021", "Umbra Security LLC", "Technology", "Net30"),
        ("C022", "Vector Capital Ops", "Financial Services", "Net30"),
        ("C023", "Willow Nonprofit Org", "Nonprofit", "Net30"),
        ("C024", "Xenon Semiconductors", "Technology", "Net30"),
        ("C025", "Yellowstone Parks Co", "Hospitality", "Net30"),
    ]
    return [
        {
            "customer_id": c,
            "name": n,
            "sector": s,
            "payment_terms": t,
            "credit_limit": money(250000 if "Bank" in n or "Insurance" in n else 100000),
        }
        for c, n, s, t in sectors
    ]


def build_employees() -> list[dict]:
    # 48 employees simplified into roles with monthly gross
    # Mid-market SaaS cost structure sized so June is near break-even / modest loss
    roles = [
        ("E001", "Avery Chen", "CEO", "CC-100", 16000),
        ("E002", "Blake Nguyen", "CFO", "CC-600", 14000),
        ("E003", "Casey Ortiz", "Controller", "CC-600", 11000),
        ("E004", "Dana Brooks", "AP Lead", "CC-600", 7000),
        ("E005", "Elliot Park", "AR Lead", "CC-600", 7000),
        ("E006", "Finley Shaw", "VP Engineering", "CC-200", 13000),
    ]
    # generate remaining staff
    # 42 additional staff → 48 total with the 6 named leaders above
    names = [
        "Gray", "Hayes", "Ivy", "Jordan", "Kim", "Lee", "Morgan", "Nash", "Owen", "Patel",
        "Quinn", "Reed", "Sage", "Taylor", "Underwood", "Vega", "Wade", "Xu", "Young", "Zane",
        "Adler", "Bell", "Cruz", "Drew", "Ellis", "Frost", "Gill", "Hunt", "Ingram", "Jules",
        "Knox", "Lane", "Moss", "Noel", "Oak", "Page", "Rios", "Shea", "True", "Voss",
        "West", "York",
    ]
    ccs = (
        ["CC-200"] * 16
        + ["CC-300"] * 8
        + ["CC-400"] * 6
        + ["CC-500"] * 8
        + ["CC-700"] * 4
    )
    base_salaries = [
        8500, 8200, 8000, 7800, 7500, 7200, 7000, 6800,
        6500, 6400, 6200, 6000, 5800, 5600, 5500, 5400,
        6500, 6400, 6200, 6000, 5800, 5600, 5500, 5400,
        6000, 5800, 5600, 5400, 5200, 5000, 6200, 6000,
        5800, 5600, 5400, 5200, 5000, 4800, 4600, 4500,
        4400, 4200,
    ]
    rows = [
        {
            "employee_id": e,
            "name": n,
            "title": t,
            "cost_center": cc,
            "monthly_gross": money(g),
            "status": "Active",
        }
        for e, n, t, cc, g in roles
    ]
    for i, name in enumerate(names):
        rows.append(
            {
                "employee_id": f"E{i+7:03d}",
                "name": f"{name} Employee",
                "title": "Staff",
                "cost_center": ccs[i],
                "monthly_gross": money(base_salaries[i]),
                "status": "Active",
            }
        )
    return rows[:48]


@dataclass
class JELine:
    je_id: str
    line: int
    date: str
    account: str
    debit: float
    credit: float
    memo: str
    source: str
    ref: str
    cost_center: str = ""
    product: str = ""
    customer_id: str = ""
    vendor_id: str = ""


def je_rows(lines: list[JELine]) -> list[dict]:
    out = []
    for x in lines:
        out.append(
            {
                "je_id": x.je_id,
                "line_no": x.line,
                "posting_date": x.date,
                "account": x.account,
                "debit": money(x.debit),
                "credit": money(x.credit),
                "memo": x.memo,
                "source": x.source,
                "ref": x.ref,
                "cost_center": x.cost_center,
                "product": x.product,
                "customer_id": x.customer_id,
                "vendor_id": x.vendor_id,
                "period": PERIOD,
            }
        )
    return out


def generate_all() -> dict:
    coa = build_chart_of_accounts()
    entities = build_entities()
    ccs = build_cost_centers()
    products = build_products()
    vendors = build_vendors()
    customers = build_customers()
    employees = build_employees()

    write_csv(MASTER / "chart_of_accounts.csv", coa)
    write_csv(MASTER / "entities.csv", entities)
    write_csv(MASTER / "cost_centers.csv", ccs)
    write_csv(MASTER / "products.csv", products)
    write_csv(MASTER / "vendors.csv", vendors)
    write_csv(MASTER / "customers.csv", customers)
    write_csv(MASTER / "employees.csv", employees)

    journals: list[JELine] = []
    je_n = 1

    def next_je(prefix: str = "JE") -> str:
        nonlocal je_n
        jid = f"{prefix}-{PERIOD.replace('-', '')}-{je_n:04d}"
        je_n += 1
        return jid

    # ------------------------------------------------------------------
    # Opening balances (as of 2026-05-31) — equity plugs retained earnings
    # ------------------------------------------------------------------
    opening = {
        "1010": 820000.0,  # operating cash
        "1020": 95000.0,  # payroll cash
        "1100": 412500.0,  # AR
        "1150": -18500.0,  # allowance (credit balance stored negative as asset contra via credit)
        "1200": 22000.0,  # unbilled
        "1300": 48000.0,  # prepaid
        "1400": 265000.0,  # FA gross
        "1450": -98000.0,  # accum dep (contra)
        "2100": -156000.0,  # AP
        "2200": -42000.0,  # accrued exp
        "2300": -38000.0,  # accrued payroll
        "2400": -615000.0,  # deferred revenue
        "2500": -8500.0,  # sales tax
        "3100": -100000.0,  # common stock
    }
    # retained earnings plug
    opening["3200"] = -sum(opening.values())

    open_rows = []
    jid = next_je("OB")
    line = 1
    for acct, bal in opening.items():
        debit = bal if bal > 0 else 0.0
        credit = -bal if bal < 0 else 0.0
        open_rows.append(
            {
                "as_of": "2026-05-31",
                "account": acct,
                "debit": money(debit),
                "credit": money(credit),
                "net": money(bal),
            }
        )
        journals.append(
            JELine(
                jid,
                line,
                "2026-05-31",
                acct,
                debit,
                credit,
                "Opening balance May 31",
                "OPENING",
                "OB-2026-05",
            )
        )
        line += 1

    write_csv(CLOSE / "opening_trial_balance_2026-05-31.csv", open_rows)

    # ------------------------------------------------------------------
    # O2C — SaaS contracts (deferred) + services
    # ------------------------------------------------------------------
    # Annual SaaS contracts billed earlier — monthly release in June
    saas_contracts = [
        # customer, annual amount, start, months, billed?
        ("C001", 144000, date(2026, 4, 1), 12),
        ("C002", 216000, date(2026, 1, 1), 12),
        ("C003", 96000, date(2026, 3, 1), 12),
        ("C004", 72000, date(2025, 7, 1), 12),
        ("C005", 120000, date(2026, 2, 1), 12),
        ("C006", 180000, date(2026, 5, 1), 12),
        ("C008", 60000, date(2026, 6, 1), 12),
        ("C011", 132000, date(2025, 10, 1), 12),
        ("C014", 84000, date(2026, 4, 15), 12),
        ("C015", 156000, date(2026, 1, 1), 12),
        ("C020", 108000, date(2026, 3, 1), 12),
        ("C024", 90000, date(2026, 5, 15), 12),
    ]

    deferred_schedule = []
    ar_invoices = []
    ar_receipts = []
    sales_orders = []

    inv_n = 1
    so_n = 1
    rcpt_n = 1

    # Monthly SaaS customers billed in arrears in June
    monthly_saas = [
        ("C007", 6500),
        ("C009", 4200),
        ("C010", 7800),
        ("C012", 9100),
        ("C013", 3500),
        ("C016", 5600),
        ("C017", 4800),
        ("C018", 6200),
        ("C019", 5400),
        ("C021", 11000),
        ("C022", 8700),
        ("C023", 2900),
        ("C025", 4100),
    ]

    # Deferred revenue releases for annual contracts
    jid = next_je("REV")
    line = 1
    total_saas_release = 0.0
    for cust, annual, start, months in saas_contracts:
        monthly = round(annual / months, 2)
        # adjust last month later if needed; for lab keep equal
        total_saas_release += monthly
        deferred_schedule.append(
            {
                "customer_id": cust,
                "contract_start": start.isoformat(),
                "annual_amount": money(annual),
                "monthly_recognition": money(monthly),
                "period": PERIOD,
                "recognition_amount": money(monthly),
                "product": "PL-SAAS",
            }
        )
        journals.append(
            JELine(
                jid,
                line,
                "2026-06-30",
                "2400",
                monthly,
                0,
                f"Deferred release {cust} {PERIOD}",
                "R2R-REV",
                f"DEF-{cust}",
                "CC-400",
                "PL-SAAS",
                cust,
            )
        )
        line += 1
        journals.append(
            JELine(
                jid,
                line,
                "2026-06-30",
                "4100",
                0,
                monthly,
                f"SaaS revenue {cust} {PERIOD}",
                "R2R-REV",
                f"DEF-{cust}",
                "CC-400",
                "PL-SAAS",
                cust,
            )
        )
        line += 1

    # New annual bill in June for C008 (already in list) — invoice + deferred add
    # C008 start June 1 — bill annual
    c008_annual = 60000.0
    inv_id = f"INV-2026-{inv_n:04d}"
    inv_n += 1
    ar_invoices.append(
        {
            "invoice_id": inv_id,
            "invoice_date": "2026-06-01",
            "customer_id": "C008",
            "product": "PL-SAAS",
            "description": "Nimbus annual subscription Jun26-May27",
            "amount": money(c008_annual),
            "tax": money(0),
            "total": money(c008_annual),
            "status": "Open",
            "due_date": "2026-07-01",
            "revenue_treatment": "deferred",
        }
    )
    sales_orders.append(
        {
            "so_id": f"SO-2026-{so_n:04d}",
            "order_date": "2026-05-28",
            "customer_id": "C008",
            "product": "PL-SAAS",
            "amount": money(c008_annual),
            "billing_type": "annual_upfront",
        }
    )
    so_n += 1
    jid = next_je("AR")
    journals.append(
        JELine(jid, 1, "2026-06-01", "1100", c008_annual, 0, "Bill C008 annual SaaS", "O2C", inv_id, "CC-400", "PL-SAAS", "C008")
    )
    journals.append(
        JELine(jid, 2, "2026-06-01", "2400", 0, c008_annual, "Defer C008 annual SaaS", "O2C", inv_id, "CC-400", "PL-SAAS", "C008")
    )

    # Monthly SaaS invoices (earned in June = revenue directly)
    for cust, amt in monthly_saas:
        inv_id = f"INV-2026-{inv_n:04d}"
        inv_n += 1
        ar_invoices.append(
            {
                "invoice_id": inv_id,
                "invoice_date": "2026-06-30",
                "customer_id": cust,
                "product": "PL-SAAS",
                "description": "Nimbus monthly subscription June 2026",
                "amount": money(amt),
                "tax": money(0),
                "total": money(amt),
                "status": "Open",
                "due_date": "2026-07-30",
                "revenue_treatment": "recognize_on_bill",
            }
        )
        sales_orders.append(
            {
                "so_id": f"SO-2026-{so_n:04d}",
                "order_date": "2026-06-01",
                "customer_id": cust,
                "product": "PL-SAAS",
                "amount": money(amt),
                "billing_type": "monthly_arrears",
            }
        )
        so_n += 1
        jid = next_je("AR")
        journals.append(
            JELine(jid, 1, "2026-06-30", "1100", amt, 0, f"Monthly SaaS bill {cust}", "O2C", inv_id, "CC-400", "PL-SAAS", cust)
        )
        journals.append(
            JELine(jid, 2, "2026-06-30", "4100", 0, amt, f"Monthly SaaS rev {cust}", "O2C", inv_id, "CC-400", "PL-SAAS", cust)
        )

    # Professional services invoices + unbilled
    services = [
        ("C001", 28000, "PRJ-1042", "Implementation milestone 3", True),
        ("C003", 15500, "PRJ-1108", "Integration T&M June", True),
        ("C014", 22000, "PRJ-1180", "Data migration milestone", True),
        ("C006", 9800, "PRJ-1201", "Advisory T&M", True),
        ("C020", 12500, "PRJ-1215", "Training package", True),
    ]
    for cust, amt, proj, desc, billed in services:
        if billed:
            inv_id = f"INV-2026-{inv_n:04d}"
            inv_n += 1
            ar_invoices.append(
                {
                    "invoice_id": inv_id,
                    "invoice_date": "2026-06-25",
                    "customer_id": cust,
                    "product": "PL-SVC",
                    "description": f"{desc} ({proj})",
                    "amount": money(amt),
                    "tax": money(0),
                    "total": money(amt),
                    "status": "Open",
                    "due_date": "2026-07-25",
                    "revenue_treatment": "recognize_on_bill",
                }
            )
            jid = next_je("AR")
            journals.append(
                JELine(jid, 1, "2026-06-25", "1100", amt, 0, desc, "O2C", inv_id, "CC-500", "PL-SVC", cust)
            )
            journals.append(
                JELine(jid, 2, "2026-06-25", "4200", 0, amt, desc, "O2C", inv_id, "CC-500", "PL-SVC", cust)
            )

    # Unbilled services earned in June
    unbilled_items = [
        ("C011", 8500, "PRJ-1190", "Unbilled advisory hours"),
        ("C024", 6200, "PRJ-1220", "Unbilled implementation"),
    ]
    jid = next_je("REV")
    line = 1
    for cust, amt, proj, desc in unbilled_items:
        journals.append(
            JELine(jid, line, "2026-06-30", "1200", amt, 0, desc, "R2R-ACCR", proj, "CC-500", "PL-SVC", cust)
        )
        line += 1
        journals.append(
            JELine(jid, line, "2026-06-30", "4200", 0, amt, desc, "R2R-ACCR", proj, "CC-500", "PL-SVC", cust)
        )
        line += 1

    # May unbilled billed in June (clear contract asset)
    may_unbilled_clear = [
        ("C002", 12000, "PRJ-1088"),
        ("C015", 10000, "PRJ-1099"),
    ]
    for cust, amt, proj in may_unbilled_clear:
        inv_id = f"INV-2026-{inv_n:04d}"
        inv_n += 1
        ar_invoices.append(
            {
                "invoice_id": inv_id,
                "invoice_date": "2026-06-05",
                "customer_id": cust,
                "product": "PL-SVC",
                "description": f"Bill prior unbilled {proj}",
                "amount": money(amt),
                "tax": money(0),
                "total": money(amt),
                "status": "Open",
                "due_date": "2026-07-05",
                "revenue_treatment": "clear_unbilled",
            }
        )
        jid = next_je("AR")
        journals.append(
            JELine(jid, 1, "2026-06-05", "1100", amt, 0, "Bill prior unbilled", "O2C", inv_id, "CC-500", "PL-SVC", cust)
        )
        journals.append(
            JELine(jid, 2, "2026-06-05", "1200", 0, amt, "Clear unbilled", "O2C", inv_id, "CC-500", "PL-SVC", cust)
        )

    # Cash collections on AR (mix of prior and current)
    collections = [
        ("C001", 45000, "2026-06-08", "Prior AR"),
        ("C002", 54000, "2026-06-10", "Prior AR"),
        ("C003", 32000, "2026-06-12", "Prior AR"),
        ("C005", 28000, "2026-06-14", "Prior AR"),
        ("C006", 40000, "2026-06-18", "Prior AR"),
        ("C011", 35000, "2026-06-20", "Prior AR"),
        ("C015", 38000, "2026-06-22", "Prior AR"),
        ("C004", 22000, "2026-06-24", "Prior AR"),
        ("C014", 18000, "2026-06-26", "Prior AR + partial"),
        ("C008", 60000, "2026-06-28", "C008 annual collected"),
        ("C020", 15000, "2026-06-29", "Prior AR"),
    ]
    bank_txns = []
    bn = 1
    for cust, amt, dt, memo in collections:
        rid = f"RCPT-2026-{rcpt_n:04d}"
        rcpt_n += 1
        ar_receipts.append(
            {
                "receipt_id": rid,
                "receipt_date": dt,
                "customer_id": cust,
                "amount": money(amt),
                "method": "ACH",
                "memo": memo,
            }
        )
        jid = next_je("CA")
        journals.append(
            JELine(jid, 1, dt, "1010", amt, 0, f"Cash app {cust}", "O2C-CASH", rid, customer_id=cust)
        )
        journals.append(
            JELine(jid, 2, dt, "1100", 0, amt, f"Cash app {cust}", "O2C-CASH", rid, customer_id=cust)
        )
        bank_txns.append(
            {
                "bank_txn_id": f"BNK-OP-{bn:04d}",
                "bank_account": "1010",
                "txn_date": dt,
                "description": f"ACH IN {cust} {memo}",
                "amount": money(amt),
                "type": "credit",
                "reconciled": "Y",
            }
        )
        bn += 1

    # ------------------------------------------------------------------
    # P2P — AP invoices, payments, accruals, prepaid
    # ------------------------------------------------------------------
    ap_invoices = []
    ap_payments = []
    pos = []
    ap_n = 1
    po_n = 1
    pay_n = 1

    ap_items = [
        ("V001", "2026-06-05", 48500, "5100", "CC-200", "AWS-style hosting June usage", "Open"),
        ("V003", "2026-06-08", 18500, "6400", "CC-700", "Demand gen campaign June", "Open"),
        ("V006", "2026-06-10", 9200, "6700", "CC-600", "Contract review retainer", "Open"),
        ("V009", "2026-06-12", 7600, "6300", "CC-200", "Managed security June", "Open"),
        ("V008", "2026-06-15", 4300, "6450", "CC-300", "Sales travel", "Open"),
        ("V010", "2026-06-16", 1200, "6550", "CC-600", "Office supplies", "Open"),
        ("V013", "2026-06-18", 2800, "6550", "CC-600", "Utilities June", "Open"),
        ("V011", "2026-06-20", 5400, "6300", "CC-200", "Analytics seats", "Open"),
        ("V012", "2026-06-22", 15000, "6100", "CC-100", "Exec search fee", "Open"),
        ("V017", "2026-06-24", 900, "6900", "CC-600", "Courier", "Open"),
        ("V018", "2026-06-25", 1600, "6550", "CC-100", "All-hands catering", "Open"),
        ("V014", "2026-06-27", 12000, "6700", "CC-600", "Interim audit work", "Open"),
        ("V005", "2026-06-07", 9600, "1400", "CC-200", "4 laptops capitalized", "Open"),
    ]

    for vendor, dt, amt, acct, cc, desc, status in ap_items:
        po_id = f"PO-2026-{po_n:04d}"
        po_n += 1
        pos.append(
            {
                "po_id": po_id,
                "po_date": dt,
                "vendor_id": vendor,
                "amount": money(amt),
                "description": desc,
                "status": "Received",
            }
        )
        ap_id = f"APINV-2026-{ap_n:04d}"
        ap_n += 1
        ap_invoices.append(
            {
                "ap_invoice_id": ap_id,
                "invoice_date": dt,
                "vendor_id": vendor,
                "po_id": po_id,
                "account": acct,
                "cost_center": cc,
                "description": desc,
                "amount": money(amt),
                "status": status,
                "due_date": (date.fromisoformat(dt) + timedelta(days=30)).isoformat(),
            }
        )
        jid = next_je("AP")
        journals.append(
            JELine(jid, 1, dt, acct, amt, 0, desc, "P2P", ap_id, cc, vendor_id=vendor)
        )
        journals.append(
            JELine(jid, 2, dt, "2100", 0, amt, desc, "P2P", ap_id, cc, vendor_id=vendor)
        )

    # Prepaid annual software — V002 Northstar CRM Soft $36,000 for 12 months from June 1
    prepaid_amt = 36000.0
    po_id = f"PO-2026-{po_n:04d}"
    po_n += 1
    pos.append(
        {
            "po_id": po_id,
            "po_date": "2026-06-01",
            "vendor_id": "V002",
            "amount": money(prepaid_amt),
            "description": "Northstar CRM annual license",
            "status": "Received",
        }
    )
    ap_id = f"APINV-2026-{ap_n:04d}"
    ap_n += 1
    ap_invoices.append(
        {
            "ap_invoice_id": ap_id,
            "invoice_date": "2026-06-01",
            "vendor_id": "V002",
            "po_id": po_id,
            "account": "1300",
            "cost_center": "CC-300",
            "description": "Northstar CRM annual license",
            "amount": money(prepaid_amt),
            "status": "Paid",
            "due_date": "2026-06-01",
        }
    )
    jid = next_je("AP")
    journals.append(
        JELine(jid, 1, "2026-06-01", "1300", prepaid_amt, 0, "CRM prepaid", "P2P", ap_id, "CC-300", vendor_id="V002")
    )
    journals.append(
        JELine(jid, 2, "2026-06-01", "2100", 0, prepaid_amt, "CRM prepaid", "P2P", ap_id, "CC-300", vendor_id="V002")
    )

    # Rent V004
    rent = 22000.0
    ap_id = f"APINV-2026-{ap_n:04d}"
    ap_n += 1
    ap_invoices.append(
        {
            "ap_invoice_id": ap_id,
            "invoice_date": "2026-06-01",
            "vendor_id": "V004",
            "po_id": "",
            "account": "6550",
            "cost_center": "CC-600",
            "description": "June office rent",
            "amount": money(rent),
            "status": "Paid",
            "due_date": "2026-06-01",
        }
    )
    jid = next_je("AP")
    journals.append(
        JELine(jid, 1, "2026-06-01", "6550", rent, 0, "June rent", "P2P", ap_id, "CC-600", vendor_id="V004")
    )
    journals.append(
        JELine(jid, 2, "2026-06-01", "2100", 0, rent, "June rent", "P2P", ap_id, "CC-600", vendor_id="V004")
    )

    # AP payments (including opening AP clearance + June paid items)
    payments = [
        ("V001", 42000, "2026-06-05", "Prior hosting"),
        ("V003", 15000, "2026-06-07", "Prior marketing"),
        ("V004", 22000, "2026-06-01", "June rent"),
        ("V002", 36000, "2026-06-03", "CRM annual"),
        ("V006", 8000, "2026-06-11", "Prior legal"),
        ("V009", 7000, "2026-06-14", "Prior security"),
        ("V007", 0, "2026-06-15", "payroll funding placeholder"),  # skip
        ("V010", 2500, "2026-06-17", "Prior supplies"),
        ("V014", 10000, "2026-06-21", "Prior audit"),
        ("V005", 9600, "2026-06-28", "Laptops"),
        ("V011", 4000, "2026-06-25", "Prior analytics"),
    ]
    for vendor, amt, dt, memo in payments:
        if amt <= 0:
            continue
        pid = f"APPAY-2026-{pay_n:04d}"
        pay_n += 1
        ap_payments.append(
            {
                "payment_id": pid,
                "payment_date": dt,
                "vendor_id": vendor,
                "amount": money(amt),
                "method": "ACH",
                "memo": memo,
            }
        )
        jid = next_je("PAY")
        journals.append(
            JELine(jid, 1, dt, "2100", amt, 0, memo, "P2P-PAY", pid, vendor_id=vendor)
        )
        journals.append(
            JELine(jid, 2, dt, "1010", 0, amt, memo, "P2P-PAY", pid, vendor_id=vendor)
        )
        bank_txns.append(
            {
                "bank_txn_id": f"BNK-OP-{bn:04d}",
                "bank_account": "1010",
                "txn_date": dt,
                "description": f"ACH OUT {vendor} {memo}",
                "amount": money(-amt),
                "type": "debit",
                "reconciled": "Y",
            }
        )
        bn += 1

    # ------------------------------------------------------------------
    # Payroll June
    # ------------------------------------------------------------------
    gross = sum(float(e["monthly_gross"]) for e in employees)
    employer_tax = round(gross * 0.0765, 2)
    net_pay = round(gross * 0.72, 2)  # simplified withholdings
    employee_withhold = round(gross - net_pay, 2)

    # Reverse May accrued payroll (opening 2300 includes May accrual ~38000) — reverse portion
    # For lab: post June payroll expense and fund net + taxes
    jid = next_je("PR")
    journals.append(
        JELine(jid, 1, "2026-06-15", "6100", gross, 0, "June salaries", "H2R", "PR-2026-06", "CC-600")
    )
    journals.append(
        JELine(jid, 2, "2026-06-15", "6110", employer_tax, 0, "June employer taxes", "H2R", "PR-2026-06", "CC-600")
    )
    journals.append(
        JELine(
            jid,
            3,
            "2026-06-15",
            "2300",
            0,
            gross + employer_tax,
            "June payroll accrual",
            "H2R",
            "PR-2026-06",
            "CC-600",
        )
    )

    # Fund payroll (pay down accrued + May remainder conceptually)
    payroll_funding = net_pay + employee_withhold + employer_tax  # total cash out related
    # Simplified: pay net to employees + remit taxes = gross + employer_tax
    cash_out = round(gross + employer_tax, 2)
    jid = next_je("PR")
    journals.append(
        JELine(jid, 1, "2026-06-16", "2300", cash_out, 0, "Fund June payroll", "H2R", "PR-FUND-06", "CC-600")
    )
    journals.append(
        JELine(jid, 2, "2026-06-16", "1020", 0, cash_out, "Fund June payroll", "H2R", "PR-FUND-06", "CC-600")
    )
    bank_txns.append(
        {
            "bank_txn_id": f"BNK-PR-{bn:04d}",
            "bank_account": "1020",
            "txn_date": "2026-06-16",
            "description": "Payroll funding June",
            "amount": money(-cash_out),
            "type": "debit",
            "reconciled": "Y",
        }
    )
    bn += 1

    # Transfer operating → payroll to top up
    transfer = 450000.0
    jid = next_je("TR")
    journals.append(
        JELine(jid, 1, "2026-06-14", "1020", transfer, 0, "Fund payroll account", "TREASURY", "XFER-0614")
    )
    journals.append(
        JELine(jid, 2, "2026-06-14", "1010", 0, transfer, "Fund payroll account", "TREASURY", "XFER-0614")
    )
    bank_txns.append(
        {
            "bank_txn_id": f"BNK-OP-{bn:04d}",
            "bank_account": "1010",
            "txn_date": "2026-06-14",
            "description": "Transfer to payroll account",
            "amount": money(-transfer),
            "type": "debit",
            "reconciled": "Y",
        }
    )
    bn += 1
    bank_txns.append(
        {
            "bank_txn_id": f"BNK-PR-{bn:04d}",
            "bank_account": "1020",
            "txn_date": "2026-06-14",
            "description": "Transfer from operating",
            "amount": money(transfer),
            "type": "credit",
            "reconciled": "Y",
        }
    )
    bn += 1

    payroll_register = [
        {
            "period": PERIOD,
            "gross_wages": money(gross),
            "employer_taxes": money(employer_tax),
            "employee_withholdings": money(employee_withhold),
            "net_pay": money(net_pay),
            "headcount": str(len(employees)),
        }
    ]

    # Bonus accrual June
    bonus_accrual = 25000.0
    jid = next_je("ACC")
    journals.append(
        JELine(jid, 1, "2026-06-30", "6120", bonus_accrual, 0, "Q2 bonus accrual", "R2R-ACCR", "BONUS-Q2", "CC-100")
    )
    journals.append(
        JELine(jid, 2, "2026-06-30", "2200", 0, bonus_accrual, "Q2 bonus accrual", "R2R-ACCR", "BONUS-Q2", "CC-100")
    )

    # ------------------------------------------------------------------
    # Accruals — reverse May and book June
    # ------------------------------------------------------------------
    # Reverse May accrued expenses (opening 2200 = 42000). Assume full reverse then re-accrue.
    may_accrual_reverse = 42000.0
    jid = next_je("ACC")
    journals.append(
        JELine(jid, 1, "2026-06-01", "2200", may_accrual_reverse, 0, "Reverse May accruals", "R2R-ACCR", "REV-MAY-ACC")
    )
    journals.append(
        JELine(jid, 2, "2026-06-01", "6400", 0, 12000, "Reverse May mkt accrual", "R2R-ACCR", "REV-MAY-ACC", "CC-700")
    )
    journals.append(
        JELine(jid, 3, "2026-06-01", "6700", 0, 10000, "Reverse May legal accrual", "R2R-ACCR", "REV-MAY-ACC", "CC-600")
    )
    journals.append(
        JELine(jid, 4, "2026-06-01", "5100", 0, 20000, "Reverse May hosting accrual", "R2R-ACCR", "REV-MAY-ACC", "CC-200")
    )

    # June period-end accruals (excluding bonus already booked)
    june_accruals = [
        ("V001", 5200, "5100", "CC-200", "Hosting late usage estimate"),
        ("V003", 7500, "6400", "CC-700", "Agency work not yet invoiced"),
        ("V006", 4000, "6700", "CC-600", "Legal work in progress"),
        ("V008", 2100, "6450", "CC-300", "Unsubmitted T&E"),
    ]
    accrual_rows = []
    jid = next_je("ACC")
    line = 1
    for vendor, amt, acct, cc, desc in june_accruals:
        accrual_rows.append(
            {
                "accrual_id": f"ACC-2026-06-{line:02d}",
                "vendor_id": vendor,
                "account": acct,
                "cost_center": cc,
                "amount": money(amt),
                "description": desc,
                "auto_reverse": "Y",
            }
        )
        journals.append(
            JELine(jid, line, "2026-06-30", acct, amt, 0, desc, "R2R-ACCR", f"ACC-{vendor}", cc, vendor_id=vendor)
        )
        line += 1
        journals.append(
            JELine(jid, line, "2026-06-30", "2200", 0, amt, desc, "R2R-ACCR", f"ACC-{vendor}", cc, vendor_id=vendor)
        )
        line += 1

    # Bonus already in 2200
    accrual_rows.append(
        {
            "accrual_id": "ACC-2026-06-BONUS",
            "vendor_id": "",
            "account": "6120",
            "cost_center": "CC-100",
            "amount": money(bonus_accrual),
            "description": "Q2 bonus accrual",
            "auto_reverse": "N",
        }
    )

    # Prepaid amortization (opening prepaid 48000 + new 36000)
    # Amortize: existing $4,000/mo + new CRM $3,000/mo = $7,000
    prepaid_amort = 7000.0
    jid = next_je("PRE")
    journals.append(
        JELine(jid, 1, "2026-06-30", "6300", prepaid_amort, 0, "Amortize prepaid software", "R2R-PRE", "PRE-AMORT", "CC-300")
    )
    journals.append(
        JELine(jid, 2, "2026-06-30", "1300", 0, prepaid_amort, "Amortize prepaid software", "R2R-PRE", "PRE-AMORT", "CC-300")
    )

    prepaid_schedule = [
        {
            "item": "Opening prepaid software/tools",
            "begin": money(48000),
            "additions": money(36000),
            "amortization": money(7000),
            "end": money(48000 + 36000 - 7000),
        }
    ]

    # ------------------------------------------------------------------
    # Fixed assets & depreciation
    # ------------------------------------------------------------------
    fa_register = [
        {
            "asset_id": "FA-001",
            "description": "Office buildout",
            "cost": money(120000),
            "accum_dep_begin": money(48000),
            "useful_life_months": 60,
            "monthly_dep": money(2000),
            "cost_center": "CC-600",
        },
        {
            "asset_id": "FA-002",
            "description": "Servers & network",
            "cost": money(85000),
            "accum_dep_begin": money(34000),
            "useful_life_months": 36,
            "monthly_dep": money(2361.11),
            "cost_center": "CC-200",
        },
        {
            "asset_id": "FA-003",
            "description": "Furniture",
            "cost": money(35000),
            "accum_dep_begin": money(14000),
            "useful_life_months": 84,
            "monthly_dep": money(416.67),
            "cost_center": "CC-600",
        },
        {
            "asset_id": "FA-004",
            "description": "Prior laptops pool",
            "cost": money(25000),
            "accum_dep_begin": money(2000),
            "useful_life_months": 36,
            "monthly_dep": money(694.44),
            "cost_center": "CC-200",
        },
        {
            "asset_id": "FA-005",
            "description": "June laptop purchase (4)",
            "cost": money(9600),
            "accum_dep_begin": money(0),
            "useful_life_months": 36,
            "monthly_dep": money(266.67),
            "cost_center": "CC-200",
        },
    ]
    # Note: opening FA gross 265000 = 120+85+35+25; June add 9600 → 274600
    monthly_dep = round(sum(float(a["monthly_dep"]) for a in fa_register), 2)
    jid = next_je("FA")
    journals.append(
        JELine(jid, 1, "2026-06-30", "6500", monthly_dep, 0, "June depreciation", "R2R-FA", "DEP-2026-06", "CC-600")
    )
    journals.append(
        JELine(jid, 2, "2026-06-30", "1450", 0, monthly_dep, "June depreciation", "R2R-FA", "DEP-2026-06", "CC-600")
    )

    # ------------------------------------------------------------------
    # Bad debt reserve true-up
    # ------------------------------------------------------------------
    # Target allowance 20,000; opening allowance 18,500 → expense 1,500
    bad_debt = 1500.0
    jid = next_je("EST")
    journals.append(
        JELine(jid, 1, "2026-06-30", "6600", bad_debt, 0, "Bad debt reserve true-up", "R2R-EST", "ADA-2026-06", "CC-600")
    )
    journals.append(
        JELine(jid, 2, "2026-06-30", "1150", 0, bad_debt, "Bad debt reserve true-up", "R2R-EST", "ADA-2026-06", "CC-600")
    )

    # ------------------------------------------------------------------
    # Bank recon extras: outstanding items & deposits in transit
    # ------------------------------------------------------------------
    # Deposit in transit: customer payment recorded in books 6/30, clears bank 7/1
    dit_amt = 12500.0
    rid = f"RCPT-2026-{rcpt_n:04d}"
    rcpt_n += 1
    ar_receipts.append(
        {
            "receipt_id": rid,
            "receipt_date": "2026-06-30",
            "customer_id": "C012",
            "amount": money(dit_amt),
            "method": "ACH",
            "memo": "Deposit in transit at month-end",
        }
    )
    jid = next_je("CA")
    journals.append(
        JELine(jid, 1, "2026-06-30", "1010", dit_amt, 0, "DIT receipt C012", "O2C-CASH", rid, customer_id="C012")
    )
    journals.append(
        JELine(jid, 2, "2026-06-30", "1100", 0, dit_amt, "DIT receipt C012", "O2C-CASH", rid, customer_id="C012")
    )
    # NOT in bank statement (reconciled=N) — timing difference
    bank_outstanding = [
        {
            "item_id": "DIT-001",
            "bank_account": "1010",
            "type": "deposit_in_transit",
            "amount": money(dit_amt),
            "book_date": "2026-06-30",
            "clears_bank": "2026-07-01",
            "description": "C012 ACH not yet on bank stmt",
        },
        {
            "item_id": "OS-CHK-001",
            "bank_account": "1010",
            "type": "outstanding_payment",
            "amount": money(1600),
            "book_date": "2026-06-25",
            "clears_bank": "2026-07-02",
            "description": "V018 catering payment outstanding",
        },
    ]
    # Mark catering payment as outstanding — we need a book payment not yet in bank
    # Add AP payment for V018 that is in books but bank reconcilied = N
    pid = f"APPAY-2026-{pay_n:04d}"
    pay_n += 1
    ap_payments.append(
        {
            "payment_id": pid,
            "payment_date": "2026-06-25",
            "vendor_id": "V018",
            "amount": money(1600),
            "method": "CHECK",
            "memo": "Catering - outstanding check",
        }
    )
    jid = next_je("PAY")
    journals.append(
        JELine(jid, 1, "2026-06-25", "2100", 1600, 0, "Catering payment", "P2P-PAY", pid, vendor_id="V018")
    )
    journals.append(
        JELine(jid, 2, "2026-06-25", "1010", 0, 1600, "Catering payment", "P2P-PAY", pid, vendor_id="V018")
    )
    bank_txns.append(
        {
            "bank_txn_id": f"BNK-OP-{bn:04d}",
            "bank_account": "1010",
            "txn_date": "2026-06-25",
            "description": "CHECK OUT V018 catering",
            "amount": money(-1600),
            "type": "debit",
            "reconciled": "N",  # outstanding — exclude from bank stmt balance calc carefully
        }
    )
    bn += 1

    # Interest income
    interest = 420.0
    jid = next_je("TR")
    journals.append(
        JELine(jid, 1, "2026-06-30", "1010", interest, 0, "Bank interest", "TREASURY", "INT-JUN")
    )
    journals.append(
        JELine(jid, 2, "2026-06-30", "7100", 0, interest, "Bank interest", "TREASURY", "INT-JUN")
    )
    bank_txns.append(
        {
            "bank_txn_id": f"BNK-OP-{bn:04d}",
            "bank_account": "1010",
            "txn_date": "2026-06-30",
            "description": "Interest credit",
            "amount": money(interest),
            "type": "credit",
            "reconciled": "Y",
        }
    )

    # ------------------------------------------------------------------
    # Close calendar
    # ------------------------------------------------------------------
    close_calendar = [
        {"day": "-2", "task": "Communicate invoice/PO cutoffs", "owner": "Controller", "status": "Done"},
        {"day": "-1", "task": "Finalize billing run", "owner": "AR Lead", "status": "Done"},
        {"day": "0", "task": "Period end — freeze operational posting", "owner": "Controller", "status": "Done"},
        {"day": "1", "task": "Reverse prior accruals; post recurring; depreciation", "owner": "Staff Accountant", "status": "Done"},
        {"day": "1", "task": "Deferred revenue release", "owner": "Revenue Accountant", "status": "Done"},
        {"day": "2", "task": "AP/AR subledger final; June accruals", "owner": "AP/AR Leads", "status": "Done"},
        {"day": "2", "task": "Prepaid amortization; bonus accrual", "owner": "Staff Accountant", "status": "Done"},
        {"day": "3", "task": "Bank reconciliations", "owner": "Treasury/Accountant", "status": "Done"},
        {"day": "3", "task": "Control account recons (AR/AP/Deferred/FA)", "owner": "Controller", "status": "Done"},
        {"day": "4", "task": "Flux analysis & management flash", "owner": "FP&A", "status": "Done"},
        {"day": "5", "task": "Certify & lock period", "owner": "CFO/Controller", "status": "Done"},
    ]

    # Write transaction files
    write_csv(TXN / "journal_entries.csv", je_rows(journals))
    write_csv(TXN / "sales_orders.csv", sales_orders)
    write_csv(TXN / "ar_invoices.csv", ar_invoices)
    write_csv(TXN / "ar_receipts.csv", ar_receipts)
    write_csv(TXN / "purchase_orders.csv", pos)
    write_csv(TXN / "ap_invoices.csv", ap_invoices)
    write_csv(TXN / "ap_payments.csv", ap_payments)
    write_csv(TXN / "bank_transactions.csv", bank_txns)
    write_csv(TXN / "bank_outstanding_items.csv", bank_outstanding)
    write_csv(TXN / "fixed_assets.csv", fa_register)
    write_csv(TXN / "payroll_register.csv", payroll_register)
    write_csv(TXN / "deferred_revenue_schedule.csv", deferred_schedule)
    write_csv(TXN / "accruals.csv", accrual_rows)
    write_csv(TXN / "prepaid_schedule.csv", prepaid_schedule)
    write_csv(CLOSE / "close_calendar.csv", close_calendar)

    # Validate journals balance
    deb = sum(j.debit for j in journals)
    cred = sum(j.credit for j in journals)
    assert abs(deb - cred) < 0.05, f"Journals out of balance: Dr {deb} Cr {cred}"

    meta = {
        "company": "Meridian CloudWorks, Inc.",
        "period": PERIOD,
        "period_end": PERIOD_END.isoformat(),
        "journal_lines": len(journals),
        "journal_debits": round(deb, 2),
        "journal_credits": round(cred, 2),
        "customers": len(customers),
        "vendors": len(vendors),
        "employees": len(employees),
        "ar_invoices": len(ar_invoices),
        "ap_invoices": len(ap_invoices),
    }
    (ROOT / "data" / "meta.json").write_text(json.dumps(meta, indent=2))
    return meta


def main() -> None:
    meta = generate_all()
    print("Generated Meridian CloudWorks synthetic finance data")
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
