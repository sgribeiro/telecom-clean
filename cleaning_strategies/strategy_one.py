# Estratégia 01: limpeza e tratamento de valores ausentes

# Importações
import numpy as np
import pandas as pd

def percent_missing(DataFrame):
    """
    Retorna uma string com a porcentagem de valores ausentes no DataFrame de entrada.

    Args:
        DataFrame (pandas.DataFrame): DataFrame de entrada a ser analisado.

    Returns:
        str: String contendo a porcentagem de valores faltantes no DataFrame de entrada, arredondada para duas casas decimais,
        seguida pelo símbolo "%".
    """
    percent_missing = DataFrame.isnull().mean().mean() * 100
    return f"{round(percent_missing, 2)}%"

def columns_percent_missing(DataFrame):
    """
    Retorna um DataFrame com as colunas do DataFrame de entrada, mostrando a quantidade e porcentagem de valores faltantes
    em cada coluna, bem como o tipo de dados de cada coluna.

    Args:
        DataFrame (pandas.DataFrame): DataFrame de entrada a ser analisado.

    Returns:
        DataFrame (pandas.DataFrame): DataFrame com as colunas do DataFrame de entrada, mostrando a quantidade e porcentagem de valores faltantes 
        em cada coluna, bem como o tipo de dados de cada coluna. 
    """
    columns_missing = pd.DataFrame({'Missing Values': DataFrame.isnull().sum(), 
                                    'Missing Values (%)': DataFrame.isnull().mean() * 100,
                                    'DType': DataFrame.dtypes})

    return columns_missing.sort_values('Missing Values (%)', ascending=False).round(2)
