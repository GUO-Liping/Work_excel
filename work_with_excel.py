# -*- coding utf-8 -*-
import pandas as pd
a = pd.read_excel('data_a.xlsx', index_col=[0], header=[0])
b = pd.read_excel('data_b.xlsx', sheet_name=None, index_col=None, header=None, skiprows=0, na_values=['NA'])  # it's a dictionary
# where index_col=[0] means that using the first column as the index rows
# index_col=None means that nothing was set as the index rows
# header=[2] means deleting the first and second rows and using the third row as the index columns
# header=None means that nothing was set as the index columns

b_sheet1 = b['Sheet1'] # it is a DataFrame
b_sheet1[3] = b_sheet1[2] - b_sheet1[1]
b_sheet2 = b_sheet1[2] - b_sheet1[1]

b_sheet2.to_excel('data_b2.xlsx',sheet_name='Sheet1')

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

# Selection DataFrame
df1 = pd.DataFrame(np.random.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
df1.loc[['a', 'b', 'd'], :]
df1.loc['d':, 'A':'C']
df1.loc['a']
df1.loc['a'] > 0
df1.loc[:, df1.loc['a'] > 0]
df1.loc['a', 'A']
df1.loc[lambda df: df.A > 0, :]
df1.loc[:, lambda df: ['A', 'B']]
df1.iloc[:, lambda df: [0, 1]]
df1[lambda df: df.columns[0]]
df1.A.loc[lambda s: s > 0]
df2 = pd.DataFrame(np.random.randn(6,4), index=list(range(0,12,2)), columns=list(range(0,8,2)))
df2.iloc[:3]
df2.iloc[1:5, 2:4]
df2.iloc[[1, 3, 5], [1, 3]]
df2.iloc[1:3, :]
df2.iloc[:, 1:3]
df2.iloc[1, 1]

# Convert to numpy array
df = pd.DataFrame([[21, 72, 67], [23, 78, 69], [32, 74, 56], [52, 54, 76]],	columns=['a', 'b', 'c'])
arr = df.to_numpy()  # Note that the recommended approach is df.to_numpy().
arr = df.values

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