# Financial Model — Fit Check
**BUS 395: Venture Creation with AI | Jane Dias | June 2026**

Full Excel model: `financial-model corrected.xlsx`

---

## Revenue Model

**Structure:** Free trial → monthly subscription
**Price:** $12/month (raised from $9 based on Van Westendorp data — June 2026)
**Free tier:** 8 full sessions, full functionality, no credit card required
**Paid tier:** $12/month to continue profile and unlimited sessions
**Ads:** None at any tier

**Why no ads:** Ad revenue creates a conflict between ads non-intrusive enough not to undermine trust and ads annoying enough to drive subscription upgrades. These cannot be optimized simultaneously at early stage.

---

## Unit Economics

### Per-Subscriber Revenue
| Item | Amount |
|---|---|
| Gross monthly revenue | $12.00 |
| Stripe fees (~2.9% + $0.30) | −$0.65 |
| Tax / refund buffer (~5%) | −$0.60 |
| **Net revenue per subscriber** | **~$11.35** |

### Variable Costs Per Subscriber
| Item | Amount |
|---|---|
| LLM API (Claude, active subscriber) | ~$3.50/mo |
| Infrastructure (CDN, storage, allocated) | ~$0.80/mo |
| Payment processing (included above) | — |
| **Variable cost per subscriber** | **~$4.30/mo** |

### Contribution Margin
**Net revenue − variable cost = ~$7.05/month per paying subscriber**

---

## Fixed Costs (Monthly)

| Category | Cost |
|---|---|
| Product labor (founder time @ market rate) | $585 |
| Content creation — TikTok/Instagram (30 hrs @ $15/hr) | $450 |
| Infrastructure base (hosting, database, API minimums) | $200 |
| Tools and services (analytics, email, misc.) | $143 |
| **Total fixed costs** | **$1,378/month** |

---

## Breakeven Analysis

**Formula:** Fixed costs ÷ contribution margin per subscriber

### At $12/month price
- Contribution margin: ~$7.05/subscriber/month
- **Breakeven: ~196 paying subscribers**

### Sensitivity Table

| Conversion Rate | Churn Rate | Breakeven Subscribers |
|---|---|---|
| 10% | 16.7% | ~196 |
| 20% | 10% | ~183 |
| 5% | 25% | Structurally negative |

**The model only works if conversion stays above 10% and churn stays below 20%. Both are assumptions until concierge test data exists.**

---

## Trial-to-Paid Conversion Assumptions

| Stage | Assumption | Basis |
|---|---|---|
| Free sessions used | 8 per trial | Product design |
| Conversion rate | 10–20% | SaaS consumer benchmarks; unvalidated |
| Time to conversion | ~3–6 weeks | Estimated from session frequency |
| LLM cost during trial | ~$1.20 per trial user | 8 sessions × ~$0.15/session |

---

## Churn

- Base assumption: ~16.7%/month (average subscription lifetime ~6 months)
- Optimistic: 10%/month (~10 month average lifetime)
- High churn scenario (25%+): unit economics are negative

**Key churn risk:** Users who have a bad month of shopping (don't need feedback) and cancel; users who feel AI feedback is generic rather than personalized to their style.

---

## Content Creation Dependency

Trial volume depends on TikTok and Instagram content. If posting stops, trials stop.

- 30 hours/month of content creation
- Largest discretionary cost line after product labor
- Must be treated as a fixed cost, not optional spend

---

## Impact of $12 vs. $9 Price

| Metric | $9/month | $12/month |
|---|---|---|
| Net revenue/subscriber | ~$8.10 | ~$11.35 |
| Contribution margin | ~$3.80 | ~$7.05 |
| Breakeven subscribers | ~363 | ~196 |
| Breakeven reduction | baseline | −46% |

**Moving to $12 cuts the breakeven subscriber count nearly in half.** Supported by Van Westendorp data: all 5 Round 2 interviewees said yes to $9, signaling underpricing, and $12 falls within the "good deal" range for the majority.

---

## What Needs to Be Validated

1. **Actual conversion rate** — concierge test when product is ready
2. **Session frequency** — how many sessions per month does the average user need? Fewer than 3–4/month makes the subscription feel like poor value
3. **Churn at paywall moment** — do users pay or drop off at session 8?
4. **LLM cost per session** — depends on model choice and prompt length; estimate needs refinement
