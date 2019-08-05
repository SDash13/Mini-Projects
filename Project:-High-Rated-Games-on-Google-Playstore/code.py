# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv(path)
data.hist(column="Rating")
plt.show()
data=data[data["Rating"]<=5]
data.hist(column="Rating")
plt.show()
#Code starts here


#Code ends here


# --------------
import pandas as pd



total_null=pd.Series(data.isnull().sum())
percent_null=pd.Series(total_null/data.isnull().count())
missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
print(missing_data)
data.dropna(how='any',inplace=True)
total_null_1=pd.Series(data.isnull().sum())
percent_null_1=pd.Series(total_null/data.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)
print(missing_data_1)



# --------------

#Code starts here

sns.catplot(x="Category",y="Rating",data=data,kind="box",height=10)
plt.xticks(rotation=90)
plt.title("Rating vs Category")

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data["Installs"].value_counts())
data["Installs"]=data["Installs"].str.replace(",","")
data["Installs"]=data["Installs"].str.replace("+","")
data["Installs"]=data["Installs"].apply(int)
le=LabelEncoder()
le.fit(data["Installs"])
data["Installs"]=le.transform(data["Installs"])
sns.regplot(x="Installs", y="Rating", data=data)
plt.title("Rating vs Installs")



# --------------
#Code starts here
print(data["Price"].value_counts())
data["Price"]=data["Price"].str.replace("$","")
data["Price"]=data["Price"].apply(float)
sns.regplot(x="Price",y="Rating",data=data)
plt.title("Rating vs Price")


#Code ends here


# --------------

#Code starts here
def split_data(s):
    return s.split(';')[0]

print(data['Genres'].nunique())

data['Genres'] = data['Genres'].apply(split_data)

gr_mean = data.groupby(['Genres'],as_index=False)['Genres','Rating'].mean()

print(gr_mean.describe())

gr_mean = gr_mean.sort_values(by='Rating')

print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])

#Code ends here


# --------------

#Code starts here
print(data["Last Updated"])
data["Last Updated"]=pd.to_datetime(data["Last Updated"])

max_date=max(data["Last Updated"])
data["Last Updated Days"]=(max_date-data["Last Updated"]).dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title("Rating vs Last Updated ")

#Code ends here


