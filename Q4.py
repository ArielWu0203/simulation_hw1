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

    # TODO : calculate mean
    table = raws.mean(axis = 0)
    
    # TODO : get the WAP of min mean
    min_wap = table.idxmin()

    table = df[[min_wap, "BUILDINGID"]]
    return(table)


# TODO : plot
def plot_table(table):
    # TODO : calculate the number of nonzero WAPs for every building
    building_zero = table[table["BUILDINGID"].isin([0])]
    B0_count = (building_zero != 0).sum(axis=0)
    building_one = table[table["BUILDINGID"].isin([1])]
    B1_count = (building_one != 0).sum(axis=0)
    building_two = table[table["BUILDINGID"].isin([2])]
    B2_count = (building_two != 0).sum(axis=0)

    x = [0,1,2]
    # TODO : y is for PDF, y2 is for CDF.
    y = [B0_count["WAP087"],B1_count["WAP087"],B2_count["WAP087"]]
    y2 = [y[0],y[0]+y[1],y[0]+y[1]+y[2]]
    
    fig = plt.figure()
    plt.xlabel('Buiding ID')
    plt.ylabel('the number of WAPs')
    plt.title('PDF & CDF of the RSSI distribution of different buildings')
    
    pdf = plt.bar(np.arange(len(x)),y,0.35,alpha=1,label="PDF")
    cdf = plt.bar(np.arange(len(x))+0.35,y2,0.35,alpha=0.2,label="CDF")
   
    plt.xticks(np.arange(len(x))+0.35,x)
    plt.legend(loc = 'upper left')
    fig.savefig('Q4.png')

if __name__ == '__main__':
    table = read('TrainingData_new.csv')
    plot_table(table)