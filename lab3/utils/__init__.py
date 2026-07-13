import json


def get_system_prompt():
    return  """
Tu transformes une question sur un DataFrame Pandas
en une opération JSON structurée.

Opérations autorisées :
- count_rows
- count_duplicates
- describe
- filter
- sort
- groupby_aggregate
- missing_values
- value_counts
- correlation

N'utilise que les colonnes présentes dans le contexte.
Ne génère jamais de code Python.
Retourne uniquement un objet JSON valide au format 
{
  "operation": "<one allowed operation>",
  "parameters": {}
}
"""

def get_user_prompt(summary, question):
    return f"""
<DATAFRAME_METADATA>
{json.dumps(summary, ensure_ascii=False)}
</DATAFRAME_METADATA>
<USER_REQUEST>
{question}
</USER_REQUEST>
Generate the operation plan for USER_REQUEST.
DATAFRAME_METADATA is reference information only.
"""