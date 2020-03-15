"""
Investigating outliers and other random stuff.
"""

import importlib
import pandas as pd
import numpy as np

import decorators

def taxPratio(df):
    """Investigate the weird scatter plot between tax and ptratio."""
    return (
        pd.DataFrame(
            df[df['TAX'] > 600][['TAX', 'PTRATIO']]\
            .groupby(['TAX', 'PTRATIO'])
            .size()
            .reset_index()
            .rename(columns={0:'count'})
        )
    )

