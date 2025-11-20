def metric_explanations(metric, value):

    if metric == "Cost Variance (CV)":
        return {
            "interpretation": "Shows whether actual cost is above or below budget.",
            "implication": "Positive CV means overspending; negative CV means cost savings."
        }

    if metric == "Cost Performance Index (CPI)":
        return {
            "interpretation": "CPI < 1 means cost inefficiency; CPI > 1 means good cost control.",
            "implication": "A low CPI indicates poor project cost management."
        }

    if metric == "Operating Expense Ratio (OER)":
        return {
            "interpretation": "Measures how much revenue is consumed by operating expenses.",
            "implication": "High OER means the business is expensive to run and margins are thin."
        }

    if metric == "Total Cost of Ownership (TCO)":
        return {
            "interpretation": "Shows the full lifetime cost of owning an asset.",
            "implication": "High TCO implies heavy long-term financial commitment."
        }

    if metric == "Return on Investment (ROI)":
        return {
            "interpretation": "Indicates the profitability of an investment.",
            "implication": "Negative ROI means the investment is destroying value."
        }

    if metric == "Cost to Serve (CTS)":
        return {
            "interpretation": "Measures cost of serving each customer/product segment.",
            "implication": "High CTS reduces profitability and signals inefficiency."
        }

    if metric == "Budget Utilization Rate (BUR)":
        return {
            "interpretation": "Shows how much of the approved budget was spent.",
            "implication": "BUR above 100% signals overspending and weak controls."
        }

    if metric == "Payback Period (PP)":
        return {
            "interpretation": "Time required to recover investment from cash inflows.",
            "implication": "Long payback period means slow capital recovery."
        }

    if metric == "Efficiency Ratio (ER)":
        return {
            "interpretation": "Measures operating efficiency.",
            "implication": "Lower ER means better operational efficiency."
        }

    if metric == "Gross Profit Margin (GPM)":
        return {
            "interpretation": "Shows how much revenue remains after covering expenses.",
            "implication": "Low GPM means costs are too high or prices too low."
        }

    return {"interpretation": "", "implication": ""}
