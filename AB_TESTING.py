#####################################################
# Comparison of Bidding Methods Conversions with AB Test
#####################################################
# Importing required libraries
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

######################################################
# Steps of AB Testing 
######################################################

#1. Establish Hypotheses
#2. Assumption Check
# - 1. Normality Assumption (shapiro)
# - 2. Variance Homogeneity (levene)
# 3. Implementation of the Hypothesis
# - 1. Independent two-sample t-test if assumptions are met
# - 2. Mannwhitneyu test if assumptions are not provided
# 4. Interpret results based on p-value

#####################################################
# Data Preparation 
#####################################################

# 1-Assign control and test group data to separate variables.
control_df = pd.read_excel("ABTesti/ab_testing.xlsx", sheet_name="Control Group")
test_df = pd.read_excel("ABTesti/ab_testing.xlsx", sheet_name="Test Group")

# 2-Combining control and test group data
control_df.columns = [col + "_control" for col in control_df.columns]
test_df.columns = [col + "_test" for col in test_df.columns]
df = pd.concat([control_df,test_df], axis=1)

#####################################################
# Defining A/B Test Hypothesis
#####################################################

# Step 1: Define the hypothesis.
# H0: There is no statistically significant difference between the purchase averages of Maximum Bidding and Average Bidding.
# H1:There is a statistically significant difference between the purchase averages of Maximum Bidding and Average Bidding.

######################################################
# Assumption Control
######################################################

# Testing separately whether the control and test group comply with the normality assumption via the Purchase variable.
   # 1-Normality Assumption
test_stat, pvalue = shapiro(df["Purchase_control"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df["Purchase_test"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

   # 2-Variance Homogeneity
test_stat, pvalue = levene(df["Purchase_control"],
                           df["Purchase_test"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

######################################################
# Implementation of Hypothesis Testing
#####################################################

test_stat, pvalue = ttest_ind(df["Purchase_control"],df["Purchase_test"],
                              equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#######################################################
# Analysis of Results
#####################################################
# The H0 hypothesis cannot be rejected because its p-value is greater than 0.05.
# It means that there is no statistically significant difference between the purchasing averages of these Bidding methods.



