from rpy2.robjects import pandas2ri, r
from rpy2.robjects.packages import importr
pandas2ri.activate()
islr = importr("ISLR")
wage = r['Wage']
wage.head()
