import csv


# initialise le budget maximun client et le chemin de fichier d'action
CLIENT_BUDGET = 500.00
ROOT_CSV = "fichier_d_action/dataset1_Python+P7.csv"


def recovery_action_list():
    """lecture d'un fichier csv et le transforme en liste"""

    list_action = {}
    with open(ROOT_CSV, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"]
            cout = float(row["price"])
            benefice = float(row["profit"])
            valeur = cout / 100 * benefice
            list_action[name] = {
                "price": cout,
                "profit": benefice,
                "profit_valeur": valeur,
            }
    return list_action


def selector_list_action(data):
    """enleve de la liste des actions a valeur inferieur ou égal à 0"""

    tab = {k:v for k, v in data.items() if v.get("profit_valeur") > 0 }
    return tab


def tri_list(data):
    """tri la liste sur la clé 'profit en valeur' en ordre décroissant"""

    tableau_trier = sorted(data.items(), key=lambda k:k[1]["profit_valeur"], reverse = True)
    return tableau_trier


def tri_list_pourcentage(data):
    """tri la liste sur clé  'profit en pourcentage' en ordre décroissant"""

    tableau_trier = sorted(data.items(), key=lambda k: k[1]["profit"], reverse=True)
    return tableau_trier


def sort_list(tab):
    """algorithme de style glouton itère sur la liste tab et ajoute dans le panier les actions
        selectionner, s'arrête quand le montant du panier à atteint la valeur du budget client"""

    panier = CLIENT_BUDGET
    benefice_panier = 0
    cout_panier = 0
    liste_action = []

    for i in tab:
        v = i[1]
        cout_action = v.get("price")
        valeur = v.get("profit_valeur")
        if panier > 0:
            if cout_action > panier:
                pass
            else:
                panier -= cout_action
                liste_action.append(i)
                benefice_panier += valeur
                cout_panier += cout_action
    return liste_action


def valeur_panier(data):
    """retourne la valeur des actions du panier"""

    valeur_profit = 0

    for i in data:
        v = i[1]
        profit = v.get("profit_valeur")
        valeur_profit += profit
    return valeur_profit


def selection_panier(data , data2):
    """choisit le panier le plus rentable"""

    if valeur_panier(data) > valeur_panier(data2):
        return data
    else:
        return data2


def print_statistique_panier(data):
    """affichage du détails du panier d'actions choisit par l'algorithme"""

    valeur_profit = 0
    cout_action = 0

    print("\nliste d' actions pour le meilleurs randement :\n")

    for i in data:
        v = i[1]
        profit = v.get("profit_valeur")
        cout = v.get("price")
        valeur_profit += profit
        cout_action += cout
        print(i[0])

    print("\ncout de ce panier  : ", cout_action, "€\n")
    print("profit de ce panier : ", valeur_profit, "€\n\n")


def add_customer_basket():
    """appel des fonctions necessaire pour la creation d'un panier d'action avec un budget
    pre_défini, calibré sur le meilleur profit"""

    list = recovery_action_list()
    data = selector_list_action(list)
    tab = tri_list(data)
    tab2 = tri_list_pourcentage(data)

    panier = sort_list(tab)
    panier2 = sort_list(tab2)

    best_panier = selection_panier(panier, panier2)

    print("\nvaleurisation du meilleur panier d'actions")
    print("pour le fichier : ", ROOT_CSV.replace("fichier_d_action/", ""))

    print_statistique_panier(best_panier)


# appel de fonction
add_customer_basket()
