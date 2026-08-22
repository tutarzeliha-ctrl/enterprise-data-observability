import streamlit as st
import pandas as pd
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from generate_data import generate_mock_observability_data

st.set_page_config(
    page_title="Enterprise Data Observability Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Enterprise Data Governance & Observability Dashboard")
st.markdown("Monitor real-time data quality metrics, automated anomaly detection, pipeline execution statuses, and Slack alert logs.")

# Sidebar Controls
st.sidebar.header("Pipeline Controls")
if st.sidebar.button("Run Data Generation & Quality Scan"):
    generate_mock_observability_data()
    st.sidebar.success("Synthetic data generated & checks executed!")

# Main layout - Metrics Overview
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Tables Monitored", "14", "+2")
col2.metric("Data Quality Score", "98.4%", "+0.5%")
col3.metric("Failed Checks (24h)", "1", "-2")
col4.metric("Slack Alerts Sent", "4", "+1")

st.markdown("---")

# Section 1: Recent Data Quality Test Results (Original Table Preserved)
st.subheader("📋 Recent Data Quality Test Results")
data = {
    "Table Name": ["raw_orders", "raw_customers", "raw_orders", "raw_products"],
    "Check Type": ["Row Count > 0", "Missing ID Check", "Status Validation", "Duplicate Check"],
    "Status": ["PASSED", "PASSED", "PASSED", "PASSED"],
    "Execution Time": ["2026-08-23 08:00:00", "2026-08-23 08:00:00", "2026-08-23 08:00:00", "2026-08-23 08:00:00"]
}
df_original = pd.DataFrame(data)
st.dataframe(df_original, use_container_width=True)

st.markdown("---")

# Section 2: Real-time Mock Anomaly Detection (New Feature)
st.subheader("🔍 Live Anomaly Detection Sample (`raw_orders`)")
if os.path.exists("raw_orders.csv"):
    df_orders = pd.read_csv("raw_orders.csv")
    st.dataframe(df_orders, use_container_width=True)
    st.info("ℹ️ Notice row index 3: `customer_id` is missing (`None`) and `status` is `invalid_status`. These anomalies trigger automated Soda checks and Slack alerts.")
else:
    st.warning("Click the 'Run Data Generation & Quality Scan' button on the sidebar to load live sample data.")

st.markdown("---")

# Section 3: Pipeline Audit & Execution Logs (New Feature)
st.subheader("📜 Pipeline Audit & Execution Logs")
if os.path.exists("pipeline_audit_logs.csv"):
    df_audit = pd.read_csv("pipeline_audit_logs.csv")
    st.dataframe(df_audit, use_container_width=True)
else:
    st.warning("Audit logs will appear here after running the pipeline scan.")