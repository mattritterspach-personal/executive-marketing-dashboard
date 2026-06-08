# Marketing Operations Playbook

A practical framework for running a data-driven marketing function. Covers cadences, metric definitions, reporting workflows, and campaign governance.

---

## 1. Core Metric Definitions

### Demand Generation

| Metric | Definition | Owner |
|--------|-----------|-------|
| **MQL** | Marketing Qualified Lead — meets ICP criteria (firmographic score ≥ 65) AND has completed a qualifying action (demo request, trial signup, content download + site visit) | Marketing |
| **SQL** | Sales Accepted Lead — MQL reviewed and accepted by an AE within 5 business days | Sales |
| **SAO** | Sales Accepted Opportunity — SQL with a discovery call completed and deal created in CRM | Sales |
| **MQL → SQL Rate** | SQLs / MQLs in the same cohort period | Marketing |
| **SQL → SAO Rate** | SAOs / SQLs | Sales |
| **Pipeline Sourced** | Gross pipeline value of deals where marketing was the first touch | Marketing |
| **Pipeline Influenced** | Gross pipeline value of deals with ≥1 marketing touch at any stage | Marketing |

### Revenue

| Metric | Definition |
|--------|-----------|
| **Mktg-Sourced Revenue** | Closed-Won revenue where marketing was the first touch |
| **Mktg-Influenced Revenue** | Closed-Won revenue with ≥1 marketing touch in the journey |
| **Marketing % of Pipeline** | Mktg-sourced pipeline / total pipeline created in period |

### Efficiency

| Metric | Formula | Target |
|--------|---------|--------|
| **CAC (Blended)** | Total S&M spend / New customers | < $2,500 |
| **Cost per MQL** | S&M spend / MQLs | Varies by channel |
| **Cost per SQL** | S&M spend / SQLs | < $800 |
| **Marketing Efficiency Ratio** | Mktg-influenced revenue / S&M spend | > 5× |
| **Pipeline per Dollar** | Mktg-sourced pipeline / S&M spend | > $4 |

---

## 2. Reporting Cadences

### Weekly (Monday AM)
- **Audience:** Marketing team
- **Contents:**
  - MQL volume vs. weekly target
  - Pipeline sourced week-over-week
  - Top 3 campaigns by MQL volume
  - Any anomalies (e.g., paid spend spike, conversion rate drop)
- **Format:** Slack summary + dashboard link
- **Owner:** Demand Gen Manager

### Monthly (First week of month)
- **Audience:** Marketing leadership + Sales leadership
- **Contents:**
  - Full KPI scorecard vs. targets
  - Funnel waterfall (MQL → SQL → SAO → Closed Won)
  - Channel performance summary
  - CAC and pipeline efficiency trends
  - Next month priorities
- **Format:** Dashboard + 1-page PDF export
- **Owner:** VP Marketing

### Quarterly (Board / Exec)
- **Audience:** Board, CEO, CFO
- **Contents:**
  - OKR progress (% complete vs. Q target)
  - Revenue contribution (sourced + influenced)
  - CAC trend and LTV:CAC
  - Competitive positioning / brand metrics
  - Next quarter plan and budget
- **Format:** Slide deck (5–7 slides)
- **Owner:** CMO

---

## 3. OKR Framework

### Structure

```
Objective (qualitative, inspiring)
└── Key Result 1 (quantitative, measurable)
└── Key Result 2
└── Key Result 3
```

### Example: Q1 Demand Generation OKR

**Objective:** Accelerate top-of-funnel pipeline to fuel Q2 revenue growth

- **KR1:** Generate 900 MQLs (300/month), up from 750 last quarter
- **KR2:** Improve MQL → SQL rate from 36% to 42%
- **KR3:** Source $3.2M in marketing-attributed pipeline

### Scoring

| Score | Description |
|-------|-------------|
| 1.0 | Fully achieved (stretch) |
| 0.7 | Mostly achieved (expected) |
| 0.4 | Partially achieved |
| 0.0 | Not achieved |

**Target:** Average OKR score of 0.7 (ambitious but achievable). Consistently hitting 1.0 means targets are too easy.

---

## 4. Campaign Governance

### Campaign Naming Convention

```
[REGION]-[TEAM]-[CHANNEL]-[QUARTER]-[DESCRIPTOR]
```

Examples:
- `US-DEMAND-PAID-Q1-GOOGLE-BRAND`
- `US-CONTENT-SEO-Q2-INTEGRATION-GUIDES`
- `EMEA-ABM-EMAIL-Q3-ENT-NURTURE`

### Campaign Launch Checklist

- [ ] ICP and target persona defined
- [ ] Message-market fit validated (1-pager or brief)
- [ ] UTM parameters configured
- [ ] CRM campaign created and linked
- [ ] Attribution touchpoints mapped
- [ ] Budget approved and tracked in spend tracker
- [ ] Success metrics and targets set (MQLs, pipeline, revenue)
- [ ] Landing page / asset QA'd
- [ ] Legal review complete (if required)
- [ ] Launch date communicated to sales

### Campaign Review (Bi-weekly)

Review all active campaigns against targets:
1. Spend vs. budget (over/under)
2. Performance vs. MQL and pipeline targets
3. Decision: scale / maintain / pause / kill

---

## 5. Channel Strategy Framework

### Channel Prioritization Matrix

Score each channel on:
- **Volume:** Can it generate enough MQLs at scale?
- **Quality:** How well does it convert to revenue?
- **Efficiency:** What's the cost per MQL / pipeline per dollar?
- **Scalability:** Can spend be increased without diminishing returns?

Tier 1 (invest): Score ≥ 16  
Tier 2 (maintain): Score 10–15  
Tier 3 (test/pause): Score < 10

### Budget Allocation Rule of Thumb

- **70%** to proven, high-ROI channels (Tier 1)
- **20%** to channels with growth potential (Tier 2)
- **10%** to experimental channels and new tests

---

## 6. Data & Attribution Governance

### UTM Parameter Standard

| Parameter | Required | Values |
|-----------|----------|--------|
| `utm_source` | Yes | google, linkedin, email, referral, etc. |
| `utm_medium` | Yes | cpc, organic, email, social, event |
| `utm_campaign` | Yes | Use campaign naming convention above |
| `utm_content` | Recommended | Ad variant or asset name |
| `utm_term` | Paid Search only | Keyword |

### Attribution Model Selection Guide

| Scenario | Recommended Model |
|----------|------------------|
| Short sales cycle (< 30 days) | Last Touch |
| Long sales cycle, brand-heavy | First Touch + U-Shaped |
| Even multi-touch journey | Linear |
| Recency-weighted | Time Decay |
| Full-funnel B2B | W-Shaped |
| High accuracy required | Shapley Value |

### Data Quality Checklist (Monthly)

- [ ] MQL definition applied consistently in CRM
- [ ] All campaigns have UTM tags
- [ ] Duplicate leads de-duped
- [ ] Touchpoint data complete (no orphaned touches)
- [ ] Revenue attribution reconciled with Finance
- [ ] CAC reconciled: S&M headcount costs included

---

## 7. Sales + Marketing Alignment

### SLA: Marketing → Sales

| Event | SLA |
|-------|-----|
| MQL created | AE reviews within **2 business days** |
| AE accepts → SQL | AE creates opportunity within **3 business days** |
| AE declines MQL | AE documents reason within **2 business days** |

### Joint Planning (Quarterly)

1. Marketing presents upcoming quarter demand gen plan
2. Sales presents territory and pipeline gaps
3. Agree on MQL volume targets by segment/region
4. Agree on content and enablement priorities
5. Set joint OKRs (1–2 shared KRs between teams)

### Closed-Loop Feedback

Marketing reviews declined MQLs weekly with Sales:
- What % were declined for quality reasons?
- What % were declined for capacity reasons?
- What ICP adjustments are needed?

---

*Last updated: 2024 · Owner: Marketing Operations*
