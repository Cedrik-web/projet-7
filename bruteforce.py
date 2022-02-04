import csv


# initialise le budget maximun client et le chemin de fichier d'action
CLIENT_BUDGET = 500.00
ROOT_CSV = "fichier_d_action/action.csv"


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


def tri_list(data):
    """tri les liste sur la profit en valeur en ordre decroissant"""

    tableau_trier = sorted(data.items(), key=lambda k:k[1]["profit_valeur"], reverse = True)
    return tableau_trier


def sort_list_by_profit(tab):
    """algorithme de style glouton itère sur la liste tab et ajoute dans le panier les actions
        selectionner, s'arrête quand le montant du panier à atteint la valeur du budget client"""

    panier = CLIENT_BUDGET
    benefice_panier = 0
    cout_panier = 0
    liste_action = []

    while panier > 0:
        for i in tab:
            v = i[1]
            cout_action = v.get("price")
            valeur = v.get("profit_valeur")
            if cout_action > panier:
                pass
            else:
                panier -= cout_action
                liste_action.append(i)
                benefice_panier += valeur
                cout_panier += cout_action
    return liste_action


def add_customer_basket():
    """appel des fonctions necessaire pour la creation d'un panier d'action avec un budget
    pre_défini, calibré sur le meilleur profit"""

    data = recovery_action_list()
    tab = tri_list(data)

    panier = sort_list_by_profit(tab)

    print_statistique_panier(panier)


def print_statistique_panier(data):
    """affichage du détails du panier d'actions choisit par l'algorithme"""

    valeur_profit = 0
    cout_action = 0

    print("\nAnalyse du fichier : ", ROOT_CSV.replace("fichier_d_action/", ""), "\n")
    print("\npanier d' actions pour la meilleure rentabilitée :\n")

    for i in data:
        v = i[1]
        profit = v.get("profit_valeur")
        cout = v.get("price")
        valeur_profit += profit
        cout_action += cout
        print(i[0])

    print("\ncout de ce panier :\n", cout_action, "€\n")
    print("profit de ce panier :\n", valeur_profit, "€\n\n")


# appel de fonction
add_customer_basket()




