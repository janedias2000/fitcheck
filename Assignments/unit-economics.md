# Unit Economics
## BUS 395: Venture Creation with AI
**Venture:** AI Styling Feedback Platform  
**Date:** June 2026  
**Model:** Ad-supported free tier (non-fashion ads) + optional paid subscription (~$6/month, ad-free + memory)

---

## Assumption Key
- **[DATA]** — grounded in competitive research or interview data
- **[ASSUMED]** — derived from industry reasoning, no direct evidence
- **[UNVALIDATED]** — appears in your BMC but no customer confirmed it

---

## 1. Revenue Per Customer Per Month

### Free User
| Item | Number | Source |
|---|---|---|
| Sessions per month | 8 | [ASSUMED] — interviews show episodic shopping (1–2 trips/month) plus uncertain mornings; no usage data exists |
| Ads shown per session | 1.5 | [ASSUMED] — post-decision placement only, never during feedback |
| Impressions per user/month | 12 | Derived from above |
| CPM (skincare/lifestyle/travel, 22–35F) | $8.00 | [ASSUMED] — industry range for female lifestyle targeting is $5–$15; $8 is mid-range |
| Ad fill rate (small app, early stage) | 70% | [ASSUMED] — small publishers typically see 60–80% fill |
| Ad network revenue share (e.g. AdMob) | 65% to publisher | [ASSUMED] — AdMob standard is ~60–70% publisher share |
| **Net ad revenue per free user/month** | **$0.04** | 12 × $8 × 0.70 × 0.65 / 1000 |

**This number is small by design. Ad-supported requires scale. At 10,000 free users: ~$440/month.**

### Paid User
| Item | Number | Source |
|---|---|---|
| Monthly subscription price | $6.00 | [UNVALIDATED] — BMC hypothesis, never tested with any interviewee |
| Apple App Store fee (Year 1) | 30% | [DATA] — Apple's published fee structure |
| Apple App Store fee (Year 2+) | 15% | [DATA] — Apple's published reduced rate for subscriptions >1 year |
| Net after App Store (Year 1) | $4.20 | $6.00 × 0.70 |
| Net after App Store (Year 2+) | $5.10 | $6.00 × 0.85 |
| Subscription refund rate | 5% | [ASSUMED] — App Store allows user-initiated refunds; industry average 3–8%; Apple processes automatically with no developer recourse |
| **Net after App Store + refunds (Year 1)** | **$3.99** | $4.20 × 0.95 |
| Stripe fee (if web subscription instead of App Store) | 2.9% + $0.30 | [DATA] — Stripe published pricing |
| Net via Stripe (web only, no refunds applied) | $5.53 | $6.00 × 0.971 − $0.30 |

**Use $3.99 as your base case for Year 1 (App Store + refund adjustment). Google Play charges the same 15%/30% structure as Apple — these numbers apply identically on Android.**

---

## 2. Cost to Serve One Customer Per Month

### A. Direct Costs

**AI Inference (the largest direct cost)**

| Model | Cost per session | Free (8 sessions) | Paid (20 sessions) | Source |
|---|---|---|---|---|
| Claude Haiku | ~$0.001 | ~$0.008 | ~$0.020 | [ASSUMED] — estimated from Anthropic pricing structure |
| Claude Sonnet | ~$0.010 | ~$0.080 | ~$0.200 | [ASSUMED] — estimated from Anthropic pricing structure |
| GPT-4V | ~$0.020 | ~$0.160 | ~$0.400 | [ASSUMED] — estimated from OpenAI pricing structure |

**Critical flag:** At $0.04 ad revenue per free user and $0.08 AI cost (Sonnet), every free user costs you more in AI than they generate in ads. The model only works if free users run on Haiku-class and paid users run on Sonnet-class. This price difference also creates a real quality gap that motivates upgrades.

Working assumption:
- Free users: Haiku → $0.008/month
- Paid users: Sonnet at ~20 sessions → $0.200/month

**Hosting and Infrastructure**

| Item | Cost/user/month | Source |
|---|---|---|
| App backend (Firebase/Supabase) | $0.050 | [ASSUMED] — free tier covers ~10,000 users; above that, ~$0.05/user |
| CDN / image delivery | $0.010 | [ASSUMED] — Cloudflare free tier + minimal AWS transfer costs |
| Image storage (paid users only) | ~$0.002 | [ASSUMED] — ~20 photos × 3MB = 60MB × $0.023/GB (AWS S3) |
| **Total hosting/user/month** | **$0.060** | |

**Content Moderation**

| Item | Cost/user/month | Source |
|---|---|---|
| Photo moderation (AWS Rekognition or Google Vision SafeSearch) | $0.012 | [ASSUMED] — $1–$1.50 per 1,000 images; at 8 sessions/user = 8 images checked/user/month; at 1,000 users = 8,000 images × $1.50 = $12/month total |

This is non-optional. Users upload photos of themselves in fitting rooms and at home. No moderation means no mechanism to catch inappropriate content. Regulatory and legal exposure from personal photo storage compounds if there is no evidence of a reasonable safety layer. This cost scales linearly with sessions — it is the most predictable cost in the model.

**Direct Cost Summary**

| User type | AI | Hosting | Moderation | Total direct |
|---|---|---|---|---|
| Free (Haiku) | $0.008 | $0.060 | $0.012 | **$0.080** |
| Paid (Sonnet) | $0.200 | $0.060 | $0.012 | **$0.272** |

---

### B. Your Time (valued at $15/hour)

All [ASSUMED] — track actual hours once live.

| Activity | Hours/month | Cost/month | Notes |
|---|---|---|---|
| Content creation (TikTok/Instagram) | 30 hrs | $450 | 3 posts/week × 2.5 hrs — classified as CAC spend, not fixed cost |
| Product maintenance and iteration | 15 hrs | $225 | Bug fixes, prompt tuning, UX updates |
| Customer support | 10 hrs | $150 | Scales with users; ~5% contact rate at 1,000 users |
| Business operations | 5 hrs | $75 | Admin, planning, tracking |
| Bookkeeping and tax records | 2 hrs | $30 | Reconciling revenue, tracking expenses, preparing for tax filing |
| **Total Jane time/month** | **62 hrs** | **$930** | At 1,000 users: $0.93/user/month |

**Critical assumption:** This entire cost structure assumes Jane builds and maintains the app herself. If she needs a developer:
- MVP development (iOS contractor): $10,000–$30,000 one-time [ASSUMED]
- Ongoing maintenance (contractor): $1,000–$3,000/month [ASSUMED]
- At those costs, every break-even number below is wrong by an order of magnitude.

Even building it herself, the upfront development time (estimated 200–400 hrs at $15/hr = $3,000–$6,000) is a real opportunity cost not in the monthly figures. Amortized over 24 months: ~$125–$250/month additional.

---

### C. Customer Acquisition Cost (CAC)

| Item | Number | Source |
|---|---|---|
| Organic CAC estimate | $10–$20 | [UNVALIDATED] — appears in your BMC, not grounded in any acquisition data |
| Implied by Jane's content time | ~$7.50–$37.50 | [ASSUMED] — depends entirely on content performance; 1/100 to 1/500 viewers converting |
| Paid acquisition CAC | $100+ | [DATA] — BMC note grounded in general app acquisition benchmarks |

Use $15 as your working assumption. It is the single number most likely to be wrong.

CAC amortized over 12-month retention: **$1.25/user/month**

Influencer partnerships: your BMC lists body-type influencers as a key acquisition channel. Influencer partnerships are not free. Even micro-influencer gifted deals have an opportunity cost. Paid influencer rates for micro-influencers (10–50K followers) run $100–$500/post. If you run 1 influencer partnership per month: adds $100–$500 to CAC spend. Not included in the $15 assumption — flag if you use this channel.

---

### D. Storage, Shipping, Physical Handling

**$0.** No inventory, no fulfillment, no packaging. Correct to exclude.

Equipment note: assumes Jane already owns a laptop and phone adequate for development and testing. If a current iOS device is needed to test camera features: $500–$1,500 one-time. Not in monthly calculations.

---

### E. Insurance, Liability, Compliance

| Item | Monthly cost | Source |
|---|---|---|
| General liability insurance (solo business) | $42–$125 | [ASSUMED] — typical range for small digital business |
| **Cyber liability insurance** | **$50–$150** | [ASSUMED] — app stores personal photos in fitting rooms and at home; a breach involving those images is materially different liability; standard GL does not cover data breaches |
| Privacy policy + terms of service (amortized one-time) | ~$17 | [ASSUMED] — $200 one-time over 12 months |
| GDPR/CCPA compliance tooling | ~$25 | [ASSUMED] — basic consent management |
| Apple developer account | ~$8 | [DATA] — $99/year |
| Google Play developer account | $2 | [DATA] — $25 one-time; ~$2/month amortized over 12 months |
| **Business registration / LLC** | **$17–$67** | [ASSUMED] — one-time formation ($50–$500 by state) + annual fees ($50–$800/year); California LLC minimum franchise tax is $800/year = $67/month alone |
| Sales tax tooling | $0–$19 | [ASSUMED] — ~30+ states require sales tax on SaaS subscriptions; TaxJar free tier handles early scale |
| **Total compliance/month** | **~$200–$280** | Increased from v1's $100 by cyber liability + LLC |

At 1,000 users: **$0.20–$0.28/user/month**

**Professional liability / E&O insurance:** Excluded. The product gives styling advice; a user claiming harm from that advice is theoretically possible but practically low risk at early stage. E&O insurance for a solo app runs $50–$200/month. Revisit if the venture scales or advice becomes more consequential. Estimated impact if excluded and a claim arises: potentially uncapped personal liability.

---

### F. Transaction / Payment Processing

| Scenario | Fee | Source |
|---|---|---|
| Via App Store (iOS subscription) | Included in 30%/15% platform fee — do not double-count | [DATA] |
| Via Stripe (web subscription) | 2.9% + $0.30 = $0.47 on $6 | [DATA] |
| Stripe chargeback fee (disputed transaction) | $15 per dispute | [DATA] — Stripe published pricing |

Refund/chargeback impact: 5% refund rate already captured in $3.99 net revenue. Stripe chargebacks are separate — estimated <0.5% of transactions; $15/dispute; estimated impact: <$0.01/user/month at small scale. Not material at early stage but worth monitoring.

---

### G. Fixed Overhead (accrues regardless of users)

| Item | Monthly cost | Source | vs. v1 |
|---|---|---|---|
| Domain registration | ~$1 | [DATA] — ~$12/year | Included |
| Basic hosting (pre-users) | ~$20 | [ASSUMED] | Included |
| Design tools (Figma) | $12 | [DATA] | Included |
| AI development tools | $20 | [ASSUMED] | Included |
| Apple developer account | $8 | [DATA] | Included |
| General liability insurance baseline | $42 | [ASSUMED] | Included |
| **Cyber liability insurance** | **$100** | [ASSUMED] — midpoint of $50–$150 | **Added** |
| **Business registration / LLC (California)** | **$67** | [ASSUMED] — $800/year CA minimum franchise tax | **Added** |
| **Business email (Google Workspace)** | **$6** | [DATA] — $6/month per user, published by Google | **Added** |
| Email infrastructure (Resend free tier) | $0 | Free up to 3,000 emails/month; sufficient at early scale | **Added — $0 at launch** |
| App analytics (PostHog free tier) | $0 | Needed to measure session frequency, conversion, retention; free at early scale | **Added — $0 at launch** |
| Error/crash monitoring (Sentry free tier) | $0 | Free up to 5,000 errors/month | **Added — $0 at launch** |
| Code repository (GitHub free tier) | $0 | Free for solo developers | **Added — $0** |
| Accounting software (Wave) | $0 | Wave is free; QuickBooks Solopreneur is $20/month if preferred | **Added — $0** |
| Sales tax tooling (TaxJar basic) | $0 | Free tier handles early scale | **Added — $0 at launch** |
| **Total fixed overhead/month** | **~$276** | Increased from v1's $103 | |

---

## 3. Gross Margin Per Customer

### Free User (Haiku model)
| Item | Amount |
|---|---|
| Revenue | $0.040 |
| AI inference | $0.008 |
| Hosting | $0.060 |
| Content moderation | $0.012 |
| **Total direct cost** | **$0.080** |
| **Gross margin (direct costs only)** | **−$0.040** |

Worsened from v1's −$0.028. Content moderation (+$0.012) pushes the per-user loss deeper.

### Paid User (Sonnet model, Year 1 App Store, 5% refund rate)
| Item | Amount |
|---|---|
| Revenue (net of App Store 30% + 5% refund rate) | $3.99 |
| AI inference (~20 sessions × $0.01) | $0.200 |
| Hosting | $0.060 |
| Content moderation | $0.012 |
| **Total direct cost** | **$0.272** |
| **Gross margin (direct costs only)** | **$3.72 (93%)** |

Slightly lower than v1's $3.94, driven by the refund rate and moderation cost.

### Blended Gross Margin by Conversion Rate

| Conversion rate | Revenue/100 users | Direct costs/100 users | Gross margin | Per user | vs. v1 per user |
|---|---|---|---|---|---|
| 1% paid | $7.95 | $8.19 | −$0.24 | −$0.002 | v1: −$0.042 |
| 2% paid | $11.90 | $8.38 | $3.52 | $0.035 | v1: $0.040 |
| 5% paid | $23.75 | $8.96 | $14.79 | $0.148 | v1: $0.170 |
| 10% paid | $43.50 | $9.92 | $33.58 | $0.336 | v1: $0.369 |

---

## 4. Break-Even on Fixed Costs

### Monthly Fixed Cost Base
| Item | Monthly cost |
|---|---|
| Jane's time — product + support + ops + bookkeeping | $480 |
| Fixed overhead (tools, insurance, infrastructure, compliance) | $276 |
| **Total fixed costs/month** | **$756** |

Content/CAC spend ($450/month) excluded — you can pause acquisition spending. $756 is the floor regardless.

v1 fixed costs were $553/month. Increase of $203 from: cyber liability (+$100), LLC registration (+$67), bookkeeping time (+$30), business email (+$6).

### Break-Even Users by Conversion Rate

| Conversion rate | Contribution margin/user | Break-even users | vs. v1 |
|---|---|---|---|
| 1% | −$0.002 | Never (barely negative on direct costs) | v1: Never |
| 2% | $0.035 | **21,600** | v1: 13,825 |
| 5% | $0.148 | **5,108** | v1: 3,253 |
| 10% | $0.336 | **2,250** | v1: 1,499 |

Break-even threshold moved up ~55% at every conversion rate because fixed costs increased from $553 to $756/month.

---

## 5. Taxes

**Largest omission in v1. Every number above is pre-tax. Taxes are not optional.**

| Tax type | Rate | Practical impact |
|---|---|---|
| Self-employment tax (US) | 15.3% of net profit; effective ~14.1% after the deductible half | On $10,000 net profit: ~$1,410 owed before income tax |
| Federal income tax | 10–22% depending on total income | For a student with modest venture income, may be 0% if below the standard deduction (~$14,600 for 2024); becomes material once profitable |
| California state income tax | 4–9.3% for typical income ranges | Applies on top of federal |
| Sales tax on SaaS subscriptions | Varies by customer location; ~30+ states require it | Must collect, track, and remit based on where each customer is located, not where Jane is; TaxJar automates this; non-compliance is a legal violation even if the dollar amount is small |

**How to apply to break-even:** Any target monthly profit figure needs to be grossed up for taxes. If the goal is $1,000/month take-home, the business needs to generate ~$1,250–$1,430/month in net profit before taxes to net $1,000 after self-employment tax + state income tax.

---

## 6. CAC Payback Period

CAC assumption: **$15** [UNVALIDATED — from BMC]

| Conversion rate | Contribution margin/user/month | CAC payback | vs. v1 |
|---|---|---|---|
| 2% | $0.035 | 429 months (36 years) | v1: 375 months |
| 5% | $0.148 | 101 months (8.4 years) | v1: 88 months |
| 10% | $0.336 | 45 months (3.7 years) | v1: 41 months |

None acceptable. Industry standard for consumer apps: 6–18 months. All scenarios moved in the wrong direction vs. v1.

The math only works if one or more of:
- Subscription price is higher than $6 (untested with any customer)
- Conversion rate exceeds 10% (not supported by competitive data in this category)
- CAC is below $15 (possible if content goes viral, not plannable)
- Session frequency is much higher, driving more ad revenue per free user

---

## 7. What Needs to Change for the Model to Work

**Lever 1: Validate the subscription price**
$6/month was never tested. If the right price is $12/month, paid user net revenue roughly doubles to ~$8.17 after App Store and refunds (Year 2+). CAC payback at 5% conversion drops from 101 months to ~30 months — still bad, but not insane. Ask Mya and Aly before setting any number.

**Lever 2: Use tiered AI models**
Free users on Haiku-class, paid users on Sonnet-class. Keeps direct costs low on the large free tier and creates real quality differentiation. Already reflected in these calculations — do not skip this.

**Lever 3: Push conversion above 5%**
The break-even math is unworkable below 5%. Memory as the upgrade value (paid users get a profile that builds; free users start fresh) is the right mechanism, but you have no data on whether it actually converts.

---

## 8. All Cost Categories — Full Audit

| Category | Status | Estimated monthly impact |
|---|---|---|
| Physical storage (inventory, warehouse) | $0 — no physical product | $0 |
| Transport / shipping | $0 — no physical product | $0 |
| Packaging / supplies | $0 — no physical product | $0 |
| Raw materials / manufacturing | $0 — no physical product | $0 |
| Equipment (laptop, phone) | Assumed owned — not stated | $0 if owned; $500–$1,500 one-time if not |
| AI inference | Included | $0.008–$0.200/user/month depending on tier |
| App hosting / backend | Included | $0.050/user/month |
| CDN / image delivery | Included | $0.010/user/month |
| Image storage | Included | $0.002/user/month (paid only) |
| Content moderation | Added in v2 | $0.012/user/month; scales with sessions |
| Email infrastructure | $0 via free tier — noted | $20–$50/month above ~10,000 users |
| Push notifications | $0 via Firebase — noted | $10–$50/month at scale |
| App analytics | $0 via free tier — noted | $0 at early scale; needed operationally |
| Error / crash monitoring | $0 via free tier — noted | $0 at early scale |
| Code repository (GitHub) | $0 via free tier — noted | $0 |
| A/B testing tools | $0 — correct for early stage | $0 |
| Jane's time — content / acquisition | Included | $450/month (CAC) |
| Jane's time — product, ops, support | Included | $450/month (fixed) |
| Jane's time — bookkeeping | Added in v2 | $30/month |
| Jane's time — App Store assets + ASO | Not included | ~$120/month (8 hrs at $15/hr); one-time asset creation + ongoing keyword maintenance |
| App development (if contractor needed) | Not included — critical assumption | $10,000–$30,000 one-time + $1,000–$3,000/month; would invalidate all break-even numbers |
| Paid advertising | Intentionally excluded (organic-first) | CAC would jump to $100+ if needed |
| Influencer partnerships | Not included | $0 if gifted-only; $100–$500/month per partnership if paid |
| General liability insurance | Included | $42–$125/month |
| Cyber liability insurance | Added in v2 | $50–$150/month; non-trivial given personal photo storage |
| Professional liability / E&O | Excluded (acceptable at early stage) | $50–$200/month; excluded because risk is low at launch |
| Privacy policy / TOS | Included | $17/month amortized |
| GDPR / CCPA compliance | Included | $25/month |
| Business registration / LLC | Added in v2 | $17–$67/month depending on state |
| Intellectual property (trademark) | $0 — correct for early stage | $0 now; $250–$400 one-time if pursued later |
| Tax preparation (CPA or software) | Not included | $100–$500/year = $8–$42/month |
| Payment processing (App Store) | Included — deducted from revenue | 30% Year 1, 15% Year 2+ |
| Payment processing (Google Play) | Included — same structure as Apple | 30% Year 1, 15% Year 2+ |
| Payment processing (Stripe, if web) | Included — alternative scenario | 2.9% + $0.30/transaction |
| Chargeback fees (Stripe) | Not included — immaterial | <$0.01/user/month at small scale |
| Subscription refunds | Added in v2 | 5% refund rate; reduces paid user net revenue from $4.20 to $3.99 |
| Bank account fees | $0 — free business checking available | $0 via Mercury or Relay |
| Accounting software | $0 via Wave — noted | $0 at early scale |
| Self-employment / income tax | Added in v2 — not in per-user cost, applied to net profit | ~14–25% of net profit |
| Sales tax on subscriptions | $0 via TaxJar free tier — noted | Non-monetary compliance risk if ignored; small dollar amount |
| Business email | Added in v2 | $6/month (Google Workspace) |
| Customer support tools | $0 at early scale — noted | $25–$95/month at scale |
| Returns / refunds on physical goods | $0 — no physical product | $0 |

---

## 9. Numbers Flagged for Validation Before Building

| Number | Current assumption | How to validate |
|---|---|---|
| Subscription price ($6/mo) | Unvalidated — BMC hypothesis | Ask Mya and Aly directly what they pay for apps monthly and what this would be worth |
| Session frequency (8/month) | Assumed | Track your own usage for 2 weeks; ask 3 users to log for a week |
| Free-to-paid conversion (2–5%) | Assumed — comparable app category | Run a fake door test: show the upgrade prompt before building paid tier |
| CAC ($15) | Partially grounded in BMC, not validated | Track actual cost per acquired user from first 50 organic users |
| AI model cost | Estimated from published pricing | Get exact numbers from Anthropic/OpenAI API docs before building |
| Ad CPM ($8) | Industry assumption | Contact Google AdMob for estimated CPM for your audience profile |
| User retention (12 months) | Fully assumed | Unknown until product exists |
| Refund rate (5%) | Industry estimate | Check App Store Connect analytics once live; no way to validate before launch |
| Content moderation cost ($0.012/user) | Calculated from AWS pricing | Get a quote from AWS Rekognition or Google Vision API before building |
