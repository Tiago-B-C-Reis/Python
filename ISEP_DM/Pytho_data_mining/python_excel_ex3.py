import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Pytho_data_mining")
import pandas as pd
import numpy as np

# 1.Create a list of names (['NPG','PGC','DBP','TST','SIC','BMI','DPF','AGE','DIA']);
data_headers = ['NPG', 'PGC', 'DBP', 'TST', 'SIC', 'BMI', 'DPF', 'AGE', 'DIA']

# 2.Read ‘pima-indians-diabetes’ file data on python showing the column’s names:
data_diabetes = pd.read_csv("pima-indians-diabetes.csv", names=data_headers, index_col=None)
pd.DataFrame(data_diabetes)

# 3.Print the first 10 rows of the dataset
print(data_diabetes.head(10))

# 4.Print a summary of the data; [Hint: use pandas describe]
pd.set_option('display.max_columns', 9)  # This line allow the describe bellow to show all info (9 is the total columns)
print(data_diabetes.describe())

# 5.Identify the number of rows and columns of the dataframe
print(data_diabetes.shape)

# 6.Identify the datatypes of each column;
print(data_diabetes.dtypes)

# Check how many diabities positive vs negavite exists on the dataset the check the data balance:
print(data_diabetes.groupby('DIA').size())
print(data_diabetes['DIA'].value_counts(normalize=True))

# Detect missing values
print("Detect Missing Values:")
print(data_diabetes.isnull().sum())

# replace the zeros to NaN in all lines from columns 1 to 6:
data_diabetes.iloc[:, 1:6] = data_diabetes.iloc[:, 1:6].replace(0, np.nan)
print(data_diabetes.describe())
