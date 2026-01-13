import pandas as pd
import numpy as np

# Create function to calculate key performance indicators (KPIs)
def calculate_kpis(df):
    kpis = {
        'total_revenue': df['Revenue'].sum() if 'Revenue' in df.columns else 0,
        'total_profit': df['Profit'].sum() if 'Profit' in df.columns else 0,
        'total_orders': len(df),
        'total_units_sold': df['Units_Sold'].sum() if 'Units_Sold' in df.columns else 0,
        'average_order_value': df['Revenue'].mean() if 'Revenue' in df.columns else 0,
        'unique_customers': df['Customer_ID'].nunique() if 'Customer_ID' in df.columns else 0
    }
    return kpis
