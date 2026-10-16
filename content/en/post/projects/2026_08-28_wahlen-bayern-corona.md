---
title: "The Toll of Voting in a Pandemic"
date: 2026-08-28
description: "My first publication!"
keywords: ["COVID-19", "Bavaria", "municipal elections", "voter turnout", "pandemic", "synthetic control method", "health economics"]
tags: ["Research", "COVID-19", "Elections", "Health Economics", "Publication"]
slug: "bavaria-election-covid"
translationKey: "wahlen-bayern-corona"
author: "Gerrit Stahn"
draft: false
---

On March 15, 2020, nearly ten million eligible voters in Bavaria went to the polls for local municipal elections — just days after the WHO had officially declared COVID-19 a pandemic. While other German states and many countries postponed elections or switched entirely to mail-in voting, most Bavarians cast their vote in person, as usual. A few weeks later, Bavaria had the highest COVID-19 case and death counts of any German state.

Was this a coincidence — or did the election itself contribute to the spread of the virus? That's exactly the question we investigate in our new study, which has just been accepted for publication in the *European Journal of Health Economics*.

## How we approached the question

We combined two independent empirical strategies:

**1. The Synthetic Control Method: Bavaria vs. "Synthetic Bavaria".**
Using the so-called Synthetic Control Method (SCM), we constructed a statistical "twin" for each of Bavaria's 96 districts out of all non-Bavarian districts — a synthetic control district. In simplified terms, it works like this: a weighting procedure assigns each non-Bavarian district a weight based on how closely it resembled the given Bavarian district before the election — in terms of population structure, economic conditions, health care provision, childcare availability, and prior COVID-19 case numbers. These weights are then multiplied by the actual COVID-19 figures of the respective districts *after* the election and summed up. The result is the fictional, "synthetic" value that the Bavarian district would presumably have reached had it not been affected by the election.[^1] Aggregating these synthetic values across all Bavarian districts yields an estimate of how case numbers in Bavaria would likely have developed *without* the election.

[^1]: For example, in our baseline specification, the synthetic twin of the state capital Munich is composed of 57% Stuttgart, 32% Frankfurt am Main, and 11% Leipzig.

![Weekly COVID-19 cases per 100,000 inhabitants by federal state](/img/bayernwahl/fig1.png)
*Figure 1: Weekly COVID-19 cases across German states — Bavaria clearly diverges from the rest starting the week after the election.*

![Weekly COVID-19 deaths per 100,000 inhabitants by federal state](/img/bayernwahl/fig2.png)
*Figure 2: Weekly COVID-19 deaths across German states — Bavaria diverges here too, following the election.*

**2. A within-Bavaria comparison.**
We also examined whether Bavarian districts with higher voter turnout experienced a steeper rise in case numbers after March 15 than districts with lower turnout — while controlling for alternative explanations, such as distance to the COVID-19 hotspot Ischgl or the number of "Starkbier" (strong beer) festivals held shortly before the lockdown.

## What we found

- Bavaria saw a substantially steeper rise in COVID-19 cases after the election than the trajectory of comparable districts would have predicted — **over a third** of the post-election increase in case numbers cannot be explained by demographic, economic, or health-related differences, nor by proximity to Ischgl.

![SCM result for case numbers](/img/bayernwahl/fig5.png)
*Figure 3: Actual versus synthetic case trajectory in Bavaria — the gap widens roughly two weeks after election day.*

- Within Bavaria, a one-percentage-point increase in voter turnout is associated with roughly **12.8 additional confirmed cases and 1.8 additional deaths per 100,000 inhabitants** — scaled up to the whole state, this corresponds to about 1,680 additional cases and 236 additional deaths in the period up to April 5, 2020.
- The effect shows up both for in-person voting and mail-in voting. This suggests that it wasn't only the act of casting a ballot itself that mattered, but also related activities such as campaign events or vote counting.
- For cases, the effect was strongest among 35- to 59-year-olds; for deaths, it was concentrated among those aged 80 and above — consistent with the well-known pattern that older individuals face a substantially higher mortality risk.

![Cases: heterogeneity by age group](/img/bayernwahl/fig14_new.png)
*Figure 4: Effect of voter turnout on COVID-19 cases by age group.*

![Deaths: heterogeneity by age group](/img/bayernwahl/fig15_new.png)
*Figure 5: Effect of voter turnout on COVID-19 deaths by age group.*

- Our results proved robust across numerous checks — for instance, when using the date of symptom onset instead of the reporting date, or when testing a "placebo election day" in June, for which we find, as expected, no effect.

## Why this matters

Our study provides some of the first causally interpretable evidence that the timing of elections during an escalating pandemic can have a measurable impact on the spread of an infectious disease. This doesn't mean elections should categorically be avoided during crises — after all, they are a cornerstone of democratic systems. But it does underscore how important it is to factor in health risks upfront when deciding on the timing and format of elections — for example, by expanding mail-in voting or enforcing stricter hygiene measures at polling stations, which should also protect poll workers.

## Acknowledgments

This paper is the result of a long shared journey, and I want to thank, from the bottom of my heart: my co-authors Jochen Güntner, Felix Krüger, and Amelie Wuppermann for the close and productive collaboration; our student research assistants Armando, Erika, Liselotte, Loredana, and Vera at MLU Halle-Wittenberg for their invaluable help with data preparation; Wolfgang Greiner as the responsible editor at the *European Journal of Health Economics* for his careful handling of the review process; and two anonymous referees, whose constructive feedback substantially improved the paper.

*The paper will soon appear in the renowned European Journal of Health Economics (ABDC: A). A link to the final version will follow once it's available online.*