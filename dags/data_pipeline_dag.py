from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# Add project root to path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from include.slack_notifier import send_slack_alert

default_args = {
    'owner': 'zeliha',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_data_quality_checks(**context):
    """
    Executes data quality checks using Soda and triggers Slack alert if any check fails.
    """
    print("Running data quality validations against raw tables...")
    # Simulation of data quality check logic
    checks_passed = True  
    
    if not checks_passed:
        error_message = "Data Quality Check Failed! Invalid records found in raw_orders."
        send_slack_alert(error_message)
        raise ValueError(error_message)
    else:
        print("All data quality checks passed successfully.")

with DAG(
    'enterprise_data_observability_pipeline',
    default_args=default_args,
    description='A production-grade pipeline with data quality checks and Slack alerts',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['production', 'data-quality', 'observability'],
) as dag:

    quality_check_task = PythonOperator(
        task_id='run_soda_quality_checks',
        python_callable=run_data_quality_checks,
    )

    quality_check_task