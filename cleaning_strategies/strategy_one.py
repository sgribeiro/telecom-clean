# Estratégia 01: limpeza e tratamento de valores ausentes

# Imports
import numpy as np
import pandas as pd

# Calcula o percentual de valores ausentes
def percent_missing(DataFrame):
    """
    Calculates the percentage of missing values in a pandas DataFrame.

    Parameters:
    DataFrame: pandas DataFrame - The DataFrame to be analyzed.

    Returns:
    string - A string containing the percentage of missing values in the DataFrame.

    Example:
    df = pd.DataFrame({'A': [1, 2, np.nan], 'B': [3, np.nan, np.nan], 'C': [4, 5, 6]})
    percent_missing(df)
    '33.33%'
    """
    percent_missing = DataFrame.isnull().mean().mean() * 100
    return f"{round(percent_missing, 2)}%"

# Calcula o percentual de valores ausentes por coluna
def columns_percent_missing(DataFrame):
    return pd.DataFrame({'Dataset Columns':DataFrame.isnull().sum(), 
                         'Dictionary Columns':DataFrame.isnull().mean(),
                         'Type': DataFrame.dtypes})