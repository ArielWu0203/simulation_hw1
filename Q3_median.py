import pandas as pd
import collections
import matplotlib.pyplot as plt
import numpy as np

# TODO : get the count table
def read(name):
    df = pd.read_csv(name)
    shape = df.shape
    # TODO : get raws of WAP1~520
    raws = df.iloc[0:shape[0],0:520]

    # TODO : calculate median
    table = raws.median(axis = 0)

    return table


# TODO : plot
def plot_table(table):
    x = list(range(1,521))
    y = table.values

    fig = plt.figure()
    plt.xlabel('WAP number')
    plt.ylabel('median value')
    plt.title('Distribution of the median of each WAP')
    plt.plot(x,y)
    plt.xlim((0,521))
    plt.gcf().autofmt_xdate()
    fig.savefig('Q3_median.png')

if __name__ == '__main__':
    table = read('TrainingData_new.csv')
    plot_table(table)