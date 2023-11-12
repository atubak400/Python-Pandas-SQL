import pandas as pd

# Load the Excel data into a DataFrame
excel_file = 'mine.xlsx'
df = pd.read_excel(excel_file)

# Perform SQL-like queries on the DataFrame
filtered_data = df.query('`Custome Order ID` < 10')

# Save to a new Excel file without the index
filtered_data.to_excel('filtered_data.xlsx', index=False)
