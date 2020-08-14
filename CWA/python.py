# Python
# Instructions
# ● You have been provided with a sample text file of Chicago firefighters. For this exercise,
# please use that data set.
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
cfd = pd.read_csv("C:\Users\Christine\Google Drive - c.amuzie\Applications\CWA\cfd.csv")
cfd.head(5)

# ● Please provide us with the code for the script that opens the included text file and
# ● does the following:
# ○ Converts the delimiter from comma (“,”) to tab.

# ○ Converts all of the header fields to uppercase.
# ○ Adds a column named “VERIFIED” to the header
# ○ Populates all rows in the “VERIFIED” column with “Y”
# ● You may use either Python 2 or 3 for your work.