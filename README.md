# ☕ Afficionado Coffee Roasters — Product Optimization & Revenue Analysis

An end-to-end **data analytics project** that explores transactional sales data from Afficionado Coffee Roasters to uncover product performance insights, revenue drivers, and optimization opportunities.

The project includes a **Jupyter Notebook** for exploratory data analysis and a **Streamlit dashboard** for interactive visualization.

---

## 📸 Dashboard Preview

> Run the app locally to explore the interactive dashboard with filters, KPIs, and charts.

---

## 🔍 Project Overview

| Aspect | Details |
|---|---|
| **Dataset** | `Afficionado Coffee Roasters.csv` (~13 MB, transactional sales data) |
| **Notebook** | `Afficionado Coffee Roasters.ipynb` — EDA, data validation & static visualizations |
| **Dashboard** | `app.py` — Interactive Streamlit app with Plotly charts |
| **Key Focus** | Product optimization, revenue contribution analysis, Pareto insights |

---

## 🧰 Tech Stack

- **Python 3.10+**
- **Pandas** & **NumPy** — Data wrangling & aggregation
- **Matplotlib** & **Seaborn** — Static visualizations (notebook)
- **Plotly Express** — Interactive charts (dashboard)
- **Streamlit** — Web-based dashboard framework

---

## 📊 Key Analyses

1. **Top Products by Units Sold & Revenue** — Identifies best-selling and highest-revenue products
2. **Revenue Share by Category** — Pie chart breakdown of category-level contributions
3. **Product Type Ranking** — Top 15 product types by revenue, color-coded by category
4. **Pareto Analysis** — Cumulative revenue curve with 80% threshold line to identify vital few products
5. **Popularity vs Revenue Matrix** — Scatter-based quadrant classification:
   - ⭐ **Hero** — High volume, high revenue
   - 💎 **Hidden Gem** — Low volume, high revenue
   - ⚠️ **High Vol Low Rev** — High volume, low revenue
   - 🪨 **Dead Weight** — Low volume, low revenue

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/afficionado-coffee-roasters.git
   cd afficionado-coffee-roasters
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit dashboard**
   ```bash
   streamlit run app.py
   ```
   The app will open in your browser at `http://localhost:8501`.

4. **Explore the notebook**
   ```bash
   jupyter notebook "Afficionado Coffee Roasters.ipynb"
   ```

---

## 📁 Project Structure

```
afficionado-coffee-roasters/
├── Afficionado Coffee Roasters.csv      # Raw transactional dataset
├── Afficionado Coffee Roasters.ipynb    # EDA & analysis notebook
├── app.py                               # Streamlit dashboard
├── requirements.txt                     # Python dependencies
├── .gitignore                           # Git ignore rules
└── README.md                            # Project documentation
```

---

## 🔧 Dashboard Features

- **Sidebar Filters** — Filter by product category, store location, and top-N products
- **KPI Cards** — Total revenue, units sold, unique products, total transactions
- **Interactive Charts** — Hover, zoom, and pan on all Plotly visualizations
- **Responsive Layout** — Wide-mode layout optimized for desktop viewing

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 👤 Author

**Salah**

---

> Built with ❤️ and ☕
