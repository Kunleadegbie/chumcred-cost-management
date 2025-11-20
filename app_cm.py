import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image
from io import BytesIO

# INTERNAL MODULES
from modules.calculators import calculate_metrics
from modules.explanations import metric_explanations
from modules.database import init_db
from modules.auth import login_screen
from modules.admin_ui import admin_dashboard

# -----------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------
st.set_page_config(
    page_title="Chumcred Limited – Cost Management Assessment Tool",
    page_icon="💼",
    layout="wide"
)

# -----------------------------------------------------
# INITIALIZE DB + SESSION
# -----------------------------------------------------
init_db()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.session_state["role"] = None

# -----------------------------------------------------
# LOGIN SCREEN (STOP EVERYTHING ELSE IF NOT LOGGED IN)
# -----------------------------------------------------
if not st.session_state["logged_in"]:
    login_screen()
    st.stop()      # 🔥 Critical — prevents the rest of the page from rendering


# -----------------------------------------------------
# SIDEBAR USER INFO + LOGOUT
# -----------------------------------------------------
st.sidebar.success(f"Logged in as: {st.session_state['username']} ({st.session_state['role']})")

if st.sidebar.button("Logout"):
    st.session_state.clear()
    st.rerun()


# -----------------------------------------------------
# COMPANY LOGO
# -----------------------------------------------------
logo_path = os.path.join("assets", "logo.png")
try:
    logo = Image.open(logo_path)
    st.image(logo, width=150)
except Exception as e:
    st.warning(f"Logo not found or unreadable: {e}")


# -----------------------------------------------------
# TITLE & INTRO
# -----------------------------------------------------
st.title("💼 Chumcred Limited – Cost Management Assessment Tool")
st.markdown("""
This tool helps organizations assess cost efficiency, financial discipline, and 
overall business performance using key cost-management metrics.  
Enter your financial figures below to get instant analysis with explanations.
""")


# -----------------------------------------------------
# ADMIN DASHBOARD OPTION
# -----------------------------------------------------
if st.session_state["role"] == "admin":
    st.sidebar.markdown("### ⚙ Admin Menu")
    admin_option = st.sidebar.selectbox("Admin Actions", ["Use App", "Manage Users"])

    if admin_option == "Manage Users":
        admin_dashboard()
        st.stop()    # Stop here and do NOT show the cost calculator


# -----------------------------------------------------
# MAIN PAGE INPUTS (ONLY SHOW AFTER LOGIN)
# -----------------------------------------------------
st.subheader("📥 Enter Company Financial Data")

col1, col2 = st.columns(2)

with col1:
    budgeted_cost = st.number_input("Budgeted Cost", min_value=0.0, value=0.0)
    actual_cost = st.number_input("Actual Cost", min_value=0.0, value=0.0)
    operating_expense = st.number_input("Operating Expense", min_value=0.0, value=0.0)
    revenue = st.number_input("Revenue", min_value=0.0, value=0.0)

with col2:
    investment = st.number_input("Investment Amount", min_value=0.0, value=0.0)
    annual_cash_inflow = st.number_input("Annual Cash Inflow", min_value=0.0, value=0.0)
    cost_to_serve = st.number_input("Cost to Serve", min_value=0.0, value=0.0)
    tco = st.number_input("Total Cost of Ownership (e.g., CapEx + OpEx)", min_value=0.0, value=0.0)

st.markdown("---")


# -----------------------------------------------------
# CALCULATE RESULTS
# -----------------------------------------------------
if st.button("🔍 Analyse Cost Metrics"):

    results = calculate_metrics(
        budgeted_cost,
        actual_cost,
        operating_expense,
        revenue,
        investment,
        annual_cash_inflow,
        cost_to_serve,
        tco
    )

    st.subheader("📊 Cost Management Result Dashboard")

    df = pd.DataFrame(results)
    st.dataframe(df, width=1200, height=500)

    # -----------------------------------------------------
    # EXCEL DOWNLOAD
    # -----------------------------------------------------
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Cost Analysis")
    excel_data = output.getvalue()

    st.download_button(
        label="⬇️ Download Excel Report",
        data=excel_data,
        file_name="chumcred_cost_management_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.success("Analysis Complete – powered by Chumcred Limited.")
