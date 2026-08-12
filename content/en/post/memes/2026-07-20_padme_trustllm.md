---
title: "No, you can't trust them"
author: "Gerrit Stahn"
date: "2026-07-20"
params:
  lang: en
permalink: /posts/memes/
description: "Three LLMs — ChatGPT, Gemini, and Claude — were asked to compare interest
  earnings on two savings products. All three made the same subtle timing mistake,
  showing why AI answers to money questions still need a human sanity check."
keywords:
- LLM Financial Reasoning
- ChatGPT vs Gemini vs Claude
- AI Interest Calculation
- Savings Comparison
- Money Market Fund
- Overnight Account
- Behavioral Finance
- Gerrit
- Stahn
- Gerrit Stahn
---

## ![Anakin - Padme - Would you trust them?](/img/memes/padme_trustllms.jpg)

##

------------------------------------------------------------------------
##

**Context:** Having just moved to Vancouver, Canada without a steady flow of monthly remuneration, I've been leaning on my accumulated wealth to smooth out my current consumption.[^1] Those savings are split between an overnight account and a money-market fund, which left me with a very practical question: which pot should I draw down first? Being an economist, I naturally reframed this as "which option carries the higher opportunity cost in forgone interest for the rest of the year?" — and decided to treat forgone interest as the full measure of that cost.

[^1]: For anyone who isn't an economist: It means that I don't have a job in Canada and I'm using my savings to cover my bills.

A few details made the comparison trickier than it first looked. First, the overnight account is brand new (opened May 20) and currently earns a promotional 4% p.a. for four months; once that window closes on September 20, the rate falls to 2% p.a. Second, my money-market fund position actually dates back to August 2025, so the opportunity-cost clock for that account doesn't start from the same point. Third, the fund's return isn't fixed — it moves around — so I simplified by assuming an average annual return of 2%, which lines up reasonably well with its historical performance.

Naturally, I ran the numbers myself first, but I was curious whether an LLM could reach the same answer. Below are the responses from ChatGPT (GPT-5.5), Google Gemini (3.5 Flash), and Claude (Sonnet 5) to an identical prompt, using €1,000 in the account and €950 in the fund:

------------------------------------------------------------------------
> Prompt: Compare the interest earnings over a one-year period (starting January 1, 2026) for two different investments: Investment 1: On May 20, I invested €1,000. I receive a promotional interest rate of 4% p.a. until September 20. Starting September 21, the rate drops to 2% p.a. Investment 2: On August 8, 2025, I invested €950. I receive a permanent interest rate of 2% p.a. for this investment.
------------------------------------------------------------------------

All three models share the same underlying flaw for Investment 2. Before reading on, see if you can spot it yourself.

<div style="
  margin: 2rem auto;
  max-width: 900px;
">

  <div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  ">
    <iframe 
      src="/pdf/Investment Interest Comparison_ChatGPT.pdf"
      style="width:100%; height:850px; border:none;">
    </iframe>
  </div>
    <p style="
    text-align: center;
    margin-top: 1rem;
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #555;
  ">
    ChatGPTs Output
  </p>
</div>

------------------------------------------------------------------------
##

<div style="
  margin: 2rem auto;
  max-width: 900px;
">

  <div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  ">
    <iframe 
      src="/pdf/Investment Interest Comparison 2026 - Google Gemini.pdf"
      style="width:100%; height:850px; border:none;">
    </iframe>
  </div>
    <p style="
    text-align: center;
    margin-top: 1rem;
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #555;
  ">
    Geminis Output
  </p>
</div>

------------------------------------------------------------------------
##

<div style="
  margin: 2rem auto;
  max-width: 900px;
">

  <div style="
    border: 1px solid #ddd;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  ">
    <iframe 
      src="/pdf/Investment Interest Comparison 2026 - Claude.pdf"
      style="width:100%; height:850px; border:none;">
    </iframe>
  </div>
    <p style="
    text-align: center;
    margin-top: 1rem;
    font-size: 2rem;
    margin-bottom: 2rem;
    color: #555;
  ">
    Claudes Output
  </p>
</div>

------------------------------------------------------------------------
##

Here's the catch: every one of the three assumes the fund investment only starts earning returns from January 1, 2026 onward — even though the money has actually been sitting there generating returns since August 2025. That's a reasonable-sounding shortcut, since the prompt frames the comparison window as starting on January 1st, but it quietly ignores interest already accrued before that date. Accounting for the roughly 145 days between the August 2025 deposit and year-end, the fund would have already earned:

$$
950 \cdot \left(0.02 \cdot \frac{145}{360}\right) \approx 7.75€
$$

So rather than the roughly €19 in 2026 that a "clean start on January 1st" assumption implies, the actual gain for the year should reflect the slightly larger base built up from that earlier interest:

$$
957.5 \cdot 0.02 = 19.15€
$$

That gap looks tiny, but remember this example uses fairly modest savings — the kind of amount you're stuck living off when you move to Vancouver without a job lined up.

It's also worth comparing how the three models handled Investment 1. Claude and Gemini both landed on the same figure I calculated by hand — call it the "PhD-in-economics" version. ChatGPT, by contrast, gave an answer like an undergrad in Economics: Technically right given its own stated assumption at the beginning, but fails to include all information from the task.

So where does the real problem come from? It turns out to be baked into how I phrased the prompt. Swap "over a one-year period (starting January 1, 2026)" for simply "in the year 2026," and the picture shifts: Claude redoes the calculation but now flags that it's ignoring compounding effects on the first investment, Gemini arrives at the "PhD-in-economics" result, and ChatGPT remains just as far off as before.

The takeaway (again): don't hand your money decisions over to an LLM at face value — that's the point of the meme. Instead treat these tools as a way to cross-check your own reasoning. And if their answers disagree with yours, it is (only) a signal you might be wrong — not a prove.
