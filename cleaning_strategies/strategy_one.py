# Estratégia 01: limpeza e tratamento de valores ausentes

# Imports
import numpy as np
import pandas as pd

def percent_missing(DataFrame):
    """
    Returns a string with the percentage of missing values in the input DataFrame.

    Args:
        DataFrame (pandas.DataFrame): Input DataFrame to be analyzed.

    Returns:
        str: String containing the percentage of missing values in the input DataFrame, rounded to two decimal places,
        followed by the "%" symbol.
    """
    percent_missing = DataFrame.isnull().mean().mean() * 100
    return f"{round(percent_missing, 2)}%"

def columns_percent_missing(DataFrame):
    """
    Returns a DataFrame with the columns of the input DataFrame, showing the amount and percentage of missing values
    in each column, as well as the data type of each column.

    Args:
        DataFrame (pandas.DataFrame): Input DataFrame to be analyzed.

    Returns:
        DataFrame (pandas.DataFrame): DataFrame with the columns of the input DataFrame, showing the amount and percentage of missing 
        values in each column, as well as the data type of each column.
    """
    columns_missing = pd.DataFrame({'Missing Values': DataFrame.isnull().sum(), 
                                    'Missing Values (%)': DataFrame.isnull().mean() * 100,
                                    'DType': DataFrame.dtypes})

    return columns_missing.sort_values('Missing Values (%)', ascending=False).round(2)
