import pandas as pd

# Load the Excel data into a DataFrame
excel_file = 'mine.xlsx'
df = pd.read_excel(excel_file)   # messes up the date format while reading

# Format the 'Transaction Date' and 'Revenue Posting Date' columns to the desired format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date']).dt.strftime('%-m/%-d/%Y')
df['Revenue Posting Date'] = pd.to_datetime(df['Revenue Posting Date']).dt.strftime('%-m/%-d/%Y')

# Remove duplicate Customer Order ID records
df_no_duplicates = df.drop_duplicates(subset=['Custome Order ID'], keep=False)

# Save the DataFrame without duplicates to a new Excel file
df_no_duplicates.to_excel('no_duplicate.xlsx', index=False)
print("Process Successful!!!")