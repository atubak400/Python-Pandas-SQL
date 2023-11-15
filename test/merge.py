import pandas as pd

# Read the two sheets from the Excel file
df_sheet1 = pd.read_excel('mine.xlsx', sheet_name='Sheet1')
df_sheet2 = pd.read_excel('mine.xlsx', sheet_name='Sheet2')

# Merge DataFrames on common columns G and H
df_combined = pd.merge(df_sheet1, df_sheet2, on=['G', 'H'], how='outer')

# Create Excel writer
with pd.ExcelWriter('mine2.xlsx', engine='xlsxwriter') as writer:
    # Write the combined DataFrame to a single sheet
    df_combined.to_excel(writer, sheet_name='CombinedSheet', index=False)