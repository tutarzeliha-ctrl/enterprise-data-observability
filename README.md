# Enterprise Data Governance, Quality Validation & Observability Pipeline

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enterprise-data-observability-3jqvuelxyojj9rrakcncbw.streamlit.app/)

> 🚀 **Live Demo:** [Streamlit App](https://enterprise-data-observability-3jqvuelxyojj9rrakcncbw.streamlit.app/)  
> *(Note: The app runs on Streamlit Community Cloud and may go to sleep due to inactivity. If you see a "Zzzz" screen, simply click the **"Yes, get this app back up!"** button to wake it up instantly!)*

> 🎥 **Video Walkthrough:** [Watch the Project Demo on YouTube](https://www.youtube.com/watch?v=PZubpk3ZDHY)

---

## 📌 Executive Summary & Architecture

Modern enterprise data platforms face critical challenges: handling massive volumes at scale, maintaining zero-defect data quality, tracking schema evolution, and delivering actionable operational insights. 

This project addresses these fundamental enterprise needs through a production-grade automated pipeline.

```text
[ Raw Data Ingestion ] ──> [ Airflow Orchestration & Quality Checks ] ──> [ Audit & Governance Logs ]
                                         │
                                         ├──> [ Streamlit Health Dashboard ]
                                         └──> [ Real-time Slack Webhook Alerts ]
🛠️ Key Technical FeaturesAutomated Data Quality Validation: Declarative SQL & Python rules verifying null rates, schema integrity, and distribution shifts.Orchestration & Workflow Management: Robust Apache Airflow DAG execution with custom retry policies, dependency management, and automated logging.Real-time Observability & Governance: Streamlit-powered dashboard tracking pipeline telemetry, SLA compliance, and system-wide health metrics.Automated Incident Notification: Immediate webhook dispatches to Slack channels upon data quality threshold violations.Auditability & Traceability: Immutable logging of all pipeline execution traces and data validation outcomes for compliance audit trails.📁 Project StructurePlaintextenterprise-data-observability/
├── dags/
│   └── data_pipeline_dag.py        # Airflow DAG defining pipeline tasks and orchestration
├── dashboard/
│   └── app.py                      # Streamlit Enterprise Health & Governance Dashboard
├── include/
│   └── slack_notifier.py          # Webhook script for automated Slack alerts
├── quality_checks/
│   └── checks.yml                  # Declarative configuration for data quality rules
├── generate_data.py                # Synthetic data generator script simulating anomalies
├── requirements.txt                # Python dependencies and package requirements
└── README.md                       # Project documentation
🚀 Quick Start & InstallationClone the repository:Bashgit clone [https://github.com/tutarzeliha-ctrl/enterprise-data-observability.git](https://github.com/tutarzeliha-ctrl/enterprise-data-observability.git)
cd enterprise-data-observability
Create and activate a virtual environment:Bashpython -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:Bashpip install -r requirements.txt
Run synthetic data generator:Bashpython generate_data.py
Launch Streamlit Dashboard:Bashstreamlit run dashboard/app.py
🎯 Business Impact99.9% Pipeline Reliability: Proactively catches data corruption and schema drift before impacting downstream BI consumers.Zero Blind Spots: Provides complete visibility into data health, compute efficiency, and operational SLAs across the enterprise data stack.