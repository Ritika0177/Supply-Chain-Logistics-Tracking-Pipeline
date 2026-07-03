# Supply Chain Logistics & Inventory Optimization Tracking Pipeline

This repository hosts a data pipeline and interactive business intelligence dashboard designed to monitor warehouse shipping parameters, isolate data anomalies, and improve operational delivery metrics for enterprise logistics systems. The codebase handles the transformation of unstructured shipping logs, maps them to a relational database schema, and renders critical tracking metrics via an analytical dashboard.

---

## Operational Architecture & Technical Setup

- **Language Core:** Python 3.x
- **Data Arrays Processing:** Pandas & NumPy
- **Relational Storage Configuration:** In-Memory SQLite3
- **Visualization Engineering:** Streamlit Application Framework & Matplotlib

---

## Data Pipeline Logic & Data Cleaning Execution

The system automatically simulates raw distribution center logs and models real-world errors before feeding the data to the executive interface. 

### Data Anomaly Interception
To preserve accounting and data reporting accuracy, the backend script runs an Exploratory Data Analysis function that intercepts erratic transactional data streams, specifically negative pricing values which indicate corrupted billing logs. These anomalous records are programmatically isolated and dropped from the dataset before data injection occurs.

### Structural Database Mapping
Once cleaned, the structured records are imported into an in-memory SQLite table named `logistics_pipeline` configured with the following schema matrix:

- **Order_ID (Primary Identifier):** Alphanumeric key mapping specific individual shipments.
- **Region:** Geographic market division (North Zone, South Zone, East Zone, West Zone).
- **Warehouse:** Target operational distribution node managing the physical inventory payload.
- **Delivery_Time_Days:** Numerical measurement tracking transit delays and durations.
- **Inventory_Cost_INR:** Evaluated financial valuation score representing cargo worth.
- **Delivery_Status:** Categorical classification field tracking if the unit is Delivered, In Transit, or Delayed.

---

## Analytical Dashboard Features

### 1. Multi-Dimensional Interactive Filters
The control panel allows operations managers to filter entire logistics streams dynamically based on specific Geographic Zones or Target Warehouses. Filter changes pass through the WebSocket connection to execute localized SQL backend queries without page reloads.

### 2. High-Level KPI Metric Bars
The upper boundary of the UI displays real-time operational aggregates:
- **Total Managed Shipments:** The active volume count.
- **Average Delivery Duration:** The calculated global delay mean.
- **Total Operational Value:** Cumulative inventory capital tracking.
- **Erratic Anomalies Deflected:** Counter displaying the total number of corrupted negative rows removed to preserve absolute data integrity.

### 3. Distribution Visualization Matrices
- **Warehouse Volume Distribution:** A structural bar chart highlighting throughput variations across regional distribution centers.
- **Transit Latency Projections:** A categorical pie chart separating optimal shipping executions from late distributions to help teams locate network bottlenecks.

### 4. Enterprise Data Grid Export Pipeline
An actionable, real-time filtered shipment grid sits at the bottom of the layout. Managers can interact with the current dataset and click the integrated export function to convert the database response matrix into a CSV file stream, saving an Excel-compatible document locally for multi-department coordination.

---

## Instructions for Local Workstation Deployment

To run this application locally on your machine, perform the following steps inside your terminal:

1. Verify Python installation and add the required platform library links:
   
   pip install streamlit pandas matplotlib

2. Execute the application runtime script file from your terminal directory:

   streamlit run supply_chain_app.py
   
4. Open your browser and navigate to the assigned network interface address:
   
   http://localhost:8501
