import pandas as pd

# Read the two sheets from the Excel file
df_sheet1 = pd.read_excel('test.xlsx', sheet_name='Cleansed Sales Listing')
df_sheet2 = pd.read_excel('test.xlsx', sheet_name='Bank Statements')

# Convert date columns to the desired format for the relevant sheet
df_sheet1['Transaction Date'] = pd.to_datetime(df_sheet1['Transaction Date']).dt.strftime('%-m/%-d/%Y')
df_sheet1['Revenue Posting Date'] = pd.to_datetime(df_sheet1['Revenue Posting Date']).dt.strftime('%-m/%-d/%Y')

df_sheet2['Transaction Date'] = pd.to_datetime(df_sheet2['Transaction Date']).dt.strftime('%-m/%-d/%Y')

# Calculate 'Reporting Currency Amount' only for df_sheet2
df_sheet2['Reporting Currency Amount'] = df_sheet2['Customer Currency Amount'] * df_sheet2['Ex Rate']

# Merge DataFrames on common columns 'Transaction Date', 'Customer Currency' and 'Customer Currency Amount'
df_combined = pd.merge(df_sheet1, df_sheet2, on=['Transaction Date', 'Customer Currency', 'Customer Currency Amount'], how='outer')

# Create Excel writer
with pd.ExcelWriter('test2.xlsx', engine='xlsxwriter') as writer:
    # Write the combined DataFrame to a single sheet
    df_combined.to_excel(writer, sheet_name='CombinedSheet', index=False)



'''
This Python code reads two Excel sheets ('Cleansed Sales Listing' and 'Bank Statements') with fields such as 'Customer Order ID,'
'Transaction Date,' 'Revenue Posting Date,' 'Customer Currency,' 'Customer Currency Amount,' 'Ex Rate,' and 'Reporting Currency Amount.'
It formats date columns, calculates 'Reporting Currency Amount' for 'Bank Statements,' merges the sheets based on common fields 
'Transaction Date,' 'Customer Currency,' and 'Customer Currency Amount,' and writes the resulting combined dataframe to 'test2.xlsx.
'''
