import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.analytics import calculate_kpis, revenue_by_region, revenue_by_category
from utils.data_processing import load_sample_data

# Set page configuration
st.set_page_config(page_title="Sales_Analytics_Dashboard", layout="wide")
st.title("Sales Analytics Dashboard")
df = pd.DataFrame()

# Add button to load sample data
if st.button("Load Sample Data"):
    with st.spinner("Loading sample data..."):
        df = load_sample_data()
        st.caption(f"Loaded {len(df)} records")

# Main dashboard, only show if data is loaded
if not df.empty:
    
    # Display KPIs in a bordered container
    with st.container(border=True):
        st.subheader("Key Performance Indicators (KPIs)")
        kpis = calculate_kpis(df)
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        kpi_col1.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}")
        kpi_col2.metric("Total Profit", f"${kpis['total_profit']:,.0f}")
        kpi_col3.metric("Average Order Value", f"${kpis['average_order_value']:,.0f}")
        kpi_col1.metric("Total Orders", f"{kpis['total_orders']:,}")    
        kpi_col2.metric("Total Units Sold", f"{kpis['total_units_sold']:,}")
        kpi_col3.metric("Unique Customers", f"{kpis['unique_customers']:,}")
    
    # Display revenue by category and region side by side
    rev_col1, rev_col2 = st.columns(2)
    with rev_col1:
        with st.container(border=True):
            st.subheader("Revenue by Region")
            region_data = revenue_by_region(df)
            fig = px.pie(region_data, names='Region', values='Revenue', title='Revenue by Region', color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(fig, use_container_width=True)
    with rev_col2:
        with st.container(border=True):
            st.subheader("Revenue by Category")
            category_data = revenue_by_category(df)
            fig = px.bar(category_data, x='Category', y='Revenue', title='Revenue by Category', color='Revenue', color_continuous_scale=px.colors.sequential.Blues_r)
            st.plotly_chart(fig, use_container_width=True)
    
    # Display data head and summary statistics side by side
    with st.container(border=True):
        st.subheader("Sales Data Overview")
        preview_col1, preview_col2 = st.columns(2)
        with preview_col1:
            with st.expander("View Data Head (8 rows)"):
                st.dataframe(df.head(8))
        with preview_col2:
            with st.expander("View Summary Statistics"):
                st.dataframe(df.describe())