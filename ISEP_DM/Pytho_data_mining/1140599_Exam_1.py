import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Pytho_data_mining")
import pandas as pd

# Create a list of names (['NPG','PGC','DBP','TST','SIC','BMI','DPF','AGE','DIA']);
data_headers = ['country', 'country_full', 'sex', 'sex_full', 'age', 'time', 'value']

# 1) (Load) Read ‘Dataset_Population_v02’ file data on python with the column names "data_headers":
population_data = pd.read_csv("Dataset_Population_v02.csv", names=data_headers, index_col=None)
pd.DataFrame(population_data)

# 2) Print the first 10 rows of the dataset:
print(population_data.head(20))  # line 0 to 19 (20 in total)

# 3) Detect missing values:
print("Detect Missing Values:")
print(population_data.isnull().sum())
# Ans: The code above sum's all the NaN (missing values) per column in the dataframe, since all of then
# return zero we can conclude that there are no missing values.
