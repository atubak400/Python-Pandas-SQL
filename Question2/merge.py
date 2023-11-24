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

# Concatenate DataFrames side by side
df_combined = pd.concat([df_sheet1, df_sheet2], axis=1)

# Create Excel writer
with pd.ExcelWriter('test2.xlsx', engine='xlsxwriter') as writer:
    # Write the combined DataFrame to a single sheet
    df_combined.to_excel(writer, sheet_name='CombinedSheet', index=False)



"""
-> pd.to_datetime(df_sheet1['Transaction Date']): This converts the 'Transaction Date' column of df_sheet1 into a pandas datetime object.

-> The .dt.strftime('%-m/%-d/%Y') method in your code indeed formats the datetime objects to only display the date in the specified format, 
effectively eliminating the time component in the displayed output.

-> .strftime('%-m/%-d/%Y'): This is used to format the datetime object into a specific string format. 
The format string '%-m/%-d/%Y' specifies that the date should be formatted as:
%-m: Month as a decimal number without a leading zero.
%-d: Day of the month as a decimal number without a leading zero.
%Y: Year with century as a decimal number.
For example, a date like "2023-01-05" would be formatted as "1/5/2023".

-> The axis=1 parameter in the pd.concat() function is used to specify the axis along which the concatenation should happen. 
In pandas, axis=0 is the default and represents concatenation along the index (rows), while axis=1 represents concatenation along the columns.

"""