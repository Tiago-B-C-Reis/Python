import os
os.chdir("/Users/tiagoreis/PycharmProjects/Python/ISEP_DM/Pytho_data_mining")
import pandas as pd

# Read the existing Excel files
CustomerAmount = pd.read_excel("CustomerAmount.xlsx")
CustomerDiscount = pd.read_excel("CustomerDiscount.xlsx")

# Show the content (first 5):
print(CustomerAmount.head())
print(CustomerDiscount.head())

# Create a new Excel file to serve as output/final:
output_excel = "output_customer.xlsx"
writer = pd.ExcelWriter(output_excel, engine="xlsxwriter")

# Write the DataFrames to the output Excel file
CustomerAmount.to_excel(writer, sheet_name="amount", index=False)
CustomerDiscount.to_excel(writer, sheet_name="discount", index=False)

# Join the table from amount to discount:
df_join = CustomerAmount.join(CustomerDiscount.set_index('Customer'), on='Customer')

df_join['total'] = df_join['Amount'] * (1 - df_join['Discount'])
df_join.to_excel(writer, sheet_name="join", index=False)

# Close the output file:
writer.close()
