import pandas as pd
Num=[10,20,30,40,50]
#1D-array with labels
print(pd.Series(Num))
'''
index  data
0       1
1       2
2       3
3       4
4       5
dtype: int64
'''
import pandas as pd
Num=['Number',10,20,30,40,50]
print(pd.Series(Num))
'''
0    Number
1        10
2        20
3        30
4        40
5        50
dtype: object
'''
Num=[10,20,30,40,50]
print(pd.Series(Num,index=['A','B','C','D','E']))
'''
A    10
B    20
C    30
D    40
E    50
dtype: int64
'''
Num=[10,20,30,40,50]
print(pd.Series(Num,index=['i','ii','iii','iv','v']))
'''
i      10
ii     20
iii    30
iv     40
v      50
dtype: int64
'''