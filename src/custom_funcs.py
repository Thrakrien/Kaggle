import pandas as pd

def string_split(df,column):
    """
    Função em questão quebra uma coluna, usando '/' como o separador,
    criando outras 3 colunas chamadas Deck, Num e Side. Por fim, exclui
    a coluna utilizada para a quebra.

    Args: 
        df (pandas.DataFrame): Dataframe que contém os dados que deseja-se observar.
        column (pandas.Series): Coluna que será utilizada para transformação.

    Returns:
        Deck (pandas.Series): Coluna contendo o andar do navio que o aposento do passageiro ficava.
        Num (pandas.Series): Coluna contendo o numero do aposento do passageiro.
        Side (pandas.Series): Coluna contendo o lado em que o aposento do passageiro ficava.
    """

    df[['Deck','Num','Side']] = df[column].str.split(pat='/',expand=True)
    df = df.drop(column,axis=1)
    return df

def bool_to_num(df,column):
    """
    Função transforma os dados de booleanos (True ou False) para a sua forma numérica.

    Args:
        df (pandas.DataFrame): Dataframe que contém os dados que deseja-se observar.
        column (pandas.Series): Coluna que será utilizada para transformação.
    
    Returns:
        columns (pandas.Series): Coluna com o valor True ou False transformado
        para 1 (True) ou 0 (False).
    """
    df[column] = df[column].map(lambda x: 0 if x==False else 1)
    return df[column]
