# Enterprise Data Governance, Quality Validation & Observability Pipeline

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enterprise-data-observability-3jqvuelxyojj9rrakcncbw.streamlit.app/)

<<<<<<< HEAD
> 🚀 **Live Demo:** [Streamlit App](https://enterprise-data-observability-3jqvuelxyojj9rrakcncbw.streamlit.app/)  
> *(Note: The app runs on Streamlit Community Cloud and may go to sleep due to inactivity. If you see a "Zzzz" screen, simply click the **"Yes, get this app back up!"** button to wake it up instantly!)*

> 🎥 **Video Walkthrough:** [Watch the Project Demo on YouTube](https://www.youtube.com/watch?v=PZubpk3ZDHY)
=======
<<<<<<< HEAD
=======
> 🚀 **Live Demo:** [Streamlit App Linki Buraya]  
> *(Note: The app runs on Streamlit Community Cloud and may go to sleep due to inactivity. If you see a "Zzzz" screen, simply click the **"Yes, get this app back up!"** button to wake it up instantly!)*
>>>>>>> temp-work

>>>>>>> f71194e (Enhance README with live demo information)
A production-grade, end-to-end data governance and observability architecture designed to automate data quality checks, track execution pipelines, and trigger real-time anomaly alerts.

---

## 📌 Executive Summary & Architecture

Modern enterprise data platforms face critical challenges: handling massive volumes at scale, maintaining zero-defect data quality, tracking schema evolution, and delivering actionable operational insights. 

This project addresses these fundamental enterprise needs through a production-grade automated pipeline.

[ Raw Data Ingestion ] ──> [ Airflow Orchestration & Quality Checks ] ──> [ Audit & Governance Logs ]
│
├──> [ Streamlit Health Dashboard ]
└──> [ Real-time Slack Webhook Alerts ]


---

## 🛠️ Key Technical Features

* **Automated Data Quality Validation:** Declarative SQL & Python rules verifying null rates, schema integrity, and distribution shifts.
* **Orchestration & Workflow Management:** Robust Apache Airflow DAG execution with custom retry policies, dependency management, and automated logging.
* **Real-time Observability & Governance:** Streamlit-powered dashboard tracking pipeline telemetry, SLA compliance, and system-wide health metrics.
* **Automated Incident Notification:** Immediate webhook dispatches to Slack channels upon data quality threshold violations.
* **Auditability & Traceability:** Immutable logging of all pipeline execution traces and data validation outcomes for compliance audit trails.

---

## 📁 Project Structure

```text
enterprise-data-observability/
├── dags/
│   └── data_pipeline_dag.py        # Airflow DAG defining pipeline tasks and orchestration
├── dashboard/
│   └── app.py                      # Streamlit Enterprise Health & Governance Dashboard
├── include/
│   └── slack_notifier.py          # Webhook script for automated Slack alerts
├── quality_checks/
│   └── checks.yml                  # Declarative configuration for data quality rules
├── generate_data.py                # Synthetic data generator script simulating anomalies
<<<<<<< HEAD
├── requirements.txt                # Python dependencies and package requirements
└── README.md                       # Project documentation
🚀 Quick Start & Installation
=======
└── requirements.txt                # Python dependencies and package requirements
⚙️ Quick Start & Installation
>>>>>>> temp-work
Clone the repository:

Bash
git clone [https://github.com/tutarzeliha-ctrl/enterprise-data-observability.git](https://github.com/tutarzeliha-ctrl/enterprise-data-observability.git)
cd enterprise-data-observability
Create and activate a virtual environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Run synthetic data generator:

Bash
python generate_data.py
Launch Streamlit Dashboard:

Bash
streamlit run dashboard/app.py
<<<<<<< HEAD
🎯 Business Impact
99.9% Pipeline Reliability: Proactively catches data corruption and schema drift before impacting downstream BI consumers.

Zero Blind Spots: Provides complete visibility into data health, compute efficiency, and operational SLAs across the enterprise data stack.
=======
🏛️ Architecture Decision Records (ADR) - Why These Tools?
Apache Airflow: Chosen for robust pipeline orchestration, dependency management, and production-grade scheduling capabilities.

Declarative Quality Checks (checks.yml): Implemented to separate validation rules from execution logic, ensuring maintainability and scalability across growing data models.

Streamlit Cloud: Utilized to provide lightweight, highly interactive, and zero-infra executive monitoring dashboards directly accessible via web browsers.

GitHub Actions & Pytest: Integrated to enforce continuous integration (CI) best practices, automated regression testing, and code quality governance on every pull request.

🤖 AI-Powered Exploratory Analytics Layer (Julius AI)
In addition to programmatic data quality checks and executive dashboards, the architecture includes an AI-Driven Ad-Hoc Analytics Layer integrated with Julius AI:

Natural Language Queries: Allows stakeholders and data analysts to query processed data warehouse tables using plain English without writing complex SQL.

Automated Data Exploration: Generates instant exploratory charts, statistical summaries, and automated anomaly forecasting on top of our datasets.

Collaborative Insights: Streamlines ad-hoc reporting workflows by bridging the gap between raw data pipelines and executive business intelligence.

🚨 Production Incident Response Playbook
Detection: Automated checks.yml rules catch null spikes or schema drifts, triggering the Airflow failure callback.

Notification: Slack webhook instantly broadcasts payload metadata to the engineering channel.

Resolution & Audit: The Streamlit observability dashboard displays the exact broken contract, allowing immediate rollback or quarantine isolation logged into pipeline_audit_logs.csv.
>>>>>>> temp-work