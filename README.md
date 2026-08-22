# Enterprise Data Governance, Quality Validation & Observability Pipeline

A production-grade, end-to-end data governance and observability architecture designed to automate data quality checks, track execution pipelines, and trigger real-time anomaly alerts.

---

## 🚀 Architectural Overview & Features

* **Data Quality & Observability:** Implements rigorous validation checks (missing ID checks, duplicate detection, row count thresholds, and status validation) using automated data quality frameworks.
* **Pipeline Orchestration:** Modeled with **Apache Airflow** DAGs to manage execution schedules, task dependencies, and operational workflows.
* **Interactive Monitoring Dashboard:** Built with **Streamlit** to provide a real-time health score, active table metrics, and live execution audit logs.
* **Automated Alerting Engine:** Simulates automated notifications via **Slack webhooks** upon data anomaly detection or pipeline warning triggers.
* **Data Governance & Auditing:** Maintains comprehensive audit logs (`pipeline_audit_logs.csv`) recording execution statuses, record counts, and anomaly timestamps.

---

## 📊 Live Streamlit Dashboard Preview

The interactive Streamlit application provides a real-time command center for data engineers and stakeholders to monitor enterprise data health:
* **System Health Score:** Dynamic tracking of pipeline success rates and anomaly indicators.
* **Audit Trail & Logs:** Detailed queryable table of recent execution runs.
* **Interactive Controls:** Trigger checks and review data quality metrics on the fly.

*(If you deploy your Streamlit app to Streamlit Community Cloud, you can add your live link here!)*

---

## 🛠️ Tech Stack

* **Orchestration:** Apache Airflow
* **Data Quality:** Python, Custom Check Rules (`checks.yml`)
* **Dashboard & UI:** Streamlit, Pandas
* **Alerting & Notification:** Slack Webhooks
* **Version Control & CI/CD:** Git, GitHub

---

## 📁 Project Structure

```text
enterprise-data-observability/
│
├── dags/
│   └── data_pipeline_dag.py        # Airflow DAG defining pipeline tasks and orchestration
├── dashboard/
│   └── app.py                      # Streamlit Enterprise Health & Governance Dashboard
├── include/
│   └── slack_notifier.py           # Webhook script for automated Slack alerts
├── quality_checks/
│   └── checks.yml                  # Declarative configuration for data quality rules
├── .gitignore                      # Git exclusion rules for virtual environments and logs
├── generate_data.py                # Synthetic data generator script simulating anomalies
└── requirements.txt                # Python dependencies and package requirements

⚙️ Quick Start & Installation
Clone the repository:

Bash
git clone [https://github.com/tutarzeliha-ctrl/enterprise-data-observability.git](https://github.com/tutarzeliha-ctrl/enterprise-data-observability.git)
cd enterprise-data-observability
Create and activate a virtual environment:

Bash
python -m venv venv
venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Generate data and run the dashboard:

Bash
python generate_data.py
streamlit run dashboard/app.py
