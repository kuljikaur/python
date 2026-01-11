import pandas as pd 
print(pd.__version__) # teels us about the version of pandas 

#data structure used by pnadas 

# 1. series: (list), or single column , multiple rows 
# 2. dataframe: full table,  more cols, fulfledge table 

# pandas series
sales = pd.Series([2,3,4,5]) #series is function
print(sales)
