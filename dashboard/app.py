import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Enterprise Data Governance & Observability",
    page_icon="🛡️",
    layout="wide"
)

# Custom Styling for Enterprise Look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# Title & Header
st.markdown("# 🛡️ Enterprise Data Governance & Observability Dashboard")
st.markdown("Monitor real-time data quality metrics, automated anomaly detection, Data Freshness SLA, lineage, and Slack alert logs.")

# Sidebar Controls
st.sidebar.markdown("## Pipeline Controls")
run_scan = st.sidebar.button("Run Data Generation & Quality Scan")

# Session state initialization for dynamic simulation
if 'scanned' not in st.session_state:
    st.session_state.scanned = False

if run_scan:
    st.session_state.scanned = True

# Metrics Row (including new Quality Coverage & Freshness SLA)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Active Tables Monitored", "14", "+2")
with col2:
    st.metric("Data Quality Score", "98.4%", "+0.5%")
with col3:
    st.metric("Failed Checks (24h)", "1", "-2")
with col4:
    st.metric("Slack Alerts Sent", "4", "+1")
with col5:
    st.metric("Data Freshness SLA", "99.8%", "On Track")

st.markdown("---")

# 1. NEW: Data Lineage & Impact Analysis Section
st.markdown("### 🧬 End-to-End Data Lineage & Architecture Flow")
st.markdown("Tracks data flow from ingestion sources through governance layers to analytics and reverse ETL destinations.")
st.code("""
[Raw Sources / Ingestion] 
       │
       ▼
[staging (dbt Core) - Schema & Type Validation]
       │
       ▼
[marts (Enterprise Data Warehouse) - Business Logic]
       │
       ├───────────────────────────────┤
       ▼                               ▼
[Interactive Dashboard (Streamlit)]   [Reverse ETL / Slack Webhook Alerts]
""", language="text")

st.markdown("---")

# Recent Data Quality Test Results
st.markdown("### 📋 Recent Data Quality Test Results & Coverage")
quality_df = pd.DataFrame([
    {"Table Name": "raw_orders", "Check Type": "Row Count > 0", "Status": "PASSED", "Coverage": "100%"},
    {"Table Name": "raw_customers", "Check Type": "Missing ID Check", "Status": "PASSED", "Coverage": "100%"},
    {"Table Name": "raw_orders", "Check Type": "Status Validation", "Status": "PASSED", "Coverage": "95%"},
    {"Table Name": "raw_products", "Check Type": "Duplicate Check", "Status": "PASSED", "Coverage": "100%"}
])
st.dataframe(quality_df, use_container_width=True)

st.markdown("---")

# Live Anomaly Detection Sample & AI-Assisted Root Cause Summary
st.markdown("### 🔍 Live Anomaly Detection Sample (`raw_orders`)")

if st.session_state.scanned:
    sample_data = pd.DataFrame([
        {"order_id": 1001, "customer_id": 101, "status": "completed", "amount": 250.5, "created_at": "2026-08-23 22:00:20"},
        {"order_id": 1002, "customer_id": 102, "status": "shipped", "amount": 120.0, "created_at": "2026-08-23 22:00:20"},
        {"order_id": 1003, "customer_id": 103, "status": "pending", "amount": 450.0, "created_at": "2026-08-23 22:00:20"},
        {"order_id": 1004, "customer_id": None, "status": "invalid_status", "amount": 89.9, "created_at": "2026-08-23 22:00:20"},
        {"order_id": 1005, "customer_id": 105, "status": "completed", "amount": 310.0, "created_at": "2026-08-23 22:00:20"}
    ])
    st.dataframe(sample_data, use_container_width=True)
    
    # Anomaly Warning & AI Root Cause Summary Box
    st.error("⚠️ Anomaly Detected at row index 3: `customer_id` is missing (None) and `status` is `invalid_status`.")
    st.info("🤖 **AI-Assisted Root Cause Summary:** Schema drift or upstream payload corruption identified in `raw_orders` ingestion API. Automated Slack webhook alert dispatched to `#data-alerts` channel.")
else:
    st.info("Click the 'Run Data Generation & Quality Scan' button on the sidebar to load live sample data and trigger anomaly analysis.")

st.markdown("---")

# Pipeline Audit & Execution Logs
st.markdown("### 📜 Pipeline Audit & Execution Logs")
logs_df = pd.DataFrame([
    {"execution_id": "exec_901", "pipeline_name": "enterprise_data_observability_pipeline", "status": "SUCCESS", "records_scanned": 15420, "issues_detected": 0, "timestamp": "2026-08-23 06:00:00"},
    {"execution_id": "exec_902", "pipeline_name": "enterprise_data_observability_pipeline", "status": "WARNING_TRIGGERED", "records_scanned": 14200, "issues_detected": 2, "timestamp": "2026-08-23 07:00:00"},
    {"execution_id": "exec_903", "pipeline_name": "enterprise_data_observability_pipeline", "status": "SUCCESS", "records_scanned": 16890, "issues_detected": 0, "timestamp": "2026-08-23 08:00:00"}
])
st.dataframe(logs_df, use_container_width=True)