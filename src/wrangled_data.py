# author: Margaret Zhao
# date: 2020-01-22

'''This script saves the cleaning and pre-processing data set to a new file.

Usage: src/wrangled_data.py --input=<input> --output=<output>

Options:
--input=<input>  Name of csv file to download, must be within the /data directory.
--output=<output>  Name of wrangled data file to be saved in /data directory. 
'''

import pandas as pd
import numpy as np
from docopt import docopt

opt = docopt(__doc__)

def main(input, output):
    # download xls to pandas dataframe
    df = pd.read_csv(f"./data/{input}")
    
    # Add column names
    df.columns = ["Class", "age", "menopause", "tumor_size", "inv_nodes", "node_caps", "deg_malig", "breast", "breast_quad", "irradiat"]
    
    # Replace ? with NaN because it's easier to work with them 
    df = df.replace('?', np.nan)
    
    # change tumor size from categorical variable to numerical values by taking the average size
    tumor_size_str_lst = [i.split('-', 1) for i in list(df["tumor_size"])]
    tumor_size_int_lst = []
    tumor_size_avg_lst = []
    for i in range(len(tumor_size_str_lst)):
        tumor_size_int_lst.append([int(j) for j in tumor_size_str_lst[i]])
    for i in range(len(tumor_size_int_lst)):
        tumor_size_avg_lst.append(sum(tumor_size_int_lst[i])/len(tumor_size_int_lst[i]))
    df["avg_tumor_size"] = tumor_size_avg_lst
    df = df.drop(columns = ["tumor_size"])
    
    # Drop missing values
    df = df.dropna()
    
    # Change target to 0 and 1
    df['Class'] = df['Class'].replace({'no-recurrence-events': 0, 'recurrence-events': 1})
    
    # Save wrangled data to file
    df.to_csv(r"./data/%s" % (output), index=False)


if __name__ == "__main__":
    main(input=opt["--input"], output=opt["--output"])




