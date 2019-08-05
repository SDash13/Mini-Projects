# --------------
import pandas as pd
from sklearn import preprocessing

#path : File path

# Code starts here
dataset=pd.read_csv(path)
print(dataset.head())
dataset.drop(columns=["Id"],axis=1,inplace=True)
dataset.describe()

# read the dataset



# look at the first five columns


# Check if there's any column which is not useful and remove it like the column id


# check the statistical description



# --------------
import seaborn as sns
from matplotlib import pyplot as plt
cols=dataset.columns
x=dataset["Cover_Type"]
y=dataset.drop(columns=["Cover_Type"],axis=1)
size=len(x)
sns.violinplot(x="Cover_Type",data=dataset)



# --------------
import numpy
upper_threshold = 0.5
lower_threshold = -0.5


# Code Starts Here
subset_train=dataset.iloc[:,:10]
data_corr=subset_train.corr(method='pearson')
sns.heatmap(data_corr)
correlation=data_corr.unstack().sort_values(kind='quicksort')
corr_var_list=correlation[((correlation> upper_threshold) | (correlation < lower_threshold)) & ((correlation != 1))]


# Code ends here




# --------------
#Import libraries 
from sklearn import cross_validation
from sklearn.preprocessing import StandardScaler

# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)

r,c = dataset.shape
X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]

# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)



#Standardized

scaler = StandardScaler()

#Apply transform only for non-categorical data
X_train_temp = scaler.fit_transform(X_train.iloc[:,:10])
X_test_temp = scaler.transform(X_test.iloc[:,:10])

#Concatenate non-categorical data and categorical
X_train1 = numpy.concatenate((X_train_temp,X_train.iloc[:,10:c-1]),axis=1)
X_test1 = numpy.concatenate((X_test_temp,X_test.iloc[:,10:c-1]),axis=1)

scaled_features_train_df = pd.DataFrame(X_train1, index=X_train.index, columns=X_train.columns)
scaled_features_test_df = pd.DataFrame(X_test1, index=X_test.index, columns=X_test.columns)


# --------------
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif


# Write your solution here:

# Code starts here
skb = SelectPercentile(score_func=f_classif,percentile=20)
predictors = skb.fit_transform(X_train1, Y_train)
scores = list(skb.scores_)

Features = scaled_features_train_df.columns

dataframe = pd.DataFrame({'Features':Features,'Scores':scores})

dataframe=dataframe.sort_values(by='Scores',ascending=False)

top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])

print(top_k_predictors)

# Code Ends here


# --------------
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score
clf = OneVsRestClassifier(LogisticRegression())
clf1=OneVsRestClassifier(LogisticRegression())
model_fit_all_features =clf.fit(X_train , Y_train)
predictions_all_features=clf.predict(X_test)

score_all_features= accuracy_score(Y_test,predictions_all_features )

print(scaled_features_train_df.columns[skb.get_support()])

X_new = scaled_features_train_df.loc[:,skb.get_support()]
X_test_new=scaled_features_test_df.loc[:,skb.get_support()]

model_fit_top_features  =clf1.fit(X_new , Y_train)
predictions_top_features=clf1.predict(X_test_new)

score_top_features= accuracy_score(Y_test,predictions_top_features )


