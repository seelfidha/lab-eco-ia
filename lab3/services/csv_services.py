import pandas as pds

def create_dataframe_summary(df: pds.DataFrame):

    print('Operation summary phase')

    return  {
        "row_count": int(len(df)),
        "columns_count": int(len(df.columns)),
        "columns": [
            {
                "name": column,
                "dtype": str(df[column].dtype),
                "missing_values": int(
                    df[column].isna().sum()
                ),
                "unique_values": int(
                    df[column].nunique()
                )
            }
           for column in df.columns
        ],
        "sample": df.head(5).to_dict(
            orient="records"
        ),
        "duplicate_count": int(df.duplicated().sum())
    }
