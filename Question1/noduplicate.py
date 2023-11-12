import pandas as pd

# Load the Excel data into a DataFrame
excel_file = 'mine.xlsx'
df = pd.read_excel(excel_file)

# Remove duplicate Customer Order ID records
df_no_duplicates = df.drop_duplicates(subset=['Custome Order ID'], keep=False)

# Save the DataFrame without duplicates to a new Excel file
df_no_duplicates.to_excel('no_duplicate_data2.xlsx', index=False)




'''
=> {PANDAS}:
Pandas is a powerful open-source data manipulation and analysis library for Python. It provides easy-to-use data structures 
such as data frames and series, along with a variety of tools for cleaning, exploring, and analyzing structured data. 
Pandas is widely used in data science and machine learning tasks for handling and processing tabular data efficiently.


=> {excel_file = 'mine.xlsx'}: This line stores the file path of an Excel file in the variable excel_file. 
The variable excel_file now holds the information needed to locate and access the specific Excel file ('mine.xlsx') in our code.


=> {df = pd.read_excel(excel_file)}: Here, we use pandas to read the Excel file specified by the variable excel_file into a pandas DataFrame. 
The resulting DataFrame is assigned to the variable df, making it a convenient in-memory representation of the data contained 
in the Excel file. We can now perform various data manipulation and analysis tasks on this DataFrame using pandas functions and methods.


=> {df_no_duplicates = df.drop_duplicates(subset=['Custome Order ID'], keep=False)}:
In this line of code, we are using the drop_duplicates method from the pandas library to create a new DataFrame called df_no_duplicates. 
This new DataFrame is derived from the original DataFrame df by removing rows where the values in the 'Custome Order ID' 
column are duplicated.

The subset=['Custome Order ID'] argument specifies that the check for duplicates should be performed only based on the values 
in the 'Custome Order ID' column.

When keep=False is specified, it means that all occurrences of the duplicated values should be removed, keeping none of them.
keep=True (default): Keeps the first occurrence of the duplicated values and removes the subsequent ones.

So, df_no_duplicates will contain the same columns as the original DataFrame df, but with rows where 'Custome Order ID' 
is duplicated removed.


=> {df_no_duplicates.to_excel('no_duplicate_data2.xlsx', index=False)}
We are using the to_excel method from the pandas library to export the DataFrame df_no_duplicates to an Excel file 
named 'no_duplicate_data2.xlsx'.

The index=False parameter in the to_excel method specifies that you do not want to include the index column in the exported Excel file. 
When index is set to False, it means that the DataFrame's index (row labels) will not be included as a separate column in the Excel file. 
If you omit index=False or use index=True (which is the default), the index will be included in the Excel file as the leftmost column.
'''