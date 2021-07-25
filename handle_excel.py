# -*- coding utf-8 -*-
import pandas as pd
a = pd.read_excel('D:\\GitHub\\data_a.xlsx', index_col=[0], header=[0])
b = pd.read_excel('D:\\GitHub\\data_b.xlsx', sheet_name=None, index_col=None, header=None, skiprows=0, na_values=['NA'])  # it's a dictionary
b_sheet1 = b['Sheet1'] # it is a DataFrame
b_sheet1[3] = b_sheet1[2] - b_sheet1[1]
b_sheet2 = b_sheet1[2] - b_sheet1[1]

还剩切片操作
# where index_col=[0] means that using the first column as the index rows
# index_col=None means that nothing was set as the index rows
# header=[2] means deleting the first and second rows and using the third row as the index columns
# header=None means that nothing was set as the index columns


#df.to_excel('foo.xlsx',sheet_name='Sheet1')

##############################################################################################################
'''
# 18 Pandas Functions to Replace Excel with Python (and be happy forever)
# Import Package
import pandas as pd

# Work With Excel Files
df = pd.read_excel('filename.xlsx') # Read Excel File
df.to_excel('filename.xlsx', index=Fales) # Save Excel File
# pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, squeeze=False, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)
# DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None, storage_options=None)

# Work With CSV Files
df.read_csv('filename.csv') # Read CSV File
df.to_csv('filename.csv') # Save CSV File

# Preview DataFrame
df.head()
df.tail()
df.shape()

# Get Statistics
df.count() # Count Rows
df.describe() # Get general statistics (min,max,mean,std,...)
df['col_name'].value_counts() # Get unique value count

# Work with DataFrame
df['col_name'] # Select one column
df.fillna(0) # Replace Null values
df.dropna() # Remove Null values
df[df['col_name'] == 0] # Filter DataFrame
df.drop_duplicates() # Remove duplicates
df = pd.util.testing.makeDataFrame() # or # pd.get_dummies(pd.Series(list('abcaa'))) # Create dummy dataframe

# Replace Vlookup With Pandas Join
df.join(df2,on='col_name') # vlookup

# Pandas .replace() vs Excel Find and Replace
df.replace('to_replace', 'new_value) # Find and Replace
df.replace(regex=r'^ba.$', value='new') # Allows regex

# Replace Pivot Tables with GroupBy
df.groupby(['col1','col2']).sum() # Pivot/Groupby
df.groupby(['col1','col2']).agg({'col1':'sum','col2','count'})

# Plot Your DataFrame
df.plot() # Plot your DataFrame
'''
##############################################################################################################