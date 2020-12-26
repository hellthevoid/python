import numpy as np
import pandas as pd


df = pd.read_csv('example')

df.to_csv('example',
          index = False)

# ## Excel
# Pandas can read and write excel files, keep in mind, this only imports data. Not formulas or images, having images or macros may cause this read_excel method to crash. 

# ### Excel Input

pd.read_excel('Excel_Sample.xlsx',
              sheetname = 'Sheet1')

# ### Excel Output

df.to_excel('Excel_Sample.xlsx',
            sheet_name = 'Sheet1')

# ## HTML
# 
# You may need to install htmllib5,lxml, and BeautifulSoup4. In your terminal/command prompt run:
# 
#     conda install lxml
#     conda install html5lib
#     conda install BeautifulSoup4
# 
# Then restart Jupyter Notebook.
# (or use pip install if you aren't using the Anaconda Distribution)
# 
# Pandas can read table tabs off of html. For example:

# ### HTML Input
# 
# Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects:

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

