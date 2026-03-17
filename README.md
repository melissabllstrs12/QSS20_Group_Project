# Add Graphs, Tables,  fix Methology, and add links to where we got data. As well, as fix the formulas in the methology
# Cost–Benefit Analysis of U.S.–China Tariffs (2018–2019)
Group Members:

- Melissa Ballesteros
- Luis Ortiz Velasquez
- Viviana Perez

# Introduction

In 2018–2019, the United States imposed a series of tariffs on Chinese imports under Section 301, marking the beginning of a major trade conflict between the U.S. and China. These tariffs were justified as a way to:

- Protect domestic manufacturing  
- Restore U.S. jobs  
- Reduce reliance on foreign imports  

However, tariffs also increase costs for firms and consumers and may trigger retaliation from trading partners.

This project evaluates the **cost–benefit tradeoff of tariff protection** by answering the following question:

> Did exposure to tariff protection increase employment in protected industries, and were any gains offset by higher prices?

We focus specifically on industries heavily affected by tariffs — particularly **steel manufacturing** — and examine both:

- Labor market effects  
- Producer price responses
- Number of Transactions of Steel Before and After Tariff


# Research Question

**Our central research question is:**

*How did exposure to the 2018–2019 U.S.–China tariffs affect employment dynamics in import-competing industries, and to what extent were labor market gains offset by price increases?*

**Sub-questions include:**

* Did steel industry employment increase after tariff implementation?
* Were these effects statistically significant?
* Did industries facing greater tariff exposure experience higher producer prices?   

# Data Sources 

### Employment Data

**We use industry-level employment data from:**

1. U.S. Bureau of Labor Statistics (BLS)
2. Quarterly Census of Employment and Wages (QCEW)
    - *Coverage:* 2015–2019
    - *Unit of analysis:* State–Industry–Year

**Key variables:**
- Total employment
- Average weekly wages
- Industry classification (NAICS codes)
- Treatment Industry
- NAICS 331110: Iron and Steel Mills and Ferroalloy Manufacturing

**Control Industry:** *NAICS 331523* (Nonferrous Metal Die-Casting)                                                                                            
 > We construct average annual employment from quarterly values and log-transform employment for interpretation in percentage terms.


### Price Data

**To measure price responses, we use:**
- *Producer Price Index (PPI)* data from the Bureau of Labor Statistics.
> This allows us to test whether tariff-protected industries experienced larger price increases relative to baseline trends.


# Methodology (fix this and edit)
### Difference-in-Differences (DiD) Framework

**We implement a Difference-in-Differences model comparing:**
* Treated industry (steel) & Control industry (non-tariff-affected metal manufacturing)
* Pre-tariff period (2015–2017) & Post-tariff period (2019)
* **Regression specification:**
  
$$
\log(Employment_{it}) =
\beta_0 +
\beta_1 Treated_i +
\beta_2 Post_t +
\beta_3 (Treated_i \times Post_t) +
\gamma_i +
\delta_t +
\epsilon_{it}
$$

**Where:**
- $\beta_3$ captures the causal effect of tariff exposure.
- $\gamma_i$ represents industry fixed effects.
- $\delta_t$ represents year fixed effects.

### Price Change Measurement
* Statistically significant increases in producer prices
* Evidence of tariff pass-through
*This evaluates whether consumers and downstream firms bore the cost of protection.*

We calculate the change in steel prices relative to a baseline period using the Producer Price Index (PPI):

$$
Price_t =
\beta_0 + 
\beta_1 TariffPost_t + 
\beta_2 Trend_t + 
\varepsilon_t
$$

**Where:**

- 𝑡 represents the indexes months
- $TariffPost_t$ is n indicator for the post-tariff period
- $\beta_1$ measures the immediate change in steel prices associated with the tariff
- $\beta_1$ controls for the underlying trend


### Monthly Aggregation of Steel Purchases
To analyze purchasing behavior surrounding tariff implementation, we aggregate steel transaction quantities to the monthly level:

$$
Q_m = 
\sum_{i=1}^{n_m} q_i
$$

**Where:**

- $Q_m$ = total quantity of steel purchased in month \(m\)  
- $q_i$ = quantity purchased in transaction \(i\)
- $n_m$ = number of transactions in month \(m\)

This aggregation produces a monthly time series of steel demand, which we use to visualize trends before and after tariff implementation.


### Summary Statistics of Steel 

In addition to time-series visualization, we construct a summary table of steel purchasing activity

$$
Q_{period} =
\frac{1}{T} 
\sum_{t=1}^{T} Q_t
$$

**Where:**

- $Q_{period}$ = average monthly steel purchases within a given period
- $Q_t$ = total quantity purchased in month 𝑡

- $T$ = number of months in the period

**We compute these statistics separately for:**
- Pre-tariff period
- Post-tariff period

This allows us to compare average purchasing levels and identify whether firms adjusted demand following tariff implementation.

# Results (Preliminary)

### Employment Effects
- **Estimated employment increase in steel: ~12.5%**
- **Marginal statistical significance (p ≈ 0.097)**

**Interpretation:**
- Suggestive evidence of **employment gains**
- **NOT** strong enough to conclusively attribute gains solely to tariffs



### Price Effects

Steel producer prices increased following tariff implementation.

**Consistent with previous research, our results suggest:**
- Tariff costs were largely passed through to U.S. buyers
- Foreign exporters did not fully absorb tariff costs



### Steel Purchasing Behavior

**Our analysis of steel transaction quantities shows:**
- Substantial increase in steel purchases prior to tariff implementation
- Slight decline in purchasing after tariffs took effect

**Interpretation:**
**This pattern may indicate:**
- Pre-tariff stockpiling behavior by firms
- Reduced demand following price increases.

**Existing Federal Reserve research suggests:**

    a. Tariffs were largely passed through to U.S. prices

    b. Foreign exporters did not fully absorb the costs


# Data Pipeline

1. Download yearly QCEW datasets (2015–2019)
2. Filter for treatment and control NAICS industries
3. Compute annual average employment
4. Create treatment and post indicators
5. Log-transform employment
6. Estimate Difference-in-Differences regression
7. Download Producer Price Index (PPI) data for steel
8. Calculate price changes relative to baseline
9. Aggregate steel transaction quantities by month
10. Compare purchasing patterns before and after tariff implementation


# Tools & Software
**All analysis is conducted in Python using:**
- pandas – Data cleaning and merging
- numpy – Variable construction
- statsmodels – Econometric estimation
- matplotlib / plotnine – Visualization

> Version control and collaboration via GitHub.

# Repository Structure

```
.
├── data/
│   ├── steel_prices/
│   └── qcew_employment/
│
├── figures/
│   ├── steel_price_trends.png
│   └── steel_transaction_quantities.png
│
├── notebooks/
│   ├── employment_did_analysis.ipynb
│   └── steel_transaction_analysis.ipynb
│
└── README.md
```
# Limitations

  **I.** Marginal statistical significance in employment estimates
  
  **II.** Limited post-tariff window (COVID-19 prevents clean extension into 2020–2021)
  
  **III.** Potential confounding factors (automation, macroeconomic conditions)
  
  **IV.** Small number of industries analyzed

# Policy Relevance

> Tariffs remain a central tool in U.S. trade policy.

**Understanding whether the 2018–2019 tariffs:**

- Increased domestic employment
- Raised consumer prices
- Produced net welfare gains

is **critical** for evaluating the net economic effects of protectionist trade policy.

# References

Autor, David H., David Dorn, and Gordon H. Hanson. 2013. “The China Syndrome: Local
Labor Market Effects of Import Competition in the United States.” American Economic
Review 103(6), p. 2121–68. [[Link]](https://www.aeaweb.org/articles?id=10.1257/aer.103.6.2121)

Flaaen, Aaron, and Justin Pierce. 2019. “Disentangling the Effects of the 2018–2019
Tariffs on a Globally Connected U.S. Manufacturing Sector.” Technical Report 2019-086,
Board of Governors of the Federal Reserve System, Washington, DC. [[Link]](https://doi.org/10.17016/FEDS.2019.086)

Minton, Robert, and Mariano Somale (2025). "Detecting Tariff Effects on Consumer Prices in 
Real Time," FEDS Notes. Washington: Board of Governors of the Federal Reserve System, May 09, 2025, 
[[Link]](https://doi.org/10.17016/2380-7172.3786)
