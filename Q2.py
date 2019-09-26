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

    # TODO : count WAPs value
    table = []
    for i in range(0,shape[0]): # raws
        index = pd.Index(raws.loc[i]) # value
        for j in range(0,520):
            table.append(index[j])

    se_table = pd.Series(table)
    bin = [-10000]
    for i in range(-100,5,5):
        bin.append(i)
    count = pd.value_counts(pd.cut(se_table,bin,right=False),sort=False)

    #print(count)
    return count


# TODO : plot
def plot_table(table):
    x = [" "]
    y = []
    for i in range(0,21):
        x.append("["+str(table.index[i].left)+","+str(table.index[i].right)+")")
        y.append(table[table.index[i]])
    y.append(0)
    # print(x)
    # print(y)
    fig = plt.figure()
    plt.xlabel('Range of RSSI')
    plt.ylabel('Number of RSSI value')
    plt.title('Distribution of RSSI value')
    plt.bar(np.arange(22),y,1)
    plt.xticks(np.arange(22),x,fontsize=5)
    plt.gcf().autofmt_xdate()
    plt.margins(x=0,y=0)
    fig.savefig('Q2.png')

if __name__ == '__main__':
    table = read('TrainingData_new.csv')
    plot_table(table)