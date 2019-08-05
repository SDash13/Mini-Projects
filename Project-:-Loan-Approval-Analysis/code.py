# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include="object")
print(categorical_var)
numerical_var=bank.select_dtypes(include="number")
print(numerical_var)



# code starts here






# code ends here


# --------------
# code starts here
banks=bank.copy()
banks.drop("Loan_ID",inplace=True,axis=1)

b=banks.isnull().sum()
print(b)

bank_mode=banks.mode(axis=1)
banks.fillna("bank_mode",inplace=True)



#code ends here


# --------------
# code starts here

# check the avg_loan_amount
avg_loan_amount = banks.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)


print (avg_loan_amount)
# code ends here


# --------------
# code starts here




loan_approved_se=len(banks[(banks["Self_Employed"] == "Yes") & (banks["Loan_Status"] == "Y")])

percentage_se = (loan_approved_se/614)*100
print(percentage_se)
loan_approved_nse=len(banks[(banks["Self_Employed"] == "No") & (banks["Loan_Status"] == "Y")])
percentage_nse = (loan_approved_nse/614)*100
print(percentage_nse)


# code ends here


# --------------
# code starts here


loan_term= banks["Loan_Amount_Term"].apply(lambda x:int(x) / 12)
big_loan_term=len(loan_term[loan_term >= 25])
print(big_loan_term)

# code ends here


# --------------
# code starts here

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

# Check the mean value 
mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


