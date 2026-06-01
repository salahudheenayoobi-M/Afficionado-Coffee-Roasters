import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Afficionado Coffee Analytics", layout="wide")

# --- Title ---
st.title("☕ Afficionado Coffee Roasters")
st.subheader("Product Optimization & Revenue Analysis")

# --- Load Data ---
df = pd.read_csv("Afficionado Coffee Roasters.csv")
df['revenue'] = df['transaction_qty'] * df['unit_price']

# --- Sidebar Filters ---
st.sidebar.title("🔍 Filters")

category = st.sidebar.multiselect(
    "Select Category",
    options=df['product_category'].unique(),
    default=df['product_category'].unique()
)

location = st.sidebar.multiselect(
    "Select Store Location",
    options=df['store_location'].unique(),
    default=df['store_location'].unique()
)

top_n = st.sidebar.slider("Top N Products", 5, 20, 10)

# --- Apply Filters ---
filtered = df[df['product_category'].isin(category) &
              df['store_location'].isin(location)]

# --- KPI Cards ---
st.markdown("## 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered['revenue'].sum():,.0f}")
col2.metric("Total Units Sold", f"{filtered['transaction_qty'].sum():,}")
col3.metric("Unique Products", filtered['product_id'].nunique())
col4.metric("Total Transactions", f"{filtered['transaction_id'].nunique():,}")

st.markdown("---")

# --- Aggregations ---
popularity = filtered.groupby('product_detail')['transaction_qty'].sum().reset_index()
popularity = popularity.sort_values('transaction_qty', ascending=False).reset_index(drop=True)

revenue_by_product = filtered.groupby('product_detail')['revenue'].sum().reset_index()
revenue_by_product = revenue_by_product.sort_values('revenue', ascending=False).reset_index(drop=True)
revenue_by_product['revenue_share_%'] = (revenue_by_product['revenue'] / revenue_by_product['revenue'].sum()) * 100
revenue_by_product['cumulative_revenue_share%'] = (revenue_by_product['revenue'].cumsum() / revenue_by_product['revenue'].sum()) * 100

category_revenue = filtered.groupby('product_category')['revenue'].sum().reset_index()
category_revenue = category_revenue.sort_values('revenue', ascending=False).reset_index(drop=True)

type_revenue = filtered.groupby(['product_category', 'product_type'])['revenue'].sum().reset_index()
type_revenue = type_revenue.sort_values('revenue', ascending=False).reset_index(drop=True)

product_matrix = pd.merge(popularity, revenue_by_product[['product_detail', 'revenue']], on='product_detail')
qty_median = product_matrix['transaction_qty'].median()
rev_median = product_matrix['revenue'].median()
product_matrix['Quadrant'] = 'Dead Weight'
product_matrix.loc[(product_matrix['transaction_qty'] > qty_median) & (product_matrix['revenue'] > rev_median), 'Quadrant'] = 'Hero ⭐'
product_matrix.loc[(product_matrix['transaction_qty'] < qty_median) & (product_matrix['revenue'] > rev_median), 'Quadrant'] = 'Hidden Gem 💎'
product_matrix.loc[(product_matrix['transaction_qty'] > qty_median) & (product_matrix['revenue'] < rev_median), 'Quadrant'] = 'High Vol Low Rev ⚠️'

# --- Chart 1 & 2 side by side ---
st.markdown("## 🏆 Product Rankings")
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(popularity.head(top_n),
                  x='transaction_qty',
                  y='product_detail',
                  orientation='h',
                  title=f'Top {top_n} Products by Units Sold')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(revenue_by_product.head(top_n),
                  x='revenue',
                  y='product_detail',
                  orientation='h',
                  title=f'Top {top_n} Products by Revenue')
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# --- Chart 3 & 4 side by side ---
st.markdown("## 📦 Category Analysis")
col1, col2 = st.columns(2)

with col1:
    fig3 = px.pie(category_revenue,
                  names='product_category',
                  values='revenue',
                  title='Revenue Share by Category')
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    fig4 = px.bar(type_revenue.head(15),
                  x='revenue',
                  y='product_type',
                  orientation='h',
                  color='product_category',
                  title='Top 15 Product Types by Revenue')
    st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# --- Chart 5 Pareto ---
st.markdown("## 📈 Pareto Analysis")
fig5 = px.line(revenue_by_product.sort_values('cumulative_revenue_share%'),
               x='product_detail',
               y='cumulative_revenue_share%',
               title='Pareto Analysis - Cumulative Revenue %')
fig5.add_hline(y=80, line_dash='dash', line_color='red', annotation_text='80% threshold')
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# --- Chart 6 Scatter ---
st.markdown("## 🎯 Popularity vs Revenue Matrix")
fig6 = px.scatter(product_matrix,
                  x='transaction_qty',
                  y='revenue',
                  color='Quadrant',
                  hover_name='product_detail',
                  title='Popularity vs Revenue - Product Matrix')
st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# --- Raw Data Table ---
st.markdown("## 🗃️ Product Performance Table")
st.dataframe(revenue_by_product, use_container_width=True)