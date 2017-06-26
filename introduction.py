# Chapter 1: Introduction
import pandas as pd
from rpy2.robjects import pandas2ri, r
from rpy2.robjects.packages import importr
import matplotlib.pyplot as plt
plt.switch_backend('qt5agg')
plt.ioff()
plt.style.use('ggplot')

pandas2ri.activate()
islr = importr("ISLR")
wage = r['Wage']
wage.columns

for x in ['age', 'year']:
    x_val = sorted(wage[x].unique())
    y_hat = [wage[wage[x] == xv].wage.mean() for xv in x_val]
    wage.plot(x=x, y='wage', kind='scatter')
    plt.plot(x_val, y_hat)
    plt.show()

# Make the education column a 'categorical' (pandas version of 'factor')
wage['education'] = wage.education.astype('category')  # Does have correct ordering

# Plot all 5 education levels on the same axes
ed = wage.pivot(columns='education', values='wage')
ed.boxplot(rot=45)
fig = plt.gcf()
fig.set_size_inches(4,5)
plt.tight_layout()
plt.show()

