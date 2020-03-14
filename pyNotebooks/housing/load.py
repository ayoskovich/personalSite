"""
Load data for the boston house price dataset.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from housing import decorators

from pandas.plotting import scatter_matrix
from sklearn.datasets import load_boston


def importDat(cols):
    """Import the housing dataset and add column names.
    
    cols (list): List of columns to use
    """

    x = pd.DataFrame(load_boston()['data'])
    y = pd.DataFrame(load_boston()['target'])

    df = pd.concat([x, y], axis=1)
    
    df.columns = list(load_boston()['feature_names']) + ['price']
    
    # Save description
    with open(os.path.join('housing', 'datDescr.txt'), "w") as text_file:
        text_file.write(load_boston()['DESCR'])
    
    return df[cols]


@decorators.showChange
def filterDat(df):
    """Filter out records of the dataframe."""
    return df.query('AGE < 100')
