<<<<<<< HEAD
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

# Methodology
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

### Price Pass-Through Analysis

**We examine whether industries exposed to tariffs experienced:**
* Statistically significant increases in producer prices
* Evidence of tariff pass-through
  
*This evaluates whether consumers and downstream firms bore the cost of protection.*


# Results (Preliminary)

### Employment Effects
- **Estimated employment increase in steel: ~12.5%**
- **Marginal statistical significance (p ≈ 0.097)**

### Interpretation:
- Suggestive evidence of **employment gains**
- **NOT** strong enough to conclusively attribute gains solely to tariffs

# Price Effects

**Existing Federal Reserve research suggests:**

    a. Tariffs were largely passed through to U.S. prices

    b. Foreign exporters did not fully absorb the costs

Our project evaluates this mechanism at the industry level using PPI data.


# Data Pipeline

  1. Download yearly **QCEW datasets** (2015–2019)
  2. Filter for **treatment** and **control** *NAICS* code
  3. Compute annual **average** employment
  4. Create **treatment** and **post** indicators
  5. Log-transform employment
  6. Merge with tariff exposure indicators
  7. Estimate *DiD* regression
  8. Conduct price pass-through analysis


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
├── v-Steel.data/          Code used to analyze Steel price
├── STEEL_PRICE_rebased/   Datasets containing Steel Prices
└── README.md              Project overview and documentation
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

is **critical** for evaluating current and future *tariff expansions*

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
=======
# QSS20_Group_Project
Group A5
Luis Ortiz Velasquez
Melissa Ballesteros 
Viviana Perez 

Introduction
U.S.–China tariffs have broad implications for economic growth, international trade partnerships, labor markets, and overall quality of life. Understanding whether the economic benefits to domestic producers and investors outweigh the costs borne by consumers or workers is essential for evaluating the overall effectiveness and welfare consequences of tariff policy. Therefore, our group analyzes how exposure to tariff protection affects employment dynamics in import-competing industries such as steel while also measuring the extent to which labor market gains may be offset by price increases felt by consumers in those same sectors. Specifically, we ask: \textbf{Did the 2018–2019 U.S.–China tariffs increase domestic employment in protected industries, and were these gains offset by higher consumer prices?}

Our group focuses on the three industries most impacted by the U.S.–China tariffs, steel, ; because, this sectors faced some of the highest tariff rates and were among the earliest and most prominently targeted industry under the Trump administration’s trade policy. We use employment data from the U.S. Bureau of Labor Statistics’ Quarterly Census of Employment and Wages (QCEW), which provides detailed industry-level employment statistics on a quarterly and annual basis. To determine whether the tariff hikes implemented during 2018–2019 affected domestic employment levels in these sectors, we compare employment trends from 2015 through the end of 2019, allowing us to observe both pre-tariff and post-tariff patterns. By examining changes before and after the policy implementation, and comparing trends within the targeted industries to their prior baselines, we aim to isolate the measurable effects of tariff protection on domestic employment.

Methods
Clumping + Thresholding (C+T) (PLINK 2)
Batch Screening Iterative Lasso (BASIL)
Bayesian Multiple Regression (BayesR)
Hypothesis
Since Clumping + Thresholding does not directly model the additive effects of the contribution from multiple SNPs, we expect that C+T would perform the worst when the number of causal SNPs increases.
Both BASIL and BayesR should be better at capturing additive effects from many SNPs, while shrinkage-based method might incorrectly shrink some effects to zero.
Consider heritability model of the form (Speed, Holmes, and Balding 2020) 
E
[
h
j
2
]
=
∑
j
w
j
[
f
j
(
1
−
f
j
)
]
(
1
+
α
)
,
 where 
w
j
 is the weight for SNP 
j
 and 
f
j
 is its minor allele frequency (MAF). For simplicity, we assume that weight 
w
j
 is a constant.

When 
α
=
−
1
, the expected heritability reduces to 
∑
j
w
j
. SNPs have linear effect on heritability, regardless of minor allele frequency. Since this data generating process is closer to Lasso, we expect BASIL to perform better under this regime.
When 
α
=
−
0.25
, the expected heritability becomes 
∑
j
w
j
[
f
j
(
1
−
f
j
)
]
0.75
. SNPs that are more common would have higher contribution to heritability. We expect BayesR would capture this nonlinear relationship better than Lasso based BASIL.
The current published papers comparing these methods have mixed findings. Most of them either only use simulated genotypes, simulate phenotypes on a narrow demography (Lloyd-Jones et al. 2019; Qian et al. 2020), or does not systematically evaluate alternative scenarios (Ding et al. 2023). To our knowledge, this is the first systematic comparison on real genomic data across ancestries/populations.

Directory for Data Storage and Computation
We are analyzing real genome data from 1000 Genomes Project Phase Three call set on GRCh37. Since the size of the data is huge, for the ease of data storage and collaborating, we store our data on Google Drive and use Google Colab for compute (by reading/copying files directly from Google Drive).

Notes: We have updated the related notebooks and the data of calculation results on GitHub. However, due to the large size of other raw data, we have only placed it on Google Drive.
Here is the link to our Google Drive project folder.

GitHub Directory:

.
├── notebook                   ← Codes and scripts
├── data
│   ├── BASIL/chr19_ldl_pheno  ← Results of BASIL
│   ├── BayesR/chr19_ldl_pheno ← Results of BayesR
│   ├── CT/chr19_ldl_pheno     ← Results of C+T
│   ├── chr19_ldl_pheno        ← Simulated phenotypes
│   └── split_ids              ← Sample splitting (train, val, test)
│       ├── by_population
│       └── by_superpopulation 
└── figure                     ← Analysis and graphs
Part of the files in Google Drive Project are organized as follows:

/CSE-284-Final-Project/
├── data
│   ├── 1000g_by_superpopulation ← Genome (all autosomes) split by superpopulation
│   │   ├── AFR_{train,val,test}.{bed,bim,fam,pgen,pvar.zst,psam}
│   │   ⋮    ⋮
│   │   └── SAS_{train,val,test}.{bed,bim,fam,pgen,pvar.zst,psam}
│   ├── 1000g_by_population ← Genome (all autosomes) split by perpopulation
│   │   ├── ACB_all.{bed,bim,fam,pgen,pvar.zst,psam}
│   │   ⋮    ⋮
│   │   └── YRI_all.{bed,bim,fam,pgen,pvar.zst,psam}
│   ├── 1000g_combined ← Genome (all autosomes) 
│   │   └── 1000g.{bed,bim,fam,pgen,pvar.zst,psam}
│   ├── 1000g_raw_combined ← Raw genome before cleaning and quality control
│   │   ├── all_phase3.{pgen.zst,pvar.zst}
│   │   ├── phase3_corrected.psam
│   │   ├── raw.{bed,bim,fam}
│   │   └── clean.{bed,bim,fam}
│   ├── 1000g_pheno ← Simulated phenotype by parameters
│   │   └── power={-1,-0.25}_her={0.1,0.3,0.5,0.7,0.9}_num-causals={1,10,100,1000,10000}.phen
│   ├── igsr_samples.tsv ← Reference table for population and sex information
│   ├── split_samples.csv ← Reference table for sample splitting
│   ├── split_ids ← Ids after sample splitting (for `--keep`)
│   │   ├── by_superpopulation
│   │   └── by_population
│   └── test_data ← Genome and phenotype data for benchmark (from PS4)
│       ├── CEU_chr19_normed.{bed,bim,fam,pgen,pvar.zst,psam}
│       ├── GBR_chr19_normed.{bed,bim,fam,pgen,pvar.zst,psam}
│       └── kgvcf_ldl.{phe,phen,pheno}
└── notebook ← Data processing and analysis
    ├── 00_download_1000genome_data_and_simulate_phenotypes.ipynb
    ├── 01_convert_to_pgen.ipynb
    ├── 02_convert_to_bed.ipynb
    ├── 04_split_train_val_test.ipynb
    ├── 05_simulate_phenotype.ipynb
    ├── 06_update_phenotype_format.ipynb
    ├── 07_convert_chr19.ipynb
    ├── 08_LDAK_chr19_pheno_simulation.ipynb
    ├── 09_test_GCTA_pheno_simulation.ipynb
    ├── 11_test_snpnet.ipynb
    ├── 12_test_GCTB.ipynb
    ├── 13_test_C+T.ipynb
    ├── 21_1000g_snpnet.ipynb
    ├── 22_1000g_GCTB.ipynb
    ├── 23_1000g_CT_population.ipynb
    ├── 24_CT_test_PS4.ipynb
    ├── 31_snpnet_superpopulation.ipynb
    ├── 32_GCTB_superpopulation.ipynb
    ├── 33_CT_superpopulation.ipynb
    ├── 34_CT_population.ipynb
    ├── 41_chr19_prs_by_superpopulation_check_progress.ipynb
    ├── 42_chr19_prs_by_superpopulation_analysis.Rmd
    ├── 42_chr19_prs_by_superpopulation_analysis.html
    ├── 42_chr19_prs_by_superpopulation_analysis.md
    └── 43_analysis.ipynb
File naming of notebook directory
0x: Data Preprocessing
1x: Model testing
2x: Run models on all autosomes
3x: Run models on Chr 19 only (final setting)
4x: Results and analysis
Data Preprocessing
Genotypes (1000 Genomes) image
Goal: get the dataset of all autosomes from 1000 Genomes with quality control
Tool: PLINK 1.9 and PLINK 2.0
Data Quality Control
--maf 0.01 --snps-only just-acgt --max-alleles 2 --rm-dup exclude-all
Convert to binary formats for different packages
For BASIL/snpnet: --make-pgen generates .pgen .pvar .psam
For BayesR/GCTB: --make-bed generates .bed .bim .fam
Dataset
Raw data: data/1000g_raw_combined/
Cleaned data: data/1000g_combined/
Split by Population: data/1000g_by_population/
Split by Super-population: data/1000g_by_superpopulation/
Reference: https://dougspeed.com/1000-genomes-project/


(Number of Samples from Each Superpopulation on 1000 Genomes Project Phase 3 Dataset)

Phenotypes (Simulation) image
Goal: simulate phenotypes with different settings
Tool: LDAK
Options
--make-phenos: perform simulation
--power (
α
) : specify how predictors are scaled
Diffirent from the power mentioned in the class that indicates the probability we can detect an association at the desired significance level, given that there is actually an association.
--her: heritability describes how much variation in the phenotype is described by genetics.
--num-phenos: the number of phenotypes to generate.
--num-causals: the number of predictors contributing to each phenotype.
 --causals <causalsfile>: specify which predictors are causal for each phenotype.
 --effects <effectsfile>: specify the effect sizes in a file.
Our simulation settings
Number of Phenotypes: 20
Power: {-0.25, -1}
Notes: GCTA Model with power of -1 vs. Human Default Model with power of -0.25
Heritability: {0.1, 0.3, 0.5, 0.7, 0.9}
Number of causal SNPs = {1, 10, 100, 250, 512}
Total combinations: 2 * 5 * 5 = 50
File naming: power=x_her=y_num-causals=z.pheno
Columns: FID, IID, PHEN1, PHEN2, PHEN3, ...
Notes: At first, we didn't specify the <causalsfile> and <effectsfile>. By default, LDAK will pick causal predictors at random and sample effect sizes from a standard normal distribution. However, the results of PRS using randomly selected causal SNPs and effect sizes are horrible (
R
2
 of testing data close to 
0
). Therefore, we adopted the ldl_prs.txt data from UCSD CSE 284 PRS Activity, which is the LDL PRS data from this paper and its publicly available data. Also, since there are 512 SNPs on Chromosome 19 listed in ldl_prs.txt, the maximal number of causal SNPs is 512.
Dataset
data/chr19_ldl_pheno/
Reference: https://dougspeed.com/simulations/
Sample Splitting image
We randomly select samples from each superpopulation into 70% training, 15% validation, and 15% test sets, while keeping each set has balanced number of samples from each population and sex.
Dataset
data/split_ids/
by_population/
by_superpopulation/
Details
P
R
S
i
=
∑
j
∈
S
β
j
X
i
j

C+T image
Tool: PLINK 2.0
Reference: UCSD CSE 284 Week 6 Lecture Slides, PS3, and PS4
Perform a GWAS to estimate per-variant effect sizes (
β
's)
--linear --maf 0.05 
Y
=
β
j
X
j
+
ϵ
Perform LD clumping (pruning) to get an independent set of SNPs
--clump gwas.assoc.linear
--clump-p1 0.0001: significance threshold for index SNPs
--clump-r2 0.1: LD threshold for clumping
–clump-kb 250: physical distance threshold for clumping
Choose all SNPs with 
p
-value less than the threshold 
T
Computer PRS and evalueate accuracy (
R
2
)
--score
Computer final PRS with optimal 
T
 and evaluate on a separate testing dataset
Repeat steps 2-4 to find out which 
T
 work the best (validation dataset)
Notes: When running C+T for AMR (superpopulation) dataset from 1000 Genomes, we encountered a problem that PLINK 2.0 will not run the --score command when there are less than 50 samples. Since there are not enough samples for validation data. We choose the best p value threhold 
T
 in the training data as the 
T
 for testing data. Thus, the performance may be underrated.
BASIL image
Minimize
∑
i
(
y
i
−
y
^
i
)
2
+
λ
∑
j
|
β
^
j
|

Tool: snpnet
Reference: Vignette of the snpnet R package by Junyang Qian and Trevor Hastie
(Already preprocessed) convert genotypes to .pgen
Train snpnet() model, get fit_snpnet object in R
niter = 100 controls the number of iterations
use.glmnetPlus = TRUE recommended for faster computation
Predict phenotype using predict_snpnet(), get pred_snpnet object
fit = fit_snpnet to use the fitted model
new_genotype_file to test on test set
Evaluate 
R
2
 in pred_snpnet$metric
BayesR image
Tool: GCTB
Reference: Tutorial: Practical 4 Bayesian methods for genomic prediction by GCTB package maintainer Jian Zeng
(Already preprocessed) convert genotypes to .bed
Train BayesR model
--chain-length 10000 controls total length of Markov Chain
--burn-in 2000 controls number of burn-ins
Get posterior effects for each SNP in .snpRes format
Send .snpRes to plink for scoring of PRS scores
Calculate 
R
2
 against the ground truth
Experiments
All autosomes with Random Effect Sizes
R
2
 of testing data close to 
0
 🥲
Probably because there are not enough samples to model the complicated relaitonships between variants and phenotypes.
Chr 19 with Random Effect Sizes
R
2
 of testing data close to 
0
 🥲
Probably because there are not enough samples to model the complicated relaitonships between variants and phenotypes.
Chr 19 with Fixed Effect Sizes
It works 😃
Superpopulation: {'AFR', 'AMR', 'EAS', 'EUR', 'SAS'}
Power: {-0.25, -1}
Heritability: {0.1, 0.3, 0.5, 0.7, 0.9}
Number of causal SNPs = {1, 10, 100, 250, 512}
Output files
combined_predict_{superpopulation}_power={power}_her={heritability}_num-causals={number of causal SNPs}_pheno={number of phenotypes}.csv
Columns: IID, Predicted Phenotype, Actual Phenotype, Phenotype Index
combined_result_{superpopulation}_power={power}_her={heritability}_num-causals={number of causal SNPs}_pheno={number of phenotypes}.csv
Columns: Superpopulation, Power, Heritability, Number of Causal SNPs, Phenotype Index, Training 
R
2
, Validation 
R
2
, Testing 
R
2
Evaluation
R
2
 (coefficient of determination) on the testing dataset in the context of GWAS and PRS provides a measure of how well a polygenic risk score can predict (true) phenotypes.
Results on Benchmark
As a proof of concept and testing of data/input requirements for different software packages, we use/transform data from PS4:

Genotype CEU_chr19_normed.{vcf,bed,pgen} is used as training set
Genotype GBR_chr19_normed.{vcf,bed,pgen} is used as test set
Phenotype kgvcf_ldl.{phen,pgeno} is used as ground truth phenotype
Method	Training 
R
2
Testing 
R
2
C+T	0.98	0.64
BASIL/snpnet	0.99	0.65
BayesR/GCTB	0.99	0.89
Table above reports the training and test set performance across the three methods. All three methods overfit on their own dataset. C+T and BASIL achieve similar performance on test set, while BayesR performs much better on the test set.

Results








For more results and the code for replicating the figures, see notebook/42_chr19_prs_by_superpopulation_analysis.Rmd

Discussions
Challenges and limitations
PLINK 1.9 and PLINK 2.0 have different input formats and modifiers. This makes data preparation and preprocessing taking a huge chunk of time. In this project, we prioritize using PLINK 2.0 since PLINK 2.0 runs faster than PLINK 1.9 in most cases, and only switch to PLINK 1.9 when PLINK 2.0 fails to accomplish what we expect or require significant modifications.
The number of samples of each superpopulation from 1000 Genomes Project vary a lot. Therefore, the comparison results across superpopulations may not be representative.
Future Work
Different distributions of effect sizes and causal SNPs from different traits.

Related Work
Frank Dudbridge (2013) provided a comprehensive overview of the power and predictive accuracy of PRS, highlighting the statistical principles underpinning these methods and their implications for disease risk prediction.
Federal Reserve System, “Disentangling the Effects of the 2018–2019 Tariffs on a Globally Connected U.S. Manufacturing Sector,”}  \cite{flaaen_pierce_2019} analyzes manufacturing activity using macro-level data and productivity measures. While this study evaluates broader manufacturing performance during the tariff period, it does not directly isolate the employment effects of tariff protection within specific targeted industries. Other Federal Reserve research has found that U.S. import tariffs implemented in 2018–19 led to statistically significant increases in consumer goods prices, with tariff pass-through occurring quickly and contributing to higher personal consumption expenditure prices, indicating that tariffs are transmitted to consumer prices rather than being fully absorbed by foreign exporters \cite{federalreserve_2025_tariff_prices}. Similarly, \textit{The China Syndrome: Local Labor Market Effects of Import Competition in the United States} by David Autor, David Dorn, and Gordon Hanson examines the labor market consequences of increased Chinese import competition \cite{aer.103.6.2121}. Using econometric causal inference methods, the authors find that greater exposure to Chinese imports led to significant declines in U.S. manufacturing employment. However, their analysis focuses on the negative employment effects of import competition rather than evaluating whether subsequent tariffs successfully restored manufacturing jobs. In contrast to this prior work, our project directly investigates whether the 2018–2019 U.S.–China tariffs increased employment in the steel industry. By using industry-level employment data and focusing on pre- and post-tariff trends, we contribute to the literature by examining whether tariff protection generated measurable labor market gains in the sector it was intended to help. 

References
Dudbridge F. (2013) Power and Predictive Accuracy of Polygenic Risk Scores. PLOS Genetics 9(3): e1003348. https://doi.org/10.1371/journal.pgen.1003348
The 1000 Genomes Project Consortium. (2015) A global reference for human genetic variation. Nature 526, 68–74 https://doi.org/10.1038/nature15393
Vilhjálmsson, B. J., Yang, J., Finucane, H. K. et al. (2015) Modeling Linkage Disequilibrium Increases Accuracy of Polygenic Risk Scores. American journal of human genetics. 97(4), 576–592. https://doi.org/10.1016/j.ajhg.2015.09.001
Khera, A.V., Chaffin, M., Aragam, K.G. et al. (2018) Genome-wide polygenic scores for common diseases identify individuals with risk equivalent to monogenic mutations. Nat Genet 50, 1219–1224. https://doi.org/10.1038/s41588-018-0183-z
Lloyd-Jones, L.R., Zeng, J., Sidorenko, J. et al. (2019) Improved polygenic prediction by Bayesian multiple regression on summary statistics. Nat Commun 10, 5086. https://doi.org/10.1038/s41467-019-12653-0
Ge, T., Chen, CY., Ni, Y. et al. (2019) Polygenic prediction via Bayesian regression and continuous shrinkage priors. Nat Commun 10, 1776. https://doi.org/10.1038/s41467-019-09718-5
Speed, D., Holmes, J. & Balding, D.J. (2020) Evaluating and improving heritability models using summary statistics. Nat Genet 52, 458–462. https://doi.org/10.1038/s41588-020-0600-y
Qian J, Tanigawa Y, Du W, Aguirre M, Chang C, Tibshirani R, et al. (2020) A fast and scalable framework for large-scale and ultrahigh-dimensional sparse regression with application to the UK Biobank. PLoS Genet 16(10): e1009141. https://doi.org/10.1371/journal.pgen.1009141
Ding, Y., Hou, K., Xu, Z. et al. (2023) Polygenic scoring accuracy varies across the genetic ancestry continuum. Nature 618, 774–781. https://doi.org/10.1038/s41586-023-06079-4
UCSD CSE 284 Lecture Slides and Problem Sets
>>>>>>> 8b4c55d (Update the Repo)
