# A/B Testing

<img src="https://user-images.githubusercontent.com/103461795/225143063-07e98e6d-cf4e-48ec-ae0e-87fb7ce1ac28.png" width="500">

## 💼Business Problem
Recently, Facebook introduced a new bidding type called average bidding as an alternative to the maximum bidding. One of our clients, company X, has decided to test this new feature and wants to understand if average bidding generates more conversions than maximum bidding through an A/B test. The A/B test has been running for a month, and X company now expects you to analyze the results of this A/B test. The ultimate success metric for X company is Purchase. Therefore, the Purchase metric should be the focus of statistical testing.
## 📊 Dataset Story
This dataset contains information about a company's website, including the number of ad impressions and clicks that users see and click, as well as revenue data from these interactions. There are two separate datasets, one for the Control group and one for the Test group. These datasets are included on separate sheets in the Excel file **ab_testing.xlsx**. The Maximum Bidding was applied to the Control group, and the Average Bidding was applied to the Test group.

## 📌 Variables
✶**Impression:** Ad views

✶**Click:** Number of clicks on the displayed ad

✶**Purchase:** Number of products purchased after ads clicked

✶**Earning:** Earnings after purchased products

## 📉Hypothesis Test Steps
   📋 **Analysis Plan: Two-Sample Hypothesis Test**

🔍 **Step 1: Formulate Hypotheses**

   &#8226; H0: There is no significant difference between the two samples.
 
   &#8226; H1: There is a significant difference between the two samples.
 
📊 **Step 2: Assumption Check**

     1️⃣ Normality assumption: Use Shapiro-Wilk test to check normality assumption of the sample distributions.

     2️⃣ Homogeneity of variance: Use Levene's test to check if variances of the samples are equal.

🔍 **Step 3: Implementation of the Hypothesis Test**

     1️⃣ If assumptions are met, use the independent two-sample t-test.

     2️⃣ If assumptions are not met, use the Mann-Whitney U test.

📈 **Step 4: Interpret the Results Based on the p-value**

If the p value is less than the significance level (0.05), reject the null hypothesis and it is concluded that there is a significant difference between the two samples. If the p-value is greater than the significance level (0.05), it cannot reject the null hypothesis and it is concluded that there is no significant difference between the two samples.
