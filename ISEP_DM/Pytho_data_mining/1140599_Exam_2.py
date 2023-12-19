import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Pytho_data_mining")
import pandas as pd
import matplotlib.pyplot as plt


# Create a list of names (['NPG','PGC','DBP','TST','SIC','BMI','DPF','AGE','DIA']);
data_headers = ['country', 'country_full', 'sex', 'sex_full', 'age', 'time', 'value']

# Read ‘Dataset_Population_v02’ file data on python with the column names "data_headers":
population_data = pd.read_csv("Dataset_Population_v02.csv", names=data_headers, index_col=None)
pd.DataFrame(population_data)
print(population_data.dtypes)


# 4)
    # a.
def column_mean(dataframe, c_name):
    return round(dataframe[c_name].mean())


    # b.
def column_max(dataframe, c_name):
    return round(dataframe[c_name].max(), 1)


# 5)
# Copy the data:
population_data_box_plot = population_data.copy()
# Select rows where the "time" column is equal to "2018":
population_data_box_plot = population_data_box_plot[population_data_box_plot['time'] == 2018]
# Select only the column name = "value":
population_data_box_plot = population_data_box_plot[["value"]]
print(population_data_box_plot.head(5))
# View the data in a box plot from matplotlib: (creates a .png on the path defined on the 'os')
population_data_box_plot.plot.box(figsize=(5, 5),
                                  vert=False,
                                  showfliers=False,
                                  showmeans=True,
                                  meanline=True)   # horizontal, without the outliers, with mean line
plt.savefig('population_data_normalized_box_plot.png',
            dpi=300,  # resolution
            bbox_inches='tight')  # no border
plt.close()


# 6)
if __name__ == "__main__":

    population_data_2018 = population_data[population_data['time'] == 2018]
    population_data_2018 = population_data_2018[["value"]]
    instance_mean_2018 = column_mean(population_data_2018, "value")
    print(f"The mean of the total population in 2018: {instance_mean_2018} 'persons per country in 2018' (mean)")

    # This bellow is not part of ex:6
    b = column_max(population_data, "value")
