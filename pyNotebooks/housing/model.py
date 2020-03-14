"""
Modeling for boston house prices
"""

import statsmodels.api as sm

from statsmodels.stats.outliers_influence import OLSInfluence

from housing import featureCreate


def slr(df, xVars, yVar):
    """Simple linear regression."""
    return sm.OLS(df[yVar], df[xVars]).fit()


def getDFB(mod):
    """Return dfbetas for model object. """
    return OLSInfluence(mod).summary_frame()

def getPlot(mod):
    """Plot influence. 
    2 / sqrt(n) as cutoff
    """
    sm.graphics.influence_plot(mod)