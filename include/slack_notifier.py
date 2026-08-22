import os
import requests

def send_slack_alert(message: str, webhook_url: str = None):
    """
    Sends an automated webhook notification to a Slack channel 
    when a data quality check fails or pipeline issues occur.
    """
    url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")
    
    if not url:
        print("⚠️ Warning: Slack Webhook URL not found! Printing notification to console:")
        print(f"[SIMULATION SLACK ALERT]: {message}")
        return

    payload = {
        "text": f"🚨 *Enterprise Data Observability Alert*\n{message}"
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Slack notification sent successfully.")
        else:
            print(f"❌ Failed to send Slack notification. Status code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error occurred during Slack notification: {str(e)}")

if __name__ == "__main__":
    # Test execution
    send_slack_alert("Test alert: Data quality validation executed successfully.")