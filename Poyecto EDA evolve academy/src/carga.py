import pandas as pd

def mostrar_info (df: pd.DataFrame, rows: int = 5) -> None:
    """
    Muestra información general del DataFrame: dimensiones, tipos de datos y 
    primeras filas.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame a explorar.
    rows : int, opcional
        Número de filas a mostrar con head(). Por defecto 5.
    """
    print("\n--- Dimensiones del dataset ---")
    print(df.shape)

    print("\n--- Tipos de datos por columna ---")
    print(df.dtypes)

    print(f"\n--- Primeras {rows} filas ---")
    print(df.head(rows))

    print(df.info)

    print(df.describe)

    