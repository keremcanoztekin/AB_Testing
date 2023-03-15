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
# AB Testing (Bağımsız İki Örneklem T Testi)
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

# Assign control and test group data to separate variables.
control_df = pd.read_excel("ABTesti/ab_testing.xlsx", sheet_name="Control Group")
test_df = pd.read_excel("ABTesti/ab_testing.xlsx", sheet_name="Test Group")

# Combining control and test group data
control_df.columns = [col + "_control" for col in control_df.columns]
test_df.columns = [col + "_test" for col in test_df.columns]
df = pd.concat([control_df,test_df], axis=1)


#####################################################
# Defining A/B Test Hypothesis
#####################################################

# Step 1: Define the hypothesis.
# H0: There is no statistically significant difference between the purchase averages of Maximum Bidding and Average Bidding.
# H1:There is a statistically significant difference between the purchase averages of Maximum Bidding and Average Bidding.



#####################################################
# GÖREV 3: Implementation of Hypothesis Testing
#####################################################


######################################################
# Assumption Control


# Testing separately whether the control and test group comply with the normality assumption via the Purchase variable.
# Normality Assumption
test_stat, pvalue = shapiro(df["Purchase_control"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

test_stat, pvalue = shapiro(df["Purchase_test"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Variance Homogeneity
test_stat, pvalue = levene(df["Purchase_control"],
                           df["Purchase_test"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


#######################################################
# Selecting and applying the appropriate test according to the Assumption of Normality and Homogeneity of Variance results
######################################################

test_stat, pvalue = ttest_ind(df["Purchase_control"],df["Purchase_test"],
                              equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.

# h0 hipotezimiz reddedilemez, çünkü p value'su 0.05'ten büyük.
# yani bu Bidding yöntemleri satın alım ortalamaları arasında istatistiksel olrak fark yoktur hipotezimiz %95 güvenle fark yoktur.


##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.

# varsayım kontrolleerini tamamladıktan sonra iki kontroldende hipotezimiz red yemediği için
# t test



