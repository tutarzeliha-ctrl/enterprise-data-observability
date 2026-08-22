# Enterprise Data Governance, Quality Validation & Observability Pipeline

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enterprise-data-observability-3jqvuelxyojj9rrakcncbw.streamlit.app/)


A production-grade, end-to-end data governance and observability architecture designed to automate data quality checks, track execution pipelines, and trigger real-time anomaly alerts.

---

## 🚀 Architectural Overview & Features

* **Data Quality & Observability:** Implements rigorous validation checks (missing ID checks, duplicate detection, row count thresholds, and status validation) using automated data quality frameworks.
* **Pipeline Orchestration:** Modeled with **Apache Airflow** DAGs to manage execution schedules, task dependencies, and operational workflows.
* **Interactive Monitoring Dashboard:** Built with **Streamlit** to provide a real-time health score, active table metrics, and live execution audit logs.
* **Automated Alerting Engine:** Simulates automated notifications via **Slack webhooks** upon data anomaly detection or pipeline warning triggers.
* **Data Governance & Auditing:** Maintains comprehensive audit logs (`pipeline_audit_logs.csv`) recording execution statuses, record counts, and anomaly timestamps.

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

---

## 🏛️ Architecture Decision Records (ADR) - Why These Tools?

* **Apache Airflow:** Chosen for robust pipeline orchestration, dependency management, and production-grade scheduling capabilities.
* **Declarative Quality Checks (`checks.yml`):** Implemented to separate validation rules from execution logic, ensuring maintainability and scalability across growing data models.
* **Streamlit Cloud:** Utilized to provide lightweight, highly interactive, and zero-infra executive monitoring dashboards directly accessible via web browsers.
* **GitHub Actions & Pytest:** Integrated to enforce continuous integration (CI) best practices, automated regression testing, and code quality governance on every pull request.

---

## 🤖 AI-Powered Exploratory Analytics Layer (Julius AI)

In addition to programmatic data quality checks and executive dashboards, the architecture includes an **AI-Driven Ad-Hoc Analytics Layer** integrated with **Julius AI**:
* **Natural Language Queries:** Allows stakeholders and data analysts to query processed data warehouse tables using plain English without writing complex SQL.
* **Automated Data Exploration:** Generates instant exploratory charts, statistical summaries, and automated anomaly forecasting on top of our dbt-modeled datasets.
* **Collaborative Insights:** Streamlines ad-hoc reporting workflows by bridging the gap between raw data pipelines and executive business intelligence.
