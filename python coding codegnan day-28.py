'''
from datetime import datetime
current_ = datetime.now()#code to get current time
print(current_)
print(current_.strftime('%Y'))
print(current_.strftime('%m'))
print(current_.strftime('%d'))

here,
%d - day in the month
%m - month in the year
%Y - year
%H - hour
%M - minutes
%S - seconds
%I - 12 hours clock
%p - AM or PM

#code to get date,time with AM & PM 
from datetime import datetime , date
current_ = datetime.now().today()
today = date.today()
now = datetime.now()
print(current_.strftime("%d/%m/%Y %I:%M:%S %p"))

#code to get calendar,weekdays,leap year or nor
import calendar
#print(calendar.calendar(2026))
print(calendar.month(2026,7))
print(calendar.weekday(2026,7,24))
print(calendar.isleap(2026))

DATA ANALYSIS
--------------
>>Data analysis is the process of inspecting, cleaning, transform and modeling data to discover useful insights,
support decision-making, and identify patterns. It is widely used in industries such as finance, healthcare, marketing, and technology.

TYPES
------
1.Descriptive Analysis - summarize data
2.Diagnostic Analysis - Understanding causes
3.Predictive Analysis - Forecasting future outcomes
4.Priscriptive Analysis - Suggesting actions based on data..


**NUMPY**
----------
>>Numpy is a library in python which is known as numerical python..
>>This numpy have different diamentional arrays such as 1D , 2D , 3D ...
>>To used the numpy we have to import library as 'import numpy as np


1D Array
--------
@example
import numpy as np
arr_1 = np.array([[1,2,3]])
print(arr_1)


*Indexing in array
---------------------
>>As we used indexing in the list or tuple, here the way it works
>>By calling index position from array, we will get the value
>>Negtive indexing also will works

#neg index
import numpy as np
arr_1 = np.array([1,2,3])
print(arr_1[-1])

#indexing
import numpy as np
arr_1 = np.array([1,2,3])
print(arr_1[2])

*Slicing in array
------------------
import numpy as np
arr_1 = np.array([1,2,3])
print(arr_1[:2])

import numpy as np
arr_1 = np.array([1,2,3])
print(arr_1.sum())
print(arr_1.mean())
print(arr_1.max())
print(arr_1.min())

#2D Array
---------
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)

@reshape
import numpy as np
arr_1 = np.array([[1,2,3],[4,5,6]])
print(arr_1)
print(arr_1.reshape(2,3))

**PANDAS**
-----------
>>Pandas is an powerful python library and this is build on the top numpy
>>By used pandas data manipulation will be done
>>Pandas have Data structures like series and dataframes
>>To use this we have import the library
'import pandas an pd'

series
-------
@example
import pandas as pd
Data = pd.Series(
    [2000,2500,4000],
    index = ['Earphones','Charger','Mobile']
)
print(Data)

@code
import pandas as pd
df = {
    "products" : ['Laptop','Charger','Mobile'],
    'Brand' : ['Mac','Realme','Iphone'],
    "Price" : [57000,2500,23000],
    "Stocks" : [2,9,3],
    "Sales" : ['Amazon','offline','Flipkart']
}
data = pd.DataFrame(df)
print(data)
'''












