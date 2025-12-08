---
title: "Review: Money Magic"
subtitle: "by Laurence J. Kotlikoff"
permalink: /reviews/
params:
  lang: en
page_id: reviews
date: 2025-11-25
---

![Cover Book Money Magic](img/moneymagic.jpg "Title")

> "I once asked a roomful of economists — all of whom were gathered to discuss household personal finance — to answer, on the fly, the consumption-smoothing question for a hypothetical forty-year-old. I gave them the pertinent information and watched their faces. They weren't happy. They knew they were about to produce a very wrong answer. Right then and there, they seemed to realize that even financially literate people like themselves couldn't make proper financial decisions via introspection." (p. 6)

# Introduction

This very sentence at the beginning of *Money Magic: An Economist's Secrets to More Money, Less Risk, and a Better Life* by **Laurence J. Kotlikoff** perfectly summarizes my current retrospective. Even after years of intensely engaging with the topic of financial planning - even after earning a doctoral degree in a field whose experts pride themselves on *knowing better* - and even after reading this highly interesting book, I must admit somewhat frustrated: I still don’t know everything. And I believe that the state of “knowing it all” will never exist. But (fortunately) for many decisions in life, it is enough simply to know *where* useful information can be found. And this book does exactly that: it taught me a lot of new things and showed me where I can refresh this knowledge whenever needed.

# Short Summary of the Content

Published in 2022, the book provides a comprehensive look at lifetime financial planning and addresses many important questions, such as: How do I choose a lucrative career? How do I obtain a quality education affordably? Until when does it currently make sense to work? Is it financially beneficial to marry—or to divorce? And much more. Prof. Kotlikoff includes many “What would be best for Max Mustermann in situation Y given X?”-style examples. As an economist, I particularly enjoyed the many calculations that effectively support his points.

# My Thoughts on the Book

The book was definitely worth its purchase price (about €12 on [Amazon](https://www.amazon.de/-/en/Money-Magic-Economists-Secrets-Better/dp/0316435996/ref=tmm_pap_swatch_0)[^1]) as well as other opportunity costs. Besides the many interesting aspects I would recommend to everyone, two ideas truly made me think: the **concept of the Living Standard Cone** and the logic behind **“Retirees should invest more in stocks the older they get.”**

[^1]: As of Nov. 2025

## The Living Standard Cone

In Chapter 9 *Invest Like an Economist—Control Your Living Standard Trajectories*, Kotlikoff introduces the idea of the Living Standard Cone. It is based on the concept that annual spending reflects one’s annual living standard. How much someone can spend each year depends partly on the (financial) decisions they make. Different decisions result in different *living standard paths*. Inspired by the figure in the book[^2], I visualized examples of such paths in *Figure 1*. Starting from a baseline of €50,000[^3] in 2025, three scenarios are shown. The dotted line represents a path in which the living standard remains roughly consistent over the next 50 years. I labeled this path *Less Fortunate* because, despite its stability, it reflects gradually declining purchasing power. (That pesky inflation!)

[^2]: See p. 242. \| Unlike the figure in the book, I generated the paths in my figures using stationary time series (without trend and with different positive trends) in R. The script can be found here: [Script_ls_cone.R](downloads/Script_ls_cone.R)

[^3]: What counts toward one’s current living standard? It includes all annual expenses—rent, food, but also yearly savings. This already makes calculating one's current living standard difficult. Accounting for future savings and returns over 50 years makes the task even more complex. If you want to learn how to do this, I recommend Chapter 10 *Making Your Own Money Magic: My Top Fifty Secrets.*

<p align="center">

*Figure 1: A Possible Living Standard Cone*

</p>

![Living Standard Cone](img/money_magic_plot.png)

The other two paths look much better. The *Better* and the *Even Better* paths show developments that I myself wish for my financial future. From year to year, I could afford to spend a little more—and ideally more than inflation eats away.[^4]

[^4]: Although these “better” paths look impressive, even the dashed path would barely make up for the loss in purchasing power—at least if the past 50 years are used as a projection for the future. Inflation strikes again!

The graph also highlights several interesting points.\
1. We will not be able to spend the same amount every year (let alone more). Sometimes our living standard falls - due to illness, unemployment, or other shocks.

2.  Which path we ultimately end up on is uncertain. Here I must offer some critique: In economics, *risk* and *uncertainty* are not synonymous. Decisions under risk assume that individuals know all possible outcomes *and* their probabilities. Under uncertainty, the probabilities are unknown. Although the book frequently uses the word “risk,” I believe that “uncertainty” is the intended meaning - at least that is how I read it, and likely many others do as well. Still, this distinction underscores that we never fully control our living standard.

3.  My favorite insight: When thinking in terms of possible living standard paths, what matters is not only which path we end up on, but how each financial decision can *improve the set of possible paths*. Kotlikoff refers to this set as the **Living Standard Cone**. Its shape (see the grey area in Figure 1) is defined by the lowest and highest possible paths while all paths start at the same point (2025 in the figure).

Why is this cone concept so fascinating? Because it provides a great way to assess the *quality* of financial decisions. Good decisions shift the cone counterclockwise - the best path improves, and the worst path improves as well. Decisions also gain value if they *reduce* the area of the cone, meaning they reduce the number of possible paths.

If a decision causes the cone to rotate leftward and raises the worst path even more strongly relative to the best path - like in Figure 2 -, then it is truly an excellent decision.

<p align="center">

*Figure 2: Good decisions rotate the cone leftward.*

</p>

![Improved Living Standard Cone](img/money_magic_plot2.png)

## **"Retirees should invest more in stocks the older they get."**

The logic expressed on page 266 immediately puzzled me. One of the few recommendations I had always shared with conventional financial advisors is the mantra: *“The younger you are, the more you should invest in stocks. The older you get, the more you should shift toward safe assets.”* Young people have long investment horizons. Downturns such as the 2008/2009 financial crisis can be offset by later bull markets. Over long horizons, portfolios tend to recover and grow. But as one ages, the number of years available to offset bad market phases shrinks. Since older individuals rely on their savings[^5], they rightfully want to avoid seeing their portfolios shrink during bear markets. So what is behind Kotlikoff’s idea?

[^5]: Especially my generation in Germany, should the current federal government (as of Nov. 2025) continue its pension policies. (See [Tagesschau article](https://www.tagesschau.de/wirtschaft/konjunktur/oekonomen-appell-rentenpaket-100.html))

The recommendation is based on portfolio theory developed by [Robert C. Merton](https://mitsloan.mit.edu/faculty/directory/robert-c-merton) and [Paul Samuelson](https://www.nobelprize.org/prizes/economic-sciences/1970/samuelson/biographical/).[^6] This theory is derived from the investor’s optimality problem: deciding how much to consume today and how to allocate remaining wealth between risky (e.g. stocks) and risk-free assets in order to maximize expected intertemporal utility. Depending on the model’s assumptions, this problem can be solved mathematically. A remarkably simple formula emerges for the optimal share of wealth to invest in risky assets, denoted \\(\pi\\):

[^6]: Both are recipients of the Nobel Memorial Prize in Economic Sciences. Samuelson’s contributions and the reasons for his award in 1970 cannot be summarized in a footnote. More information is available in the linked source. Merton’s award (1997) concerned financial theory and risk management, particularly option pricing.

$$
\pi(W,t) = \frac{\mu - r}{\sigma^{2} \gamma}
$$

This percentage depends on the expected return \\(\mu\\), the market volatility \\(\sigma\\), the risk-free rate \\(r\\), and the investor’s degree of risk aversion \\(\gamma\\). Interestingly, the formula does *not* depend on wealth \\(W\\) or time \\(t\\). Meaning: regardless of age or wealth, the *share* of wealth invested in risky assets should remain constant.

*But wait—if the share should stay constant, what investing more in stocks with age?*\
The share stays constant - but maintaining that share requires *action*. The theory implies the following: If the *absolute amount* of **safe** wealth increases, then the amount invested in stocks must also increase to maintain the same risky-asset percentage \\(\pi\\). This is the core of Kotlikoff’s argument. He assumes that retirees have two forms of wealth: safe, periodic income (e.g. pension payments) and invested financial wealth. As retirees gradually draw down their invested wealth, the relative importance of safe wealth increases. To maintain the optimal percentage \\(\pi\\), the remaining portfolio must become more heavily invested in stocks.

As intriguing as this idea is—and as much as it made me think (see *My Take-Aways*) - I find the book’s treatment of the underlying assumptions too brief. The assumptions are only briefly described as unrealistic, yet the resulting recommendations are still applied.[^7]

[^7]: See p. 262.

For instance, the model assumes a world without transaction costs. One might argue this is not far from today’s world, given low-cost trading through neo-brokers. But in economics, transaction costs include more than trading fees - they also include the cost of acquiring information. Even reading this article incurs opportunity costs.

The model also assumes efficient stock markets: all available information is reflected in prices, and price changes result only from random, unpredictable new information. This implies no asset class becomes systematically riskier or yields systematically higher returns. The debate over whether markets are efficient remains unresolved. In 2013, two economists - [Eugene Fama](https://faculty.chicagobooth.edu/eugene-fama) and [Robert Shiller](http://www.econ.yale.edu/~shiller/) - were even jointly awarded the Nobel Prize despite fundamentally opposing views. Fama sees markets as mostly efficient; Shiller argues that psychological forces frequently lead to bubbles, crashes, and predictable deviations from fundamentals.

Another assumption is the full fungibility of wealth and future income: the idea that future labor income can instantly be converted into wealth (e.g. by trading one’s salary for a lump-sum payment).

How realistic assumptions are does not determine a model’s usefulness - after all, maps or Google Maps also rely on simplifications (“The world is two-dimensional”). What matters is predictive accuracy. And here lies my issue with the book: Kotlikoff emphasizes that the Merton-Samuelson theory often fails to predict actual investor behavior, **concluding** that people must be poorly informed or poorly advised. This reasoning ignores a third possibility: many people's decision-making may simply be inadequately represented by the model.

*So was the chapter not worth its opportunity costs after all?*\
It absolutely was. The recommendation is explicitly for *retirees* in the *modern world*. Many retirees today have acquired some financial literacy and can trade at negligible cost (assumption: no transaction costs).

Regarding market efficiency, even Shiller argues that increased information availability improves efficiency—and today information is more accessible than ever (welcome to my site!). Algorithmic trading and Robo-Advisors may also stabilize markets against psychological effects (assumption: efficient markets).

Additionally, the assumption of wealth fungibility appears plausible for many retirees at the start of retirement, as their first pension payments will likely be small compared to their accumulated assets.

Thus, for retirees at the beginning of their pension phase, the model’s assumptions can make sense. Under these circumstances, the conclusion follows: As retirees draw down their savings—and pension income determines more of their living standard—the remaining portfolio should tilt more heavily toward stocks.[^8]

[^8]: Yet I still have an open question: How does this conclusion align with the principle of *risk transfer* that we teach in our undergraduate courses? The concept is based on CRRA utility functions and states that people can *pareto-improve* if risk is transferred from the poor to the wealthy. Wealthier individuals benefit by taking on risk from the less wealthy—e.g. by insuring them. Put simply: the richer you are, the more risk you should take on. The poorer you are, the more you avoid risk.

    Why then should retirees with accumulated wealth—assuming constant relative risk aversion—invest *less* in risky assets the wealthier they are, while the same theoretical foundation suggests that wealthy individuals should *take on* risks from the less wealthy?

    If any reader has more insight on this, I would greatly appreciate hearing from you.

# My Take-Away

The ideas discussed above capture only a small part of what fascinated me about this book and what I genuinely took value from. If I had to summarize my biggest insight, it would be this: Perhaps I should increase the share of safe assets in my portfolio. Even though I am not a retiree yet (and hopefully won’t be for a long time - I enjoy me working!), every additional euro I save slightly reduces the relative importance of my regular income. From the perspective of living standard paths and the Merton-Samuelson theory, it may therefore be time to allocate a larger portion of my wealth to truly safe assets.
