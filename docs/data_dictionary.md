# Enterprise Data Dictionary & Governance Reference

This document outlines the core datasets, schemas, business definitions, and quality SLA thresholds tracked within the Enterprise Data Observability platform.

## 1. Tables & Schema Definitions

### `raw_orders`
Tracks raw e-commerce transaction payloads coming from upstream ingestion APIs.
* **`order_id`** (Integer, Primary Key): Unique identifier for each order. Must be non-null and unique.
* **`customer_id`** (Integer, Foreign Key): Reference to the customer placing the order. Must not be null.
* **`status`** (String): Current status of the order. Allowed values: `completed`, `shipped`, `pending`. (Monitored via status validation checks).
* **`amount`** (Float): Monetary value of the order transaction.
* **`created_at`** (Timestamp): Exact UTC timestamp when the order payload was ingested.

### `raw_customers`
Maintains customer profile records and account states.
* **`customer_id`** (Integer, Primary Key): Unique customer identifier.
* **`signup_date`** (Timestamp): Account creation timestamp.

---

## 2. Data Quality SLA & Monitoring Thresholds
* **Data Freshness SLA:** Must remain $\ge 99.5\%$ on-track (Max allowed data lag: 15 minutes).
* **Row Count Validation:** Daily row count variance must not exceed $\pm 20\%$ compared to the 7-day rolling average.
* **Null Check Threshold:** Critical fields (`order_id`, `customer_id`) enforce a strict $0\%$ tolerance for null values.