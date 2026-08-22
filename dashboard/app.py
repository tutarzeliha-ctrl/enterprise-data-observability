from datetime import datetime
import numpy as np
import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Enterprise Data Governance & Observability Dashboard",
    page_icon="🛡️",
    layout="wide",
)

# Custom Styling for Enterprise Look
st.markdown(
    """
    <style>
    .main { background-color: #f8f9fa; }
    .metric-card { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""",
    unsafe_allow_html=True,
)

# Title & Header
st.markdown(
    "# 🛡️ Enterprise Data Governance & Observability Dashboard"
)
st.markdown(
    "Monitor real-time data quality metrics, automated anomaly detection, Data Freshness SLA, lineage, and Slack alert logs."
)

# Sidebar Controls
st.sidebar.markdown("## Pipeline Controls")
run_scan = st.sidebar.button("Run Data Generation & Quality Scan")

# Session state initialization for dynamic simulation
if "scanned" not in st.session_state:
    st.session_state.scanned = False

if run_scan:
  st.session_state.scanned = True

# Top Metrics Row
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
  st.metric(
      label="Active Tables Monitored", value="14", delta="+2", delta_color="normal"
  )
with col2:
  st.metric(
      label="Data Quality Score",
      value="98.4%",
      delta="+0.5%",
      delta_color="normal",
  )
with col3:
  st.metric(
      label="Failed Checks (24h)", value="1", delta="-2", delta_color="inverse"
  )
with col4:
  st.metric(
      label="Slack Alerts Sent", value="4", delta="+1", delta_color="normal"
  )
with col5:
  st.metric(
      label="Data Freshness SLA",
      value="99.8%",
      delta="On Track",
      delta_color="normal",
  )

st.markdown("---")

# Architecture Flow Section
st.markdown("## 🧬 End-to-End Data Lineage & Architecture Flow")
st.markdown(
    "Tracks data flow from ingestion sources through governance layers to"
    " analytics and reverse ETL destinations."
)

st.code(
    """
[Raw Sources / Ingestion]
         │
         ▼
[staging (dbt Core) - Schema & Type Validation]
         │
         ▼
[marts (Enterprise Data Warehouse) - Business Logic]
         │
         ├─────────────────────────────────────┐
         ▼                                     ▼
[Interactive Dashboard (Streamlit)]    [Reverse ETL / Slack Webhook Alerts]
    """,
    language="text",
)

st.markdown("---")

# Recent Data Quality Test Results & Coverage Table
st.markdown("## 📋 Recent Data Quality Test Results & Coverage")

quality_data = pd.DataFrame({
    "Table Name": ["raw_orders", "raw_customers", "raw_orders", "raw_products"],
    "Check Type": [
        "Row Count > 0",
        "Missing ID Check",
        "Status Validation",
        "Duplicate Check",
    ],
    "Status": ["PASSED", "PASSED", "PASSED", "PASSED"],
    "Coverage": ["100%", "100%", "95%", "100%"],
})

st.dataframe(quality_data, use_container_width=True, hide_index=False)

st.markdown("---")

# Live Anomaly Detection Sample Section
st.markdown("## 🔍 Live Anomaly Detection Sample (`raw_orders`)")

if not st.session_state.scanned:
  st.info(
      "Click the 'Run Data Generation & Quality Scan' button on the sidebar to"
      " load live sample data and trigger anomaly analysis."
  )
else:
  # Simulated anomaly dataset
  anomaly_df = pd.DataFrame({
      "order_id": [1001, 1002, 1003, 1004, 1005],
      "customer_id": ["C01", "C02", "C03", None, "C05"],
      "status": ["completed", "shipped", "pending", "invalid_status", "completed"],
      "amount": [250.5, 120.0, 450.0, 89.9, 310.0],
      "created_at": [
          "2026-08-23 22:00:20",
          "2026-08-23 22:00:20",
          "2026-08-23 22:00:20",
          "2026-08-23 22:00:20",
          "2026-08-23 22:00:20",
      ],
  })

  st.dataframe(anomaly_df, use_container_width=True)

  # Error alert box simulating Slack webhook trigger
  st.error(
      "⚠️ Anomaly Detected at row index 3: `customer_id` is missing (None) and"
      " `status` is invalid_status."
  )
  st.warning(
      "🤖 **AI-Assisted Root Cause Summary:** Schema drift or upstream payload"
      " corruption identified in `raw_orders` ingestion API. Automated Slack"
      " webhook alert dispatched to `#data-alerts` channel."
  )

st.markdown("---")

# NEW: Julius AI-Driven Ad-Hoc Analytics Section
st.markdown(
    "## 🤖 AI-Driven Ad-Hoc Analytics Assistant (Julius AI Integration)"
)
st.info(
    "💡 **Modern AI Data Stack:** Business stakeholders can query processed dbt"
    " warehouse tables using plain English via Julius AI to instantly generate"
    " charts, predictive forecasts, and automated statistical insights."
)

with st.expander("💬 Test AI Natural Language Query (Interactive Simulation)"):
  user_query = st.text_input(
      "Ask a question about your enterprise data (e.g., 'Show me top 5"
      " customers by order amount last month')",
      "Show me churn trends and anomaly forecasts for raw_orders",
  )
  if st.button("Generate AI Insights"):
    with st.spinner("Julius AI is analyzing dbt modeled datasets..."):
      st.success("✅ Analysis Complete!")
      st.markdown(f"**Query:** `{user_query}`")
      st.markdown(
          "**AI Generated Insight:** *Trend analysis indicates a 4.2% drop in"
          " order frequency during off-peak hours. Anomaly scores remain within"
          " acceptable governance thresholds (SLA: 99.8%).*"
      )
      # Simulated AI generated chart
      ai_chart_data = pd.DataFrame(
          np.random.randn(20, 2),
          columns=["Order Volume Trend", "Anomaly Risk Score"],
      )
      st.line_chart(ai_chart_data)

st.markdown("---")

# Pipeline Audit & Execution Logs
st.markdown("## 📜 Pipeline Audit & Execution Logs")

audit_logs = pd.DataFrame({
    "execution_id": ["exec_901", "exec_902", "exec_903"],
    "pipeline_name": [
        "enterprise_data_observability_pipeline",
        "enterprise_data_observability_pipeline",
        "enterprise_data_observability_pipeline",
    ],
    "status": ["SUCCESS", "WARNING_TRIGGERED", "SUCCESS"],
    "records_scanned": [15420, 14200, 16890],
    "issues_detected": [0, 2, 0],
    "timestamp": [
        "2026-08-23 06:00:00",
        "2026-08-23 07:00:00",
        "2026-08-23 08:00:00",
    ],
})

st.dataframe(audit_logs, use_container_width=True, hide_index=True)