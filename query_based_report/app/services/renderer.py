import pandas as pd

def rows_to_df(columns, rows):
    return pd.DataFrame(rows, columns=columns)

def df_head_markdown(df: pd.DataFrame, n: int = 10) -> str:
    return df.head(n).to_markdown(index=False)
