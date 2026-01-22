# Sales Analytics Dashboard

## Overview

The **Sales Analytics Dashboard** is an interactive data analytics application built with **Streamlit, Pandas, and Plotly**.
It allows users to upload raw sales data or load a sample dataset and instantly generate key business insights through KPIs, visualizations, and filtering tools — all without writing any code.

This project focuses on **turning raw transactional sales data into actionable business intelligence**, similar to tools used in real-world sales, finance, and analytics teams.

---

## Current Features

### Data Input

* Upload custom sales data via CSV
* Load a built-in sample dataset for demonstration
* Automatic validation of required columns

### Required Columns

The uploaded dataset must include the following columns:

* `Revenue`
* `Profit`
* `Units_Sold`
* `Customer_ID`
* `Category`
* `Region`

Optional:

* `Date` (enables time-based analysis)

---

### Key Performance Indicators (KPIs)

Automatically calculates and displays:

* Total Revenue
* Total Profit
* Average Order Value
* Total Orders
* Total Units Sold
* Unique Customers

KPIs dynamically update based on applied filters.

---

### Interactive Filters

* Date range filtering (if Date column is present)
* Reset date filters to original dataset
* Sidebar-based filtering for clean UI separation

---

### Visualizations

* **Revenue by Region** (Pie Chart)
* **Revenue by Category** (Bar Chart)
* **Revenue Over Time** (Daily Line Chart with markers)

All charts are interactive and resize dynamically.

---

### Data Exploration

* Preview first 8 rows of filtered data
* View descriptive statistics for numeric columns
* Expandable sections to reduce visual clutter

---

## Project Structure

```
streamlit_sales_analytics_dashboard/
│
├── app.py                      # Main Streamlit application
├── utils/
│   ├── analytics.py            # KPI and aggregation logic
│   └── data_processing.py      # Data loading and preprocessing
├── data/
│   └── sample_sales_data.csv   # Sample dataset
├── requirements.txt
└── README.md
```

---

## How to Run the App

1. **Clone the repository**

   ```
   git clone https://github.com/ChimoMallous/streamlit_sales_analytics_dashboard.git
   cd streamlit_sales_analytics_dashboard
   ```

2. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```
   streamlit run app.py
   ```

The app will automatically open in your default browser.

---

## Notes

* Requires **Python 3.9+**
* Designed to handle clean, structured CSV files
* Missing required columns will trigger validation errors
* Date filtering is optional but recommended for full functionality

---

## Planned Features

* Additional filters (Category, Region)
* Profit margin analysis
* Export filtered data
* Monthly and quarterly aggregation views
* Improved UI styling and layout
* Accounting-focused extensions (trial balance, income statement integration)

---

## About

This project demonstrates practical skills in:

* Business analytics
* Dashboard design
* Python-based data visualization
* Streamlit application development

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly

---

