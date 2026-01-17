import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.analytics import calculate_kpis, revenue_by_region, revenue_by_category, revenue_by_day, convert_date
from utils.data_processing import load_sample_data

# Set page configuration
st.set_page_config(page_title="Sales_Analytics_Dashboard", layout="wide")
st.title("Sales Analytics Dashboard")

# Initialize session state for data storage
if 'df_original' not in st.session_state:
    st.session_state.df_original = pd.DataFrame()

# Required columns
REQUIRED_COLUMNS = ['Revenue', 'Profit', 'Units_Sold', 'Customer_ID', 'Category', 'Region']

# Add File uploader to load user data
uploaded_file = st.file_uploader("Upload your sales data CSV file (required columns: Revenue, Profit, Units_Sold, Customer_ID, Category, Region)", type=["csv"])
if uploaded_file is not None:
    with st.spinner("Loading data..."):
        st.session_state.df_original = pd.read_csv(uploaded_file)
        st.caption(f"Loaded {len(st.session_state.df_original)} records")

# Add button to load sample data
if st.button("Load Sample Data"):
    with st.spinner("Loading sample data..."):
        st.session_state.df_original = load_sample_data()
        st.caption(f"Loaded {len(st.session_state.df_original)} records")

# MAIN DASHBOARD: Only display IF data is loaded
if not st.session_state.df_original.empty:

    # Start with original data
    df = st.session_state.df_original.copy()

    # Check for required columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        st.error(f"The following required columns are missing from the data: {', '.join(missing_cols)}")
        st.stop()

    # Convert date if exists
    df = convert_date(df)

    # Filters in sidebar
    with st.sidebar:
        st.header("Filters")

        # Date range filter
        if 'Date' in df.columns:
            min_Date = df['Date'].min()
            max_Date= df['Date'].max()
            date_range = st.date_input("Select Date Range", [min_Date, max_Date], min_value=min_Date, max_value=max_Date)
            if len(date_range) == 2:
                df = df[(df['Date'] >= pd.to_datetime(date_range[0])) & (df['Date'] <= pd.to_datetime(date_range[1]))]
            # Add button to reset date range filter
            if st.button("Reset Date Filter"):
                df = st.session_state.df_original.copy()
                df = convert_date(df)
                
                
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

    # Display revenue over time by day with monthly ticks
    with st.container(border=True):
        st.subheader("Revenue Over Time")
        daily_revenue = revenue_by_day(df)


        fig = px.line(daily_revenue, x='Date', y='Revenue', title='Revenue by Day', markers=True)
        fig.update_xaxes(tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

    # Display data head and summary statistics side by side
    with st.container(border=True):
        st.subheader("Sales Data Overview")
        preview_col1, preview_col2 = st.columns(2)
        with preview_col1:
            with st.expander("View Data Header"):
                st.dataframe(df.head(8))
        with preview_col2:
            with st.expander("View Summary Statistics"):
                st.dataframe(df.describe())