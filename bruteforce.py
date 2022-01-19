import csv
from itertools import permutations
import cProfile
import re


# initialise le budget maximun client et le chemin du fichier d'action
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
            list_action[name] = {
                "price": cout,
                "profit": benefice,
            }
        print("\n fichier csv télécharger")
        return list_action


def sort_list_by_profit(tab):
    """creer toutes les combinaisons possible et return une liste"""

    comb = {}
    compteur = 0
    nombre = len(tab)
    print("\ncréation des combinaisons possibles")
    print("merci de patienter ...\n")

    for key in permutations(tab.keys(), nombre):
        compteur += 1
        list = "liste_" + str(compteur)
        action = {}
        for i in key:
            name = i
            action[i] = tab.get(name)
        comb[list] = action

    return comb

def data_brute(data_brute):
    """transforme DATABRUTE en liste et retour une liste de panier"""

    liste_panier = {}
    compteur = 0
    for data in data_brute.values():
        compteur += 1
        panier = "panier"+ str(compteur)
        liste = create_bascket_list(data)
        liste_panier[panier] = liste

    return liste_panier


def create_bascket_list(data):
    """creation de panier d'action d'un montant défini par le CLIENT_BUDGET initialiser
    en haut du script et return un tableau"""

    cout_global = 0.00
    panier = []
    compteur = 0

    for i, j in data.items():
        compteur += 1
        cout_action = j.get("price")
        ecart = CLIENT_BUDGET - cout_global

        if cout_action <= ecart:
            cout_global += cout_action
            choix = {i: j}
            panier.append(choix)

    return panier


def statistique_panier(tab):
    """calcul le cout et le profit global du panier d'action rentré en parametre et return
    ces informations sous forme de liste"""

    panier = {}
    paniers = []

    for key, value in tab.items():
        cout_panier = 0.00
        profit_panier = 0.00
        for i in value:
            for k, v in i.items():
                cout = v.get("price")
                profit = cout * v.get("profit") / 100
                cout_panier += cout
                profit_panier += profit
        panier[key] = {
                "profit_panier": profit_panier,
                "cout_panier": cout_panier,
                "liste_actions": value,
            }
        paniers.append(panier)

    return paniers


def choice_best_list(datas):
    """tri à bulles calibré sur le pourcentage et return un tableau"""

    data = datas[1]

    list_actions = sorted(data.items(), key=lambda k: k[1]["profit_panier"], reverse=True)

    return list_actions


def add_customer_basket():
    """appel des fonctions necessaire pour la creation d'un panier d'action avec un budget
    pre_défini, calibré sur le meilleur profit et affiche en console le resultat"""

    list_action = recovery_action_list()
    paniers = statistique_panier(data_brute(sort_list_by_profit(list_action)))

    liste = choice_best_list(paniers)

    panier_trier = liste[0]
    basket = panier_trier[1]

    valeur_profit = panier_trier[1].get("profit_panier")
    cout_d_action = basket.get("cout_panier")
    liste_d_action = basket.get("liste_actions")

    print("\n\nliste d'action des meilleurs actions :\n")
    for i in liste_d_action:
        print(i)
    print("\ncout de ce panier :\n", cout_d_action, "€\n")
    print("cout de ce panier :\n", valeur_profit, "€\n\n")


# appel defonction
cProfile.run(add_customer_basket())
