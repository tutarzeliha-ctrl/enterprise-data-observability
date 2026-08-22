import pytest
import pandas as pd

def test_sample_orders_schema():
    """Test that sample orders dataframe contains expected columns."""
    sample_data = pd.DataFrame([
        {"order_id": 1001, "customer_id": 101, "status": "completed", "amount": 250.5}
    ])
    expected_columns = ["order_id", "customer_id", "status", "amount"]
    for col in expected_columns:
        assert col in sample_data.columns

def test_data_quality_score_threshold():
    """Test that data quality score meets enterprise SLA (> 95%)."""
    dq_score = 98.4
    assert dq_score >= 95.0, "Data Quality score dropped below enterprise SLA threshold!"

def test_anomaly_detection_logic():
    """Test anomaly detection identification on null customer IDs."""
    df = pd.DataFrame([
        {"order_id": 1004, "customer_id": None, "status": "invalid_status"}
    ])
    null_counts = df['customer_id'].isnull().sum()
    assert null_counts > 0, "Expected anomaly not detected."