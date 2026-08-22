import os
import requests
import json
from datetime import datetime

def send_slack_alert(anomaly_details: dict):
    """
    Dispatches automated anomaly alerts and root-cause summaries to Slack webhook.
    """
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "https://hooks.slack.com/services/T00/B00/X00")
    
    payload = {
        "channel": "#data-alerts",
        "username": "DataObservabilityBot",
        "icon_emoji": ":warning:",
        "text": f"🚨 *Data Quality Anomaly Detected!*\n"
                f"• *Table:* `{anomaly_details.get('table_name')}`\n"
                f"• *Issue:* {anomaly_details.get('issue_description')}\n"
                f"• *AI Root Cause:* {anomaly_details.get('root_cause')}\n"
                f"• *Timestamp:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    }
    
    # In production, this sends the actual POST request:
    # response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    # return response.status_code
    
    print(f"[SIMULATION] Slack alert dispatched to #data-alerts for table: {anomaly_details.get('table_name')}")
    return 200

if __name__ == "__main__":
    sample_anomaly = {
        "table_name": "raw_orders",
        "issue_description": "customer_id is missing (None) and status is invalid_status",
        "root_cause": "Schema drift or upstream payload corruption identified in ingestion API."
    }
    send_slack_alert(sample_anomaly)