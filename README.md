Mise en place du programmme:
	
	
	ETAPE 1 : Mise en place de votre environement virtuel. 
	
	- Dans votre terminal, allez dans le repertoire où se situe le dossier qui contient 	tout les fichiers, les dossiers et srcipts du programme. 
	- Créez votre environement virtuel en tapant : 
		sur windows : python -m venv env 
		sur mac ou Unix : python3 -m venv env
	- En cas de besoin, vous trouverez plus d'informations sur docs.python liens ci-joins: 
					https://docs.python.org/fr/3/library/venv.html
	- Activez votre environement en tapant: 
		sur windows :              env\scripts\activate
		sur mac ou Unix :          source env/bin/activate

	- Vous allez voir apparaitre "(env)" en entête de la ligne de commande. 


	ETAPE 2 : Integration des bibliothèques nécessaires pour l'application. 
	
	- Dans votre environement virtuel que vous venez de créer, importez toutes les 			bibliothèques nécessaires en tapant: 
		pip install -r requirements.txt
		
		
	ETAPE 3 : L'application est prête vous pouvez la lancer en tapant: 
		sur windows :              python bruteforce.py	
		sur mac ou Unix :          python3 bruteforce.py
        
        ou

        sur windows :              python optimized.py	
		sur mac ou Unix :          python3 optimized.py
		


Cas particulier:

    
    Pour lancer l'algorithme sur un nouveaux fichier csv vous devez :
        
        - Mettre le fichier dans le fichier_d_action 
        - Dans le script choisit rentrer le nom du fichier dans la constante
                ROOT_CSV = fichier_d_action/"nom du nouveau fichier"
        - Puis procéder comme à l'étape 3 précédente