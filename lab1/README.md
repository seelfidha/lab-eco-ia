<a id="top"></a>

# Mini-lab 1 — Développement d’une application de visualisation de données CSV avec Streamlit

<summary><strong> — Résumé du travail effectué</strong></summary>

<br/>
<details>
Ce mini-lab porte sur le développement d’une application simple de visualisation de données avec **Streamlit**. 
L’interface mise en place permet à un utilisateur ce qui suit:

<br/>
1 - Chargement d'un fichier CSV
<br/>
2 - Affichage du contenu de fichier sous forme de tableau
<br/>
3 - Analyse du contenu de fichier. Cette partie consiste a :
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;a - afficher une description du dataset, 
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;b - afficher un graphique pour chaque colonne,
<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;c - pour chaque colonne, determiner les données manquantes ainsi que leurs pourcentages,
<br/> 
&nbsp;&nbsp;&nbsp;&nbsp;d - trouver les données dupliquées
<br/>
4 - Suppression de fichier
</details>
<br/>
Pour lancer le projet pour la première fois il suffit d'exécuter la liste de commande suivante: 

<br/>
1 - Créer un environnement virtuel python avec la commande : "py -3.11 -m venv myenv"

<br/>
2 - Activer l'environnement avec la commande : "myenv\Scripts\activate"

<br/>
3 - Installer (1) Streamlit : "pip install streamlit" (2) matplotlib : "pip install matplotlib"

<br/>
4 - Ouvrir le dossier lab1 : "cd lab1"

<br/>
5 - Lancer app.py : "streamlit run app.py"

<br/>
PS: Vous pouvez rencontrer une erreur liée a l'installation de la bibliothéque matplotlib

<br/>
Pour lancer l'application depuis docker desktop, 

1 - pointez vous dans le dossier du lab a executer

<br/>
2 - Ensuite creer une image docker avec la commande: docker build -t app-name . 
(remplacez app-name par le nom de l'instance de votre choix)

<br/>
3 - Une fois l'image cree lancez l'execution soit:
(a) avec docker desktop (n'oubliez pas de specifier le port 8501)
(b) ou via la commande docker run -p 8501:8501 app-name