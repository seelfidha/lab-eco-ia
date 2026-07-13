import json

import pandas as pds
import streamlit as st
import os

from services.csv_services import create_dataframe_summary
from services.executor_service import execute_operation
from services.ollama_services import create_operation_plan



st.title('Assistant virtuel pour manipuler un fichier CSV')

uploadedFile = st.file_uploader('Veuillez charger un fichier csv', type=['csv'])

if uploadedFile is not None:
    savePath = os.path.join('uploads', uploadedFile.name)
    os.makedirs('uploads', exist_ok=True)
    df = pds.read_csv(uploadedFile)
    st.dataframe(df.head(100))
    summary = create_dataframe_summary(df)

    question = st.chat_input('Veuillez poser une question sur le fichier csv chargé')

    if question is not None:

        plan = create_operation_plan(question, summary, 'qwen3:0.6b')

        result = execute_operation(df, plan)

        st.write(result)

        st.divider()


    