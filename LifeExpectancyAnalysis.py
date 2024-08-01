
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.stats import linregress

# Has life expectancy increased over time in the six nations?
# Has GDP increased over time in the six nations?
# Is there a correlation between GDP and life expectancy of a country?
# What is the average life expectancy in these nations?
# What is the distribution of that life expectancy?

df = pd.read_csv('all_data.csv')

print(df.head())
print(df.dtypes)
df = df.rename(columns={"Life expectancy at birth (years)":"Life Expectancy"})



#Life Expectancy vs. Time
count = 1
plt.figure(figsize=(14,16))
plt.xticks([])
plt.yticks([])
plt.title("Life Expectancy vs Year")

for country in df.Country.unique():
    plt.subplot(3,2,count)
    dfT = df[df.Country == country]
    plt.scatter(dfT["Year"],dfT["Life Expectancy"],label="Measured Data")
    line = linregress(dfT["Year"],dfT["Life Expectancy"])
    slope = line.slope
    intercept = line.intercept
    plt.plot(dfT["Year"],slope*dfT["Year"]+intercept,label="Fitted line",linestyle="dashed")
    plt.xlabel("Year")
    plt.xticks([2000,2002,2004,2006,2008,2010,2012,2014])
    plt.ylabel("Life Expectancy (yrs)")
    plt.legend(loc="best")
    plt.title(country)
    count+=1
    print("The correlation coefficient, for a linear regression, of life Expectancy vs Year in " + country + " is " +str(pearsonr(dfT["Year"],dfT["Life Expectancy"])[0]))
plt.show()
plt.clf()
print("\n")

#GDP vs. Time
count = 1
plt.figure(figsize=(14,16))
plt.xticks([])
plt.yticks([])
plt.title("GDP vs Year")
for country in df.Country.unique():
    plt.subplot(3,2,count)
    dfT = df[df.Country == country]
    plt.scatter(dfT["Year"],dfT["GDP"],label="Measured Data",)
    line = linregress(dfT["Year"], dfT["GDP"])
    slope = line.slope
    intercept = line.intercept
    plt.plot(dfT["Year"], slope * dfT["Year"] + intercept,label="Fitted line",linestyle="dashed")
    plt.xlabel("Year")
    plt.ylabel("GDP ($)")
    plt.legend(loc="best")
    plt.title(country)
    count+=1
    print(
        "The correlation coefficient, for a linear regression, of GDP vs Year in " + country + " is " + str(
            pearsonr(dfT["Year"], dfT["GDP"])[0]))
plt.show()
plt.clf()
print("\n")
# GDP and Life Expectancy
count = 1
plt.figure(figsize=(14,16))
plt.xticks([])
plt.yticks([])
plt.title("Life Expectancy vs GDP")
for country in df.Country.unique():
    plt.subplot(3,2,count)
    dfT = df[df.Country == country]
    plt.scatter(dfT["GDP"],dfT["Life Expectancy"],label="Measured Data")
    line = linregress(dfT["GDP"], dfT["Life Expectancy"])
    slope = line.slope
    intercept = line.intercept
    plt.plot(dfT["GDP"], slope * dfT["GDP"] + intercept,label="Fitted line",linestyle="dashed")
    plt.xlabel("GDP ($)")
    plt.ylabel("Life Expectancy (yrs)")
    plt.title(country)
    plt.legend(loc="best")
    count+=1
    print(
        "The correlation coefficient, for a linear regression, of life Expectancy vs GDP in " + country + " is " + str(
            pearsonr(dfT["GDP"], dfT["Life Expectancy"])[0]))
plt.show()
plt.clf()
print("\n")
#Average Life expectancy in these nations

mean = np.mean(df["Life Expectancy"])
meanChile = np.mean(df["Life Expectancy"][df.Country == "Chile"])
meanChina = np.mean(df["Life Expectancy"][df.Country == "China"])
meanUS = np.mean(df["Life Expectancy"][df.Country == "United States of America"])
meanGermany = np.mean(df["Life Expectancy"][df.Country == "Germany"])
meanMexico = np.mean(df["Life Expectancy"][df.Country == "Mexico"])
meanZimbabwe = np.mean(df["Life Expectancy"][df.Country == "Zimbabwe"])

print(mean)
print(meanChile)
print(meanChina)
print(meanUS)
print(meanGermany)
print(meanMexico)
print(meanZimbabwe)



#Distribution life expectancy in these nations.

count = 1
plt.figure(figsize=(14,16))
plt.xticks([])
plt.yticks([])
plt.title("Distribution of Life Expectancy")
for country in df.Country.unique():
    plt.subplot(3,2,count)
    dfT = df[df.Country == country]
    plt.hist(dfT["Life Expectancy"])
    plt.title(country)
    count+=1
    plt.xlabel("Life Expectancy (yrs)")
    plt.ylabel("Count")
plt.show()
plt.clf()

plt.hist(df["Life Expectancy"])
plt.xlabel("Life Expectancy (yrs)")
plt.ylabel("Count")
plt.title("Life Expectancy Distribution")
plt.show()
plt.clf()