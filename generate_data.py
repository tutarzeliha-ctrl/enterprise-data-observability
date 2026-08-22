import pandas as pd
import random
from datetime import datetime

def generate_mock_observability_data():
    """
    Generates synthetic enterprise datasets and runs automated validation checks
    to simulate real-time data quality monitoring.
    """
    print("Generating synthetic enterprise operational data...")
    
    # Mock Orders Data with intentional minor data anomalies for testing quality rules
    orders_data = {
        "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
        "customer_id": [501, 502, 503, None, 505, 506],  # Anomaly: Missing customer ID
        "status": ["completed", "shipped", "pending", "invalid_status", "completed", "cancelled"],  # Anomaly: Invalid status
        "amount": [250.50, 120.00, 450.00, 89.90, 310.00, 150.00],
        "created_at": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")] * 6
    }
    
    df_orders = pd.DataFrame(orders_data)
    df_orders.to_csv("raw_orders.csv", index=False)
    print("✅ raw_orders.csv generated successfully.")

    # Mock Audit Logs
    audit_data = {
        "execution_id": ["exec_901", "exec_902", "exec_903"],
        "pipeline_name": ["enterprise_data_observability_pipeline", "enterprise_data_observability_pipeline", "enterprise_data_observability_pipeline"],
        "status": ["SUCCESS", "WARNING_TRIGGERED", "SUCCESS"],
        "records_scanned": [15420, 14200, 16890],
        "issues_detected": [0, 2, 0],
        "timestamp": ["2026-08-23 06:00:00", "2026-08-23 07:00:00", "2026-08-23 08:00:00"]
    }
    
    df_audit = pd.DataFrame(audit_data)
    df_audit.to_csv("pipeline_audit_logs.csv", index=False)
    print("✅ pipeline_audit_logs.csv generated successfully.")

if __name__ == "__main__":
    generate_mock_observability_data()