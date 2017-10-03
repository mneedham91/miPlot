import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice #This is used in setting up the colors

# Initialize folder to save images. This shold be made more dynamic / editable
folder = 'C:/Users/mneedham/Documents/Python/10k/'

#Initialize pyplot style
plt.style.use('ggplot')

# Read in data file. This should be made more dynamic / editable
df = pd.read_csv('10k.csv')

# Pull out benchmarks row. This should include a check
benchmarks = df.tail(1)
df = df[:-1]

df = df.set_index('Name')
index = df.index.values
col_count = len(df.columns)

# Initialize colors list. this should be made more dynamic / editable
my_colors = list(islice(cycle(['#6a8747','#6a8747','#B64926','#B64926','#d6a137','#d6a137','#115a87','#115a87','#778899','#778899']), None, len(df)))

# Function to create an image file name using folder, statistic, and file extension
def filename(header):
    filename = header.replace(" ", "_") + ".png"
    new_string = os.path.join(folder, filename)
    return new_string

# This is the meat of the program. Graphs a statistic and saves an image of the graph.
# Among other likely changes, make the "kind" field editable.
def kplot(myStat):
    sub_series = df[myStat]
    plt.bar(range(len(sub_series)), sub_series, color=my_colors)
    plt.title("10K Phase One: " + myStat)
    plt.xticks(range(len(sub_series)),index)
    if(benchmarks.loc[10,myStat] > 0):
        plt.plot([0.0, len(sub_series)-1], [benchmarks.loc[10,myStat], benchmarks.loc[10,myStat]], "k--", color="r", label="Benchmark")
        plt.legend()
    if(myStat=="Delivery Rate"):
       plt.ylim((0.9,1))
    plt.savefig(filename(myStat), bbox_inches='tight')
    plt.clf()

# Goes through all columns in the dataframe and calls kplot
for column in df:
    try:
        kplot(column)
    except ValueError:
        pass
