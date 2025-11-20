import numpy as np
from modules.explanations import metric_explanations

def calculate_metrics(budgeted, actual, opex, revenue, investment, cashflow, cts, tco):

    def safe_div(a, b):
        return a / b if b != 0 else np.nan

    # Calculations
    cost_variance = actual - budgeted
    cpi = safe_div(budgeted, actual)
    opex_ratio = safe_div(opex, revenue)
    roi = safe_div((cashflow - investment), investment)
    budget_utilization = safe_div(actual, budgeted)
    payback_period = safe_div(investment, cashflow)
    efficiency_ratio = safe_div(opex, revenue)
    gross_profit_margin = safe_div((revenue - opex), revenue)

    metrics = [
        ("Cost Variance (CV)", cost_variance),
        ("Cost Performance Index (CPI)", cpi),
        ("Operating Expense Ratio (OER)", opex_ratio),
        ("Total Cost of Ownership (TCO)", tco),
        ("Return on Investment (ROI)", roi),
        ("Cost to Serve (CTS)", cts),
        ("Budget Utilization Rate (BUR)", budget_utilization),
        ("Payback Period (PP)", payback_period),
        ("Efficiency Ratio (ER)", efficiency_ratio),
        ("Gross Profit Margin (GPM)", gross_profit_margin),
    ]

    result = []
    for metric, value in metrics:
        explanation = metric_explanations(metric, value)
        result.append({
            "Metric": metric,
            "Value": round(value, 4) if value == value else "N/A",
            "Interpretation": explanation["interpretation"],
            "Implication": explanation["implication"]
        })

    return result
