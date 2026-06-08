"""
Executive Marketing Dashboard — Streamlit
Board-ready KPI reporting: demand gen, revenue impact, efficiency.
Run: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

st.set_page_config(page_title="Executive Marketing Dashboard", page_icon="📈", layout="wide")


# ─── Data Generation ──────────────────────────────────────────────────────────

@st.cache_data
def generate_monthly_data(months: int = 13) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    base = datetime(2024, 1, 1)
    records = []
    # Simulate growth trend
    for i in range(months):
        dt = base + pd.DateOffset(months=i)
        growth = 1 + i * 0.03 + rng.normal(0, 0.04)
        records.append({
            "month":           dt,
            "month_label":     dt.strftime("%b %Y"),
            # Demand gen
            "mqls":            int(280 * growth + rng.integers(-20, 20)),
            "sqls":            int(105 * growth + rng.integers(-10, 10)),
            "pipeline_sourced":int(420000 * growth + rng.integers(-30000, 30000)),
            # Spend
            "sm_spend":        int(95000 + rng.integers(-5000, 5000)),
            "paid_spend":      int(38000 + rng.integers(-3000, 3000)),
            # Revenue
            "mktg_sourced_rev":int(280000 * growth + rng.integers(-20000, 20000)),
            "mktg_influenced_rev": int(620000 * growth + rng.integers(-40000, 40000)),
            "total_new_rev":   int(950000 * growth + rng.integers(-50000, 50000)),
            # Web
            "sessions":        int(24000 * growth + rng.integers(-1500, 1500)),
            "organic_sessions":int(14000 * growth + rng.integers(-800, 800)),
            # CAC components
            "new_customers":   int(38 * growth + rng.integers(-3, 3)),
        })
    df = pd.DataFrame(records)
    df["mql_to_sql_rate"] = df["sqls"] / df["mqls"]
    df["cost_per_mql"]    = df["sm_spend"] / df["mqls"]
    df["cost_per_sql"]    = df["sm_spend"] / df["sqls"]
    df["cac"]             = df["sm_spend"] / df["new_customers"]
    df["pipeline_per_dollar"] = df["pipeline_sourced"] / df["sm_spend"]
    df["mktg_pct_of_rev"] = df["mktg_sourced_rev"] / df["total_new_rev"]
    df["efficiency_ratio"]= df["mktg_influenced_rev"] / df["sm_spend"]
    return df


df = generate_monthly_data()
current = df.iloc[-1]
prior   = df.iloc[-2]

def delta(curr, prev, pct=True):
    if pct:
        return (curr - prev) / prev if prev != 0 else 0
    return curr - prev


# ─── Header ───────────────────────────────────────────────────────────────────
st.title("📈 Executive Marketing Dashboard")
st.caption(f"Reporting through {current['month_label']} · All figures in USD")

tab_overview, tab_demand, tab_revenue, tab_efficiency, tab_trends = st.tabs([
    "📊 Overview", "🎯 Demand Gen", "💰 Revenue Impact", "⚡ Efficiency", "📅 Trends"
])


# ─── OVERVIEW ─────────────────────────────────────────────────────────────────
with tab_overview:
    st.subheader("Monthly Snapshot")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("MQLs",                f"{current['mqls']:,}",           f"{delta(current['mqls'],prior['mqls']):.1%}")
    c2.metric("SQLs",                f"{current['sqls']:,}",           f"{delta(current['sqls'],prior['sqls']):.1%}")
    c3.metric("Pipeline Sourced",    f"${current['pipeline_sourced']/1e3:.0f}K", f"{delta(current['pipeline_sourced'],prior['pipeline_sourced']):.1%}")
    c4.metric("Mktg-Sourced Rev",    f"${current['mktg_sourced_rev']/1e3:.0f}K", f"{delta(current['mktg_sourced_rev'],prior['mktg_sourced_rev']):.1%}")
    c5.metric("S&M Spend",           f"${current['sm_spend']/1e3:.0f}K", f"{delta(current['sm_spend'],prior['sm_spend']):.1%}")
    c6.metric("New Customers",       f"{current['new_customers']:,}",  f"{delta(current['new_customers'],prior['new_customers']):.1%}")

    st.divider()

    # Sparklines grid
    def sparkline(series, title, fmt="int"):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["month_label"], y=series, mode="lines+markers",
                                  line=dict(color="#4F46E5", width=2),
                                  marker=dict(size=4)))
        fig.update_layout(
            title=title, height=180,
            margin=dict(l=0, r=0, t=30, b=0),
            xaxis=dict(showticklabels=False),
            yaxis=dict(tickformat="$,.0f" if fmt=="dollar" else ".0%" if fmt=="pct" else ","),
        )
        return fig

    r1c1, r1c2, r1c3 = st.columns(3)
    with r1c1: st.plotly_chart(sparkline(df["mqls"], "MQLs"), use_container_width=True)
    with r1c2: st.plotly_chart(sparkline(df["sqls"], "SQLs"), use_container_width=True)
    with r1c3: st.plotly_chart(sparkline(df["mql_to_sql_rate"], "MQL → SQL Rate", "pct"), use_container_width=True)

    r2c1, r2c2, r2c3 = st.columns(3)
    with r2c1: st.plotly_chart(sparkline(df["pipeline_sourced"], "Pipeline Sourced ($)", "dollar"), use_container_width=True)
    with r2c2: st.plotly_chart(sparkline(df["mktg_sourced_rev"], "Mktg-Sourced Revenue ($)", "dollar"), use_container_width=True)
    with r2c3: st.plotly_chart(sparkline(df["cac"], "CAC ($)", "dollar"), use_container_width=True)


# ─── DEMAND GEN ───────────────────────────────────────────────────────────────
with tab_demand:
    st.subheader("Demand Generation Performance")
    col_l, col_r = st.columns(2)

    with col_l:
        fig = go.Figure()
        fig.add_trace(go.Bar(name="MQLs", x=df["month_label"], y=df["mqls"], marker_color="#4F46E5"))
        fig.add_trace(go.Bar(name="SQLs", x=df["month_label"], y=df["sqls"], marker_color="#7C3AED"))
        fig.update_layout(barmode="group", title="MQLs vs SQLs", height=340)
        st.plotly_chart(fig, use_container_width=True)

    with col_r:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df["month_label"], y=df["mql_to_sql_rate"],
                                   mode="lines+markers", line=dict(color="#10B981", width=3)))
        fig2.update_layout(title="MQL → SQL Conversion Rate", yaxis_tickformat=".0%", height=340)
        st.plotly_chart(fig2, use_container_width=True)

    col_l2, col_r2 = st.columns(2)
    with col_l2:
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=df["month_label"], y=df["cost_per_mql"],
                                   mode="lines+markers", line=dict(color="#F59E0B", width=3), name="Cost/MQL"))
        fig3.add_trace(go.Scatter(x=df["month_label"], y=df["cost_per_sql"],
                                   mode="lines+markers", line=dict(color="#EF4444", width=3), name="Cost/SQL"))
        fig3.update_layout(title="Cost per MQL and SQL", yaxis_tickprefix="$", height=340)
        st.plotly_chart(fig3, use_container_width=True)

    with col_r2:
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(x=df["month_label"], y=df["pipeline_sourced"],
                               marker_color="#A855F7", name="Pipeline Sourced"))
        fig4.update_layout(title="Marketing-Sourced Pipeline ($)", yaxis_tickprefix="$", height=340)
        st.plotly_chart(fig4, use_container_width=True)


# ─── REVENUE IMPACT ───────────────────────────────────────────────────────────
with tab_revenue:
    st.subheader("Revenue Impact")

    col_l, col_r = st.columns(2)
    with col_l:
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Mktg Sourced",   x=df["month_label"], y=df["mktg_sourced_rev"],   marker_color="#4F46E5"))
        fig.add_trace(go.Bar(name="Mktg Influenced", x=df["month_label"], y=df["mktg_influenced_rev"], marker_color="#A5B4FC", opacity=0.6))
        fig.update_layout(barmode="overlay", title="Marketing Revenue Contribution ($)", yaxis_tickprefix="$", height=360)
        st.plotly_chart(fig, use_container_width=True)

    with col_r:
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df["month_label"], y=df["mktg_pct_of_rev"],
                                   mode="lines+markers+text",
                                   text=[f"{v:.0%}" for v in df["mktg_pct_of_rev"]],
                                   textposition="top center",
                                   line=dict(color="#10B981", width=3)))
        fig2.add_hline(y=0.35, line_dash="dash", line_color="#999", annotation_text="Target: 35%")
        fig2.update_layout(title="Mktg-Sourced % of New Revenue", yaxis_tickformat=".0%", height=360)
        st.plotly_chart(fig2, use_container_width=True)

    # Rolling 3-month table
    st.subheader("Rolling 3-Month Revenue Summary")
    last3 = df.tail(3)[["month_label", "mktg_sourced_rev", "mktg_influenced_rev",
                         "total_new_rev", "mktg_pct_of_rev", "new_customers"]].copy()
    last3.columns = ["Month", "Sourced ($)", "Influenced ($)", "Total New Rev ($)", "Mktg %", "New Customers"]
    last3["Sourced ($)"]    = last3["Sourced ($)"].apply(lambda x: f"${x:,.0f}")
    last3["Influenced ($)"] = last3["Influenced ($)"].apply(lambda x: f"${x:,.0f}")
    last3["Total New Rev ($)"] = last3["Total New Rev ($)"].apply(lambda x: f"${x:,.0f}")
    last3["Mktg %"]         = last3["Mktg %"].apply(lambda x: f"{x:.1%}")
    st.dataframe(last3, use_container_width=True, hide_index=True)


# ─── EFFICIENCY ───────────────────────────────────────────────────────────────
with tab_efficiency:
    st.subheader("Marketing Efficiency")

    col_l, col_r = st.columns(2)
    with col_l:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["month_label"], y=df["cac"],
                                  mode="lines+markers", line=dict(color="#EF4444", width=3)))
        fig.add_hline(y=2500, line_dash="dash", line_color="#999", annotation_text="Target CAC: $2,500")
        fig.update_layout(title="Blended CAC over Time", yaxis_tickprefix="$", height=340)
        st.plotly_chart(fig, use_container_width=True)

    with col_r:
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=df["month_label"], y=df["efficiency_ratio"],
                               marker_color="#4F46E5"))
        fig2.add_hline(y=5, line_dash="dash", line_color="#999", annotation_text="Target: 5x")
        fig2.update_layout(title="Marketing Efficiency Ratio (Influenced Rev / Spend)", height=340)
        st.plotly_chart(fig2, use_container_width=True)

    col_l2, col_r2 = st.columns(2)
    with col_l2:
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=df["month_label"], y=df["pipeline_per_dollar"],
                               marker_color="#10B981"))
        fig3.update_layout(title="Pipeline Generated per $1 Spent", yaxis_tickprefix="$", height=340)
        st.plotly_chart(fig3, use_container_width=True)

    with col_r2:
        # Web efficiency
        df["organic_pct"] = df["organic_sessions"] / df["sessions"]
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(x=df["month_label"], y=df["organic_pct"],
                                   mode="lines+markers", fill="tozeroy",
                                   line=dict(color="#7C3AED", width=2)))
        fig4.update_layout(title="Organic Traffic Share", yaxis_tickformat=".0%", height=340)
        st.plotly_chart(fig4, use_container_width=True)


# ─── TRENDS ───────────────────────────────────────────────────────────────────
with tab_trends:
    st.subheader("Full KPI History")
    display_cols = ["month_label", "mqls", "sqls", "mql_to_sql_rate", "pipeline_sourced",
                    "mktg_sourced_rev", "sm_spend", "cac", "efficiency_ratio", "new_customers"]
    display = df[display_cols].copy()
    display.columns = ["Month", "MQLs", "SQLs", "MQL→SQL%", "Pipeline ($)",
                       "Mktg Rev ($)", "S&M Spend ($)", "CAC ($)", "Efficiency", "New Custs"]
    for col in ["Pipeline ($)", "Mktg Rev ($)", "S&M Spend ($)", "CAC ($)"]:
        display[col] = display[col].apply(lambda x: f"${x:,.0f}")
    display["MQL→SQL%"]    = display["MQL→SQL%"].apply(lambda x: f"{x:.1%}")
    display["Efficiency"]  = display["Efficiency"].apply(lambda x: f"{x:.1f}x")
    st.dataframe(display.sort_values("Month", ascending=False), use_container_width=True, hide_index=True)
