import os.path
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Visualisation et description d'un fichier CSV")

sidebar = st.sidebar
sidebar.write('This is my sidebar')

uploaded_file = st.file_uploader(
    "Veuillez charger un fichier CSV",
    type=["csv"]
)

if uploaded_file is not None:
    #########################################################upload
    path = os.path.join('uploads', uploaded_file.name)
    os.makedirs("uploads", exist_ok=True)

    with open(path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    details = {
        'filename': uploaded_file.name,
        'filesize (bytes)': uploaded_file.size
    }
    for k, v in details.items():
        st.write(k, ':', v)
    st.success('File uploaded successfully')

    df = pd.read_csv(path)

    #########################################################display
    st.header('Contenu du fichier CSV')
    columns = df.columns
    st.dataframe(df)

    tab1, tab2, tab3, tab4= st.tabs(['Description du dataset', 'Colonnes & graphiques', 'Données manquants','Données dupliquées'])
    #########################################################description
    with tab1:
        st.dataframe(df.describe().T)

    #########################################################columns
    with tab2:
        st.header('Liste des colonnes possibles: ')
        options = (columns.tolist())
        column = st.selectbox("Colonne", df.select_dtypes(include="number").columns)
        st.write("La colonne selectionnée est: ", column)
        fig, ax = plt.subplots()
        ax.hist(df[column].dropna(), bins=20)
        st.pyplot(fig)

    #########################################################missing
    with tab3:

        st.write('Liste des colonnes avec le % de données manquantes:')
        missingSummary = pd.DataFrame({
            'Nombre': df.isnull().sum(),
            'Pourcentage': (df.isnull().mean() * 100).round(2)
        })

        missingSummary = missingSummary[missingSummary['Nombre'] > 0]
        if missingSummary.empty:
            st.success("Aucune donnée manquante.")
        else:
            st.dataframe(missingSummary)

    #########################################################duplicates
    with tab4:
        duplicates = df.duplicated().sum()
        st.write(f"Duplicate rows: {duplicates}")

    #########################################################remove
    st.header('Suppression du fichier CSV chargé')
    if st.checkbox("Supprimer le fichier"):
        if(os.path.exists(path)):
            os.remove(path)
            st.success('Le fichier a été correctement supprimé')
        else:
            st.write('Le fichier n\'existe pas')

