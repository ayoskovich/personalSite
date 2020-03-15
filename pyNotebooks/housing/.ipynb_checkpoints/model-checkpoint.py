"""
Modeling for boston house prices
"""

import statsmodels.api as sm
import pandas as pd
import seaborn as sns

from statsmodels.stats.outliers_influence import OLSInfluence
from statsmodels.stats.outliers_influence import variance_inflation_factor

import featureCreate


def slr(df, xVars, yVar):
    """Simple linear regression."""
    return sm.OLS(df[yVar], df[xVars]).fit()


def getDFB(mod):
    """Return dfbetas for model object. """
    return OLSInfluence(mod).summary_frame()


def getPlot(mod):
    """Plot influence. 
    2 / sqrt(n) as cutoff for dfbeta
    """
    sm.graphics.influence_plot(mod)
    
    
def getCoefs(mod):
    """Return clean model coefficients."""
    return (
        pd.DataFrame(mod.params)
        .reset_index()
        .rename(columns={'index':'var', 0:'coef'})
    )


def getVIF(df, plot=True):
    """Returns dataframe containing the VIF. 
    
    df should contain only x variables."""
    X = df
    X['Intercept'] = 1

    vif = pd.DataFrame()
    vif["var"] = X.columns
    vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    vif = vif.query('var != "Intercept"')
    
    if plot:
        sns.barplot(x='var', y='VIF', data=vif);
    else:
        return vif
