# Pricing Test — AI Styling Feedback App
BUS 395: Venture Creation with AI | Jane Dias | Week of June 23, 2026

---

## 1. Pricing Hypothesis

**"Women aged 22–35 who regularly seek second opinions on outfit choices will pay $9/month for AI styling feedback that gives them honest, personalized advice without the awkwardness of asking friends — because they currently have no reliable, bias-free feedback mechanism, and $9 is less than what they spend on a single item they return anyway."**

**Why $9, not $7:**
$7 was never validated with any interviewee — it was a design choice that carried forward. The unit economics show $7 barely breaks even at 100 users even under optimistic assumptions. $9 is the number the math actually requires, it sits within the competitive range ($7.99–$12.99 for direct comparables), and if Mya and Aly will pay $9, you know $7 also works. If they won't pay $9 but will pay $7, you learn something critical: your price ceiling is below what the model needs. Better to find that out now.

---

## 2. Test Method: Wizard of Oz

**Why Wizard of Oz over the other options:**

- **Smoke test** requires traffic you don't have. Building a landing page and driving 5 signups from cold audience this week is not realistic.
- **Direct ask / Van Westendorp** gives stated preference. People are notoriously optimistic about what they'd pay in hypothetical conversations — "yeah, I'd probably pay that" is very different from handing over a credit card number. Use these questions only as a fallback (see Section 5).
- **Pre-sale** is essentially Wizard of Oz with a delayed delivery promise. Delivering this week is better — you get payment AND product feedback in one test.
- **Wizard of Oz** gives you revealed preference (they pay or they don't) AND product feedback (how they react to the experience) in the same session. No product needs to exist. You deliver the AI analysis manually: user sends a photo, you run it through Claude with their profile context, you send back the response. They get real value. You get a real signal.

**How the manual delivery works:**
User sends a photo via iMessage/WhatsApp. You feed it to Claude with their profile (body proportions they've described, goals, occasion). You send back the response — formatted as if it came from an app. This takes you 5–10 minutes per photo. You are not deceiving anyone; if asked, you say the AI is in testing and you're running it manually. The value is real. The payment is real. The willingness signal is real.

---

## 3. Step-by-Step Plan

### Monday, June 23 (today)

**Action 1: Set up your payment link (30 minutes)**
Create a Venmo or Stripe payment link for $9. If you don't have Stripe: go to dashboard.stripe.com → Payment Links → Create a link for $9 labeled "AI Styling App — First Month." Stripe deposits in 2 business days. Alternatively, Venmo is fine for this test — it's less friction and you're only doing 5 people. Note the link somewhere you can paste it quickly.

**Action 2: Identify your 5 contacts (20 minutes)**
You need 5 people who match the target profile: women who shop, deal with outfit uncertainty, currently solve it by texting friends or nothing. Your list:
1. **Mya** — primary target, named the honesty gap, 20s, limited clothing budget
2. **Aly** — primary target, still stuck on styling decisions, 20s, limited budget
3. **Allison** — secondary, 40s, larger budget, partially solved the problem through experience
4. **One person from your network** — classmate, friend, or Instagram follower who fits the profile (not someone who works in fashion, not a close friend who will say yes to be nice)
5. **One person from your network** — same criteria, someone who would tell you no if they meant no

Write their names down now. Do not leave this as "I'll find someone."

### Tuesday, June 24

**Action 3: Send the outreach message to all 5 (morning)**

Send this individually — not a group text. Personalize the first line.

---
*"Hey [name] — you know how I've been working on that styling app for class? I'm running a paid test this week and thought of you. Here's what it is:*

*You send me a photo from a fitting room, your closet, or before an event. I run it through the AI and send you back honest feedback — does it fit well, does it work for your body, would you actually wear it again. It knows your proportions and goals from what you've told it.*

*I'm testing the price at $9 for the first month. If it's not worth it after the first session, I'll refund you, no argument.*

*If you're in, send $9 to [Venmo handle / Stripe link] with "styling test" in the note and I'll start your first session today. If $9 feels like too much for something you've never tried, totally fair — just let me know and I can ask you a few questions instead.*

*Either answer is useful."*

---

The last two sentences matter. They keep the door open for a Van Westendorp conversation if they decline, and they signal that you are doing research, not sales.

**Action 4: Follow up on any non-responses (afternoon)**
If someone hasn't replied by 3pm, send one follow-up: "Just checking — did my earlier message come through?"

### Wednesday, June 25

**Action 5: Run sessions for anyone who paid**
For each person who sent payment:
- Ask them to send 1–3 photos (fitting room, outfit check, pre-event)
- Note: what did they send first? A shopping photo or a "does this work?" photo? That tells you when the product is most relevant
- Run each photo through Claude with their profile context
- Send back the response. Keep it concise, specific, honest — not "you look great." Specific feedback: what works, what doesn't, why, and whether you'd buy it
- Time how long this takes you per session (you need this for the labor cost estimate in your model)

**Action 6: For anyone who did NOT pay — ask four questions (Wednesday afternoon)**
Do not ghost them. Send: *"No worries at all — can I ask you 4 quick questions? Takes 3 minutes."* Then use the Van Westendorp questions:

1. "At what price would this service be so cheap that you'd doubt the quality?"
2. "At what price would this be a genuinely good deal?"
3. "At what price would it start to feel expensive but you'd still consider it?"
4. "At what price is it just too expensive, full stop?"

Write down their exact answers. Do not coach them or suggest numbers. If they give a range, ask which end they'd actually act on.

### Thursday, June 26

**Action 7: Run sessions for any late payers**
Some people take a day to act. If anyone paid Wednesday, deliver their session Thursday.

**Action 8: Send a 2-question follow-up to anyone who had a session**
*"Two quick questions: (1) On a scale of 1–10, how useful was that feedback compared to asking a friend? (2) If this was a real app for $9/month, would you subscribe? Why or why not?"*

Do not ask leading questions. Do not say "I hope you liked it."

### Friday, June 27

**Action 9: Count the results and make the decision**
Tally: how many people did you contact, how many paid, how many declined, what were the Van Westendorp numbers from decliners. Write three sentences on what you learned. See Section 4 for how to interpret.

---

## 4. What a Yes Signal Looks Like vs. a No Signal

### Strong yes (keep $9, proceed with confidence)
- 3 or more out of 5 pay without negotiating the price
- Those who pay ask for more sessions before the week is out
- Van Westendorp "too expensive" threshold from the other 2 comes in above $9
- At least one person shares it with a friend unprompted

### Weak yes (price works, but retention risk is real)
- 2 out of 5 pay
- Those who pay don't ask for more sessions
- Van Westendorp "too expensive" threshold clusters at exactly $9 — you're at the ceiling
- Signal: lower the price to $7 to reduce churn risk, accept tighter margins, fix the economics elsewhere

### No signal (pricing or product problem — must distinguish between them)
- 0–1 out of 5 pay
- You need to understand whether the barrier is price or value. Ask directly: *"What would make you pay for something like this?"*
  - If they say "I'd pay less" → price problem, run a $5 test (see Plan B)
  - If they say "I'd need to trust it first" → free trial is the right model, but the paywall moment is wrong
  - If they say "I just don't think I need this" → product-market fit problem, return to discovery

**The signal that matters most is not the words — it is the behavior.** Someone who says "I'd definitely use that" but does not send $9 is a no. Someone who says "I'm not sure" but sends $9 immediately after reading the message is a yes. Treat actions as data. Treat words as context.

---

## 5. What to Do If the Test Fails

### If 0–1 people pay at $9

**Plan B: Run a $5 test the following week**

$5/month is below your cost floor ($3–4/month in direct costs per user, not counting your time). You know you cannot run a sustainable business at $5. But the test is not about sustainability — it's about isolating whether the barrier is price or product value.

Specific actions:
- Contact the same 5 people who declined at $9. Say: *"I'm running a second test at a lower price — $5 for one month. Same offer. Would you try it at that price?"*
- If 3+ pay at $5: the product has value but your price was too high. The question becomes whether you can redesign the trial model (shorter trial, lower LLM burn rate) to make $7–8 work. Schedule a session with your professor to work through the math.
- If fewer than 2 pay at $5: the barrier is not price. People do not perceive the product as worth money at any price point yet. This is a product-value problem, not a pricing problem. Do not launch and do not iterate on price. Go back to one-on-one discovery sessions with Mya and Aly and ask: *"Walk me through the last time you had a photo you wanted feedback on. What did you do instead of paying for help?"*

**Plan B is not a pivot.** It is a diagnostic. It tells you which layer of the problem you are actually solving.

### If people pay but don't use the second session

This is a warning sign that appears even in the "yes" scenario. Low engagement after payment means:
- The first session experience did not deliver on the promise, or
- The use case is narrower than you assumed (people want it for shopping trips but not daily outfit checks)

If this happens, do not optimize the marketing. Optimize the session quality. Go back to the transcripts from the first sessions and ask: what did the feedback miss? What question did the user have that the feedback didn't answer?

### If Mya and Aly both decline but Allison pays

This is a product-market fit mismatch that tells you your target customer is wrong. Allison has a bigger budget and a more developed relationship with her wardrobe. The product may be solving a different customer's problem than the one you designed for.

If this happens, schedule a follow-up interview with Allison and one more person in her demographic (40s, budget-conscious, has solved the styling problem partially but imperfectly). Do not pivot to that segment without at least 2 paying users who match it.

---

## Decision Criteria Summary

| Result | Interpretation | Next action |
|---|---|---|
| 3–5 pay at $9 | Price validated | Build toward $9 subscription, update financial model |
| 2 pay at $9 | Weak signal | Run 5 more contacts at $9 before deciding |
| 0–1 pay at $9; Van Westendorp threshold >$9 | Product value problem | Return to discovery |
| 0–1 pay at $9; Van Westendorp threshold $5–8 | Price ceiling below model floor | Run $5 test, revisit unit economics |
| Pay at $9 but don't re-engage | Retention risk | Redesign session experience before launch |
| Allison pays, Mya/Aly don't | Wrong target segment | Interview Allison cohort before proceeding |

---

*Generated: June 2026 | BUS 395: Venture Creation with AI*
*This test must be completed before any further investment in product development.*
