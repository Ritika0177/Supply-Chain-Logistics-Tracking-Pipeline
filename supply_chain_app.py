import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt

# 1. Page Configuration Set Up
st.set_page_config(page_title="Supply Chain Logistics Optimizing Dashboard", layout="wide")

st.title("Supply Chain Logistics & Inventory Optimization Tracking Pipeline")
st.markdown("An enterprise operational data pipeline engineered to analyze warehouse delivery parameters, drop anomalies, and optimize logistics performance queues.")

# 2. Synthetic Corporate Supply Chain Data Generation
@st.cache_data
def generate_supply_chain_data():
    np.random.seed(42)
    regions = ['North Zone', 'South Zone', 'East Zone', 'West Zone']
    warehouses = ['WH-Alpha', 'WH-Beta', 'WH-Gamma', 'WH-Delta']
    status = ['Delivered', 'In Transit', 'Delayed']
    
    data = {
        'Order_ID': [f"ORD{1000+i}" for i in range(100)],
        'Region': np.random.choice(regions, 100),
        'Warehouse': np.random.choice(warehouses, 100),
        'Delivery_Time_Days': np.random.randint(1, 15, 100),
        'Inventory_Cost_INR': np.random.randint(5000, 50000, 100).astype(float),
        'Delivery_Status': np.random.choice(status, 100, p=[0.7, 0.2, 0.1])
    }
    
    df = pd.DataFrame(data)
    
    # Intentionally introducing anomalies (negative values) to show pipeline data cleaning capabilities
    df.loc[15, 'Inventory_Cost_INR'] = -15000.0
    df.loc[42, 'Inventory_Cost_INR'] = -8000.0
    df.loc[73, 'Inventory_Cost_INR'] = -22000.0
    return df

raw_data = generate_supply_chain_data()

# 3. Backend Database Processing (In-Memory SQLite Configuration)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Creating the Relational Data Schema Layout
cursor.execute('''
    CREATE TABLE IF NOT EXISTS logistics_pipeline (
        Order_ID TEXT,
        Region TEXT,
        Warehouse TEXT,
        Delivery_Time_Days INTEGER,
        Inventory_Cost_INR REAL,
        Delivery_Status TEXT
    )
''')

# Intercepting and Dropping Erratic Metrics (Cleaning Negative Values) before SQL injection
cleaned_df = raw_data[raw_data['Inventory_Cost_INR'] >= 0]
cleaned_df.to_sql('logistics_pipeline', conn, if_exists='replace', index=False)

# 4. Front-End Interface Filters Layout
st.sidebar.header("Operational Control Filters")
selected_region = st.sidebar.selectbox("Select Geographic Operating Zone:", ['All Zones'] + list(cleaned_df['Region'].unique()))
selected_wh = st.sidebar.selectbox("Select Target Warehouse Node:", ['All Warehouses'] + list(cleaned_df['Warehouse'].unique()))

# Formulating Dynamic SQL Query Base depending on selections
query = "SELECT * FROM logistics_pipeline WHERE 1=1"
if selected_region != 'All Zones':
    query += f" AND Region = '{selected_region}'"
if selected_wh != 'All Warehouses':
    query += f" AND Warehouse = '{selected_wh}'"

# Fetching real-time filtered results back into Pandas
filtered_df = pd.read_sql_query(query, conn)

# 5. High-Level Performance Counter Cards Layout
st.markdown("### Enterprise Key Performance Indicators (KPIs)")
col1, col2, col3, col4 = st.columns(4)

total_orders = len(filtered_df)
avg_delivery = round(filtered_df['Delivery_Time_Days'].mean(), 1) if total_orders > 0 else 0
total_valuation = round(filtered_df['Inventory_Cost_INR'].sum(), 2) if total_orders > 0 else 0
anomalies_blocked = len(raw_data) - len(cleaned_df)

col1.metric("Total Managed Shipments", f"{total_orders} Units")
col2.metric("Avg Delivery Duration", f"{avg_delivery} Days")
col3.metric("Total Operational Value", f"₹{total_valuation:,}")
col4.metric("Erratic Anomalies Deflected", f"{anomalies_blocked} Blocks", delta="-3 Negative Rows", delta_color="inverse")

# 6. Analytics Visualizations Section
st.markdown("---")
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("#### Warehouse Delivery Volume Split")
    if total_orders > 0:
        wh_counts = filtered_df['Warehouse'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        wh_counts.plot(kind='bar', color='#1f77b4', ax=ax)
        ax.set_ylabel("Number of Orders")
        ax.set_xlabel("Warehouse Node")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("No logs found for current configuration.")

with right_col:
    st.markdown("#### Transit Latency Projections")
    if total_orders > 0:
        status_counts = filtered_df['Delivery_Status'].value_counts()
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', colors=['#2ca02c', '#ff7f0e', '#d62728'], startangle=90)
        st.pyplot(fig)
    else:
        st.info("No logs found for current configuration.")

# 7. Actionable Data Grid Layer & Optimization Export Mechanism
st.markdown("---")
st.markdown("### Active Geographic Shipment Log Grid")
st.dataframe(filtered_df, use_container_width=True)

# Dynamic Data Byte-Stream Extraction Pipeline
csv_bytes = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Export Filtered Logistics Data to Excel/CSV",
    data=csv_bytes,
    file_name="Optimized_Logistics_Pipeline.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Supply Chain Optimization Engine • Cleaned Data Repository Deployment Configuration Layer.")
