"""
Create features
"""

import pandas as pd
import numpy as np

def logVars(df, varList):
    """Log variables in varList and drop originals. """
    for var in varList:
        df['log_'+var] = np.log(df[var])
        df.drop(labels=[var], axis=1)
        
    return df