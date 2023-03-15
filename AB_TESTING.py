#####################################################
# Comparison of Bidding Methods Conversions with AB Test
#####################################################
# Importing required libraries
import pandas as pd

#####################################################
# İş Problemi
#####################################################

#
# teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi veaveragebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchasemetriğine odaklanılmalıdır.




#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç



#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.




#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################

# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

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

# Step 1: Hipotezi tanımlayınız.
# H0: There is no statistically significant difference between the purchase averages of Maximum Bidding and Average Bidding.
# H1:There is a statistically significant difference between the purchase averages of Maximum Bidding and Average Bidding.



# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz
df[["Purchase_control", "Purchase_test"]].mean()

#####################################################
# GÖREV 3: Implementation of Hypothesis Testing
#####################################################


######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.

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



# Adım 2: Selecting and applying the appropriate test according to the Assumption of Normality and Homogeneity of Variance results
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


# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.
# iki teklif verme türü arasında purchase ortalamarı arasında istatistiksel olarak bir fark bulunmadığı için,
# şirket iki teklif türünden maliyet olraak uygun olanını seçebilir.
