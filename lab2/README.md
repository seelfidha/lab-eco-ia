<a id="top"></a>

# Mini-lab 2 — Développement d’une application avec Streamlit connectée a OLLAMA

<summary><strong> — Résumé du travail effectué</strong></summary>

<br/>
<details>
Ce mini-lab porte sur le développement d’une application simple d'interaction avec des modeles ollama en utilisant **Streamlit**. 

Faute de performance, des modèles légers tels que gemma3:270m & qwen3:0.6b ont été utilisé 

L’interface mise en place permet à un utilisateur ce qui suit:

<br/>
1 - Installer ollama avec la commande : "irm https://ollama.com/install.ps1 | iex"

<br/>
2 - Installer la bibliotheque ollama localement : "pip install ollama"

<br/>
3 - Faire un pull des modeles a utiliser tels que: "ollama pull gemma3:270m", "ollama pull qwen3:0.6b" & "ollama pull qwen2.5-coder:0.5b"
"

</details>
<br/>
Pour lancer le projet pour la première fois il suffit de:

1 - se pointer dans le dossier lab2 avec l'invite de commande
<br/>
2 - Lancer app.py : "streamlit run app.py"


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

<br/> 
PS: vous devez installer Ollama localement pour utiliser l'application sinon vous erreur une d'execution
