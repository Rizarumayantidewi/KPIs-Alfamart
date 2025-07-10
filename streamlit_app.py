import altair as alt
import pandas as pd
import streamlit as st

# Set halaman
st.set_page_config(page_title="Alfamart BI Dashboard", page_icon="📊")
st.title("📊 Alfamart Business Intelligence Dashboard (2021–2024)")
st.markdown("By: **Riza Rumayanti Dewi** | NIM: 20240130015 | MI24M")
st.markdown("---")

# Data lengkap dari laporan tahunan
data = {
    "KPI": [
        "Total Revenue", "Net Profit", "Gross Profit / Margin", "Operating Margin", "Total Expenses",
        "Debt-to-Equity Ratio", "YoY Growth Rate", "Return on Investment (ROI)", "Current Ratio", "Quick Ratio",
        "PDACL", "OCFCL", "CBTL", "Total Liabilities to Tangible Assets (TLTAI)", "Interest Cover Ratio (ICR)",
        "Net Debt to Equity Ratio", "Equity Multiplier", "Earnings per Share (EPS)", "Net Profit Margin",
        "Return on Assets (ROA)", "Return on Equity (ROE)", "Price to Earnings Ratio (PE)", "PEG Ratio",
        "Dividend Yield", "Inventory Turnover", "Fixed Asset Turnover", "Total Asset Turnover",
        "Day’s Sales in Inventory", "Receivables Turnover", "Day’s Sales in Receivable",
        "Average Accounts Receivable"
    ],
    "2021": [
        84904301, 1988750, 17681005, 3.31, 83055990,
        2.06, 11.00, 7.22, 0.87, 0.33,
        36, 39, 18, 67, 8.73,
        1.69, 3.06, 0.0479, 2.34,
        7.22, 22.09, 20917.66, 2091.77,
        0.1878, 8.20, 13.53, 3.09,
        44.51, 48.39, 7.55,
        1753651
    ],
    "2022": [
        96924686, 2907478, 20022444, 3.89, 94126025,
        1.68, 14.88, 9.46, 0.90, 4.42,
        29, 41, 20, 63, 20.56,
        1.35, 2.68, 0.0699, 3.00,
        9.46, 25.38, 14287.01, 1428.70,
        0.02406, 8.60, 14.19, 3.15,
        42.44, 49.39, 7.39,
        1960311
    ],
    "2023": [
        106944683, 3484025, 23066117, 4.14, 103658852,
        1.18, 10.43, 10.18, 1.00, 0.42,
        43, 39, 22, 54.16, 27.24,
        0.92, 2.18, 0.08197, 3.26,
        10.18, 22.19, 12199.59, 1219.96,
        0.02868, 8.30, 13.20, 3.12,
        43.90, 45.20, 7.39,
        2365531
    ],
    "2024": [
        118227031, 3220083, 25365481, 3.45, 115245135,
        1.19, 10.55, 8.29, 1.04, 0.44,
        42, 11, 23, 54.38, 31.91,
        0.92, 2.19, 0.0776, 2.72,
        8.29, 18.21, 12903.23, 1290.32,
        0.02868, 8.49, 13.77, 3.05,
        43.00, 42.49, 8.59,
        2782399
    ]
}

# Convert ke DataFrame panjang
df = pd.DataFrame(data)
df_long = df.melt(id_vars="KPI", var_name="Year", value_name="Value")

# Pilih KPI dan Tahun
kpi_selected = st.multiselect("Pilih KPI", options=df["KPI"].tolist(), default=["Total Revenue", "Net Profit"])
years = st.slider("Pilih rentang tahun", 2021, 2024, (2021, 2024))
years_selected = list(map(str, range(years[0], years[1]+1)))

# Filter berdasarkan pilihan
df_filtered = df_long[df_long["KPI"].isin(kpi_selected) & df_long["Year"].isin(years_selected)]

# Tabel Data
st.dataframe(df_filtered.pivot(index="Year", columns="KPI", values="Value"), use_container_width=True)

# Grafik Altair
chart = (
    alt.Chart(df_filtered)
    .mark_line(point=True)
    .encode(
        x=alt.X("Year:N", title="Tahun"),
        y=alt.Y("Value:Q", title="Nilai KPI"),
        color="KPI:N"
    )
    .properties(height=400, title="Tren KPI Alfamart (2021–2024)")
)

st.altair_chart(chart, use_container_width=True)

# Footer
st.markdown("---")
st.caption("📊 Data dari Annual Report Alfamart 2021–2024 – Disusun oleh Riza Rumayanti Dewi")
