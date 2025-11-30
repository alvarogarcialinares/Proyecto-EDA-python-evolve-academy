import pandas as pd

def comprobar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula valores nulos por columna y su porcentaje.

    Returns
    -------
    pd.DataFrame
        Tabla con el número de nulos y el porcentaje.
    """
    missing = df.isna().sum()

    result = pd.DataFrame({
        "Valores_nulos": missing })

    return result[result["Valores_nulos"] > 0]  # Mostrar solo columnas con nulos


def comprobar_duplicados(df: pd.DataFrame) -> pd.DataFrame:
    """
    Devuelve las filas duplicadas del dataset, si existen.

    Returns
    -------
    pd.DataFrame
        Filas duplicadas.
    """
    duplicates = df[df.duplicated(keep=False)]
    return duplicates


def rango(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el rango (mínimo y máximo) de todas las columnas numéricas.

    Returns
    -------
    pd.DataFrame
        Tabla con min y max de cada columna numérica.
    """
    numeric = df.select_dtypes(include="number")
    return pd.DataFrame({
        "Min": numeric.min(),
        "Max": numeric.max()
    })


def descripcion_categorias(df: pd.DataFrame, max_unique: int = 10) -> dict:
    """
    Devuelve un resumen de las columnas categóricas (tipo object), incluyendo 
    número de categorías únicas y las más frecuentes.

    Returns
    -------
    dict
        Diccionario con cada columna categórica y sus estadísticas.
    """
    result = {}
    cat_cols = df.select_dtypes(include="object").columns

    for col in cat_cols:
        uniques = df[col].nunique()
        freq = df[col].value_counts().head(max_unique)
        result[col] = {
            "n_categorías": uniques,
            "categorías_más_comunes": freq.to_dict()
        }

    return result

