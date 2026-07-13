import pandas as pd
from streamlit import empty

ALLOWED_OPERATION = {
    'count_rows',
    'count_duplicates',
    'describe',
    'filter',
    'sort',
    'groupby_aggregate',
    'missing_values',
    'value_counts',
    'correlation'
}

def validate_column(
        df: pd.DataFrame,
        column: str
):
    if column not in df.columns:
        raise ValueError(f'La colonne {format(column)} est inconnue')

def execute_operation(
        df: pd.DataFrame,
        plan:dict):

    print('Operation execution phase')

    if not plan:
        return 'Aucune operation retrouvée'

    operation = plan.get('operation')
    parameters = plan.get('parameters', {})

    if operation not in ALLOWED_OPERATION:
        raise ValueError(f'L\'operation {operation} est inconnue')

    if operation == 'count_rows':
        return len(df)

    if operation == 'count_duplicates':
        return int(df.duplicated().sum())

    if operation == 'missing_values':
        return df.isna().sum().sort_values(ascending=False)

    if operation == 'describe':
        return df.describe(
            include="all"
        ).transpose()

    if operation == 'value_counts':
        column = parameters["column"]
        validate_column(df, column)

        return df[column].value_counts(dropna=False)

    if operation == 'sort':
        column = parameters["column"]
        ascending= parameters.get('ascending', True)

        validate_column(df, column)
        return df.sort_values(
            by=column,
            ascending=ascending
        )

    if operation == 'groupby_aggregate':
        group_column = parameters['group_column']
        value_column = parameters['value_column']
        aggregation = parameters['aggregation']
        validate_column(df, group_column)
        validate_column(df, value_column)
        allowed_aggregation = {
            "mean",
            "sum",
            "min",
            "max",
            "median",
            "count"
        }
        if aggregation not in allowed_aggregation:
            raise ValueError(f'L\'aggregation {format(aggregation)} est inconnue')

        return (
            df.groupby(group_column)[value_column]
              .agg(aggregation)
              .reset_index()
        )
    raise ValueError(f'L\'operation {operation} n\'est pas encore terminé')
