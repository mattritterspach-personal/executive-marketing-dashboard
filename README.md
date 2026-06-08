# Executive Marketing Dashboard

A board-ready marketing reporting system with a live Streamlit KPI dashboard, Excel OKR tracker, and a marketing operations playbook.

## What's Inside

| File | Description |
|------|-------------|
| `dashboard.py` | Streamlit executive dashboard — all key marketing KPIs |
| `kpi_tracker.xlsx` | Excel OKR + KPI tracker with monthly/quarterly views |
| `docs/marketing_playbook.md` | Marketing ops playbook — frameworks, cadences, definitions |
| `requirements.txt` | Python dependencies |

## Dashboard KPIs

**Demand Generation**
- MQLs, SQLs, pipeline sourced
- Cost per MQL, cost per SQL
- MQL → SQL conversion rate

**Revenue Impact**
- Marketing-sourced pipeline ($ and % of total)
- Marketing-influenced revenue
- Channel ROI

**Brand & Awareness**
- Website sessions, organic traffic, branded search volume
- Share of voice (estimated)

**Efficiency**
- CAC by channel
- Marketing efficiency ratio (revenue influenced / S&M spend)
- Payback period

## Quick Start

```bash
pip install -r requirements.txt
streamlit run dashboard.py
```

## Excel OKR Tracker Tabs

1. **Annual OKRs** — Objectives and Key Results with target / actual / % complete
2. **Monthly KPIs** — Rolling 12-month KPI tracking table
3. **Channel Scorecard** — Per-channel performance vs targets
4. **Board Report** — One-page summary for board / exec presentations

## License

MIT
