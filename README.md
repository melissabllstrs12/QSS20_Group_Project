# Cost–Benefit Analysis of U.S.–China Tariffs (2018–2019)
Group Members:

Melissa Ballesteros, Luis Ortiz Velasquez, Viviana Perez

# Introduction

In 2018–2019, the United States imposed a series of tariffs on Chinese imports under Section 301, marking the beginning of a major trade conflict between the U.S. and China. These tariffs were justified as a way to:

Protect domestic manufacturing

Restore U.S. jobs

Reduce reliance on foreign imports

However, tariffs also increase costs for firms and consumers and may trigger retaliation from trading partners.

This project evaluates the cost–benefit tradeoff of tariff protection by answering the following question:

Did exposure to tariff protection increase employment in protected industries, and were any gains offset by higher prices?

We focus specifically on industries heavily affected by tariffs — particularly steel manufacturing — and examine both:

Labor market effects

Producer price responses


# Research Question

Our central research question is:

How did exposure to the 2018–2019 U.S.–China tariffs affect employment dynamics in import-competing industries, and to what extent were labor market gains offset by price increases?

Sub-questions include:

Did steel industry employment increase after tariff implementation?

Were these effects statistically significant?

Did industries facing greater tariff exposure experience higher producer prices?   

# Data Sources 

4.1 Employment Data

We use industry-level employment data from:

U.S. Bureau of Labor Statistics (BLS)
Quarterly Census of Employment and Wages (QCEW)

Coverage: 2015–2019

Unit of analysis: State–Industry–Year

Key variables:

Total employment

Average weekly wages

Industry classification (NAICS codes)

Treatment Industry

NAICS 331110: Iron and Steel Mills and Ferroalloy Manufacturing

Control Industry

NAICS 331523: Nonferrous Metal Die-Casting

We construct average annual employment from quarterly values and log-transform employment for interpretation in percentage terms.


4.2 Price Data

To measure price responses, we use:

Producer Price Index (PPI) data from the Bureau of Labor Statistics.

This allows us to test whether tariff-protected industries experienced larger price increases relative to baseline trends.

# Methodology
5.1 Difference-in-Differences (DiD) Framework

We implement a Difference-in-Differences model comparing:

Treated industry (steel)

Control industry (non-tariff-affected metal manufacturing)

Pre-tariff period (2015–2017)

Post-tariff period (2019)

Regression specification:
#insertequation 

5.2 Price Pass-Through Analysis

We examine whether industries exposed to tariffs experienced:

Statistically significant increases in producer prices

Evidence of tariff pass-through

This evaluates whether consumers and downstream firms bore the cost of protection.


# Results (Preliminary)
Employment Effects

Estimated employment increase in steel: ~12.5%

Marginal statistical significance (p ≈ 0.097)

Interpretation:

Suggestive evidence of employment gains

Not strong enough to conclusively attribute gains solely to tariffs

# Price Effects

Existing Federal Reserve research suggests:

Tariffs were largely passed through to U.S. prices

Foreign exporters did not fully absorb the costs

Our project evaluates this mechanism at the industry level using PPI data.


# Data Pipeline

Download yearly QCEW datasets (2015–2019)

Filter for treatment and control NAICS codes

Compute annual average employment

Create treatment and post indicators

Log-transform employment

Merge with tariff exposure indicators

Estimate DiD regression

Conduct price pass-through analysis


# Tools & Software

All analysis is conducted in Python using:

pandas – Data cleaning and merging

numpy – Variable construction

statsmodels – Econometric estimation

matplotlib / plotnine – Visualization

Version control and collaboration via GitHub.


# Limitations

Marginal statistical significance in employment estimates

Limited post-tariff window (COVID-19 prevents clean extension into 2020–2021)

Potential confounding factors (automation, macroeconomic conditions)

Small number of industries analyzed

# Policy Relevance

Tariffs remain a central tool in U.S. trade policy.

Understanding whether the 2018–2019 tariffs:

Increased domestic employment

Raised consumer prices

Produced net welfare gains

is critical for evaluating current and future tariff expansions.

# References

Autor, Dorn, & Hanson (2013). The China Syndrome. American Economic Review.

Flaaen & Pierce (2019). Disentangling the Effects of the 2018–2019 Tariffs. Federal Reserve Board.

Board of Governors of the Federal Reserve System (2025). Detecting Tariff Effects on Consumer Prices in Real Time.
