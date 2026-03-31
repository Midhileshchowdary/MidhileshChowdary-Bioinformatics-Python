import pandas as pd 
calories={'day 1':420,'day 2':380,'day 3':390}
print(pd.Series(calories))
'''
day 1    420
day 2    380
day 3    390
dtype: int64
'''
import pandas as pd 
calories={'day 1':420,'day 2':380,'day 3':390}
# observe index calls and keys in dictionary called as they are'nt same it shows NaN
print(pd.Series(calories,index=["day1","day2","day3"]))
'''
day1   NaN
day2   NaN
day3   NaN
dtype: float64
'''
calories={'day 1':420,'day 2':380,'day 3':390}
# observe index calls and keys in dictionary called as they are same it shows values
print(pd.Series(calories,index=["day 1","day 2","day 3"]))
'''
day 1    420
day 2    380
day 3    390
dtype: int64
'''