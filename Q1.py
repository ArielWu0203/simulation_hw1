import pandas as pd
import collections
import matplotlib.pyplot as plt

# TODO : get the table
def read(name):
    df = pd.read_csv(name)
    shape = df.shape
    # TODO : get raws of WAP1~520
    raws = df.iloc[0:shape[0],0:520]

    # TODO : count the number of 0
    table = {}
    for i in range(0,shape[0]):
        index = pd.Index(raws.loc[i])
        count = index.value_counts()
        APs = 520-count[0]
        table.setdefault(APs,0)
        table[APs] = table[APs]+1
    sort_table = collections.OrderedDict(sorted(table.items()))
    return sort_table

# TODO : plot
def plot_table(table):
    x = []
    y = []
    for k,v in table.items():
        x.append(k)
        y.append(v)
    fig = plt.figure()
    plt.xlabel('Numbers of detected WAP on single capture')
    plt.ylabel('Count')
    plt.title('Distribution of the number of WAPs')
    plt.scatter(x,y)
    
    fig.savefig('Q1.png')

if __name__ == '__main__':
    table = read('TrainingData_new.csv')
    plot_table(table)