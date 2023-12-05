import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Pytho_data_mining")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn


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


# Se eu quiser substituir não apenas o 0 mas todos os valores menores que x?
data_diabetes.loc[data_diabetes["PGC"] < 100, "PGC"] = np.nan
# df.loc[linhas, colunas] portanto linhas=data["PGC"]< 100
# ie, todas as linhas onde PGC é menor que 100, e só altera a coluna PGC


# View the data in a box plot from matplotlib: (creates a .png on the path defined on the 'os')
data_diabetes.plot.box(figsize=(6, 6))  # tuple with dimensions of the figure
plt.savefig('box_plot.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()


# DATA NORMALIZATION: (min-max feature scaling)
# 1- Copy the data
data_diabetes_mm_normalized = data_diabetes.copy()
# 2- Apply normalization techniques
data_diabetes_mm_normalized = ((data_diabetes_mm_normalized - data_diabetes_mm_normalized.min())
                            / (data_diabetes_mm_normalized.max() - data_diabetes_mm_normalized.min()))
# 3- View the data in a box plot from matplotlib: (creates a .png on the path defined on the 'os') WITH NORMALIZATION
data_diabetes_mm_normalized.plot.box(figsize=(6, 6))  # tuple with dimensions of the figure
plt.savefig('min_max_normalized_box_plot.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()


# DATA NORMALIZATION: (standardization feature scaling)
# 1- Copy the data
data_diabetes_std_normalized = data_diabetes.copy()
# 2- Apply normalization techniques
data_diabetes_std_normalized = ((data_diabetes_std_normalized - data_diabetes_std_normalized.mean())
                            / data_diabetes_std_normalized.std())
# 3- View the data in a box plot from matplotlib: (creates a .png on the path defined on the 'os') WITH NORMALIZATION
data_diabetes_std_normalized.plot.box(figsize=(6, 6), vert=False)  # tuple with dimensions of the figure and horizontal
plt.savefig('std_normalized_box_plot.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()


# DATA CORRELATION:
# Create a 'scatter_matrix' with the 'data_diabetes_mm_normalized': (diagonal = 'hist')
pd.plotting.scatter_matrix(data_diabetes, alpha=0.5, figsize=(10, 10), ax=None, grid=False, diagonal='hist',
                           marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05)
plt.savefig('min_max_normalized_scatter_matrix_hist.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()

# Create a 'scatter_matrix' with the 'data_diabetes_mm_normalized': (diagonal = 'kde')
pd.plotting.scatter_matrix(data_diabetes, alpha=0.5, figsize=(10, 10), ax=None, grid=False, diagonal='kde',
                           marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05)
plt.savefig('min_max_normalized_scatter_matrix_kde.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()

# Pearson correlation coefficient:
pcd = data_diabetes.corr(method='pearson', min_periods=1, numeric_only=False)
print(pcd)

# Correlation HeatMap: (using Seaborn lib)
seaborn.heatmap(pcd.round(2), vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=True, fmt='.2g',
                annot_kws=None, linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False,
                xticklabels='auto', yticklabels='auto', mask=None, ax=None)
plt.savefig('data_correlation_seaborn.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()
