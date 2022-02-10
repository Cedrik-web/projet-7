import csv
from itertools import permutations, combinations
from tqdm import tqdm
from time import sleep
from math import factorial
import os


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


def control_budget_total_action(data):
    """controle si la valeur globale des actions est plus grande que le budget client"""

    price = 0

    for k, v  in data.items():
        price_action = v.get("price")
        price += price_action

    if price >= CLIENT_BUDGET:
        return True


def sort_list(tab):
    """initialise les compteurs et autres variables necessaires, compte les monbres d'actions quand
        celui ci est inferieur à 13 renvoie sur une fonction qui itere sur la listes de permutations
        et autrement renvoie sur une fonction qui itere sur la listes de conbinaisons"""

    panier_action = []
    compteur = 0
    conb = len(tab)
    # definie la longueur de des listes d'actions reduit la liste afin de reduire le monbre de permutations possible
    longueur_liste = int(conb - (conb / 4))
    permu = permutations(tab.items(), conb)
    tab_tri = tri_list(tab)
    conbinaisons = combinations(tab_tri.items(), longueur_liste)
    comptage = combinations(tab_tri , longueur_liste)
    total = factorial(conb)

    if conb < 13:
        os.system("clear")
        print("Python va générer et comparer " + str(total) + " toutes les permutations d'actions possible , merci de patienter ...\n")

        for liste, i in zip(permu, tqdm(range(int(0), int(total)))):
            panier_action = take_panier(liste,panier_action, conb)
    else:
        for _ in comptage:
            compteur += 1

        os.system("clear")
        print("Python va générer et comparer " + str(compteur) + " conbinaison d'actions, merci de patienter ...\n")

        for liste, i in zip(conbinaisons, tqdm(range(compteur))):
            panier_action = take_panier(liste, panier_action, longueur_liste)
            sleep(0.001)

    return panier_action


def take_panier(data, paniers, longueur_list):
    """itere sur la liste d'actions et retourne le panier d'actions le plus rentable"""

    panier_action = paniers
    panier = CLIENT_BUDGET
    benefice_panier = 0
    liste_action = []
    cout_panier = 0

    for count, action in enumerate(data):
        v = action[1]
        cout_action = v.get("price")
        valeur = v.get("profit_valeur")
        if cout_action > panier:
            if valeur_panier(liste_action) > valeur_panier(panier_action):
                panier_action = liste_action
                return panier_action
            else:
                return panier_action
        elif count == longueur_list -1:
            if valeur_panier(liste_action) > valeur_panier(panier_action):
                panier_action = liste_action
                return panier_action
            else:
                return panier_action
        else:
            panier -= cout_action
            liste_action.append(action)
            benefice_panier += valeur
            cout_panier += cout_action


def valeur_panier(data):
    """retourne la valeur des actions du panier"""

    valeur_profit = 0

    for i in data:
        v = i[1]
        profit = v.get("profit_valeur")
        valeur_profit += profit
    return valeur_profit


def tri_list(data):
    """tri la liste sur la clé 'profit en valeur' en ordre décroissant"""

    tableau = sorted(data.items(), key=lambda k:k[1]["profit_valeur"], reverse = True)
    tableau_trier = {}
    for i in tableau:
        tableau_trier[i[0]] =  i[1]
    return tableau_trier


def add_customer_basket():
    """appel des fonctions necessaire pour la creation d'un panier d'action avec un budget
    pre_défini, calibré sur le meilleur profit"""

    data = recovery_action_list()
    data_control = control_budget_total_action(data)
    if data_control == True:
        panier = sort_list(data)
        print_statistique_panier(panier)
    else:
        os.system("clear")
        print("\nle budget client permet d'acheter toutes les actions de cette liste.\n")


def print_statistique_panier(panier):
    """affichage du détails du panier d'actions choisit par l'algorithme"""

    valeur_profit = 0
    cout_action = 0

    print("\nAnalyse du fichier : ", ROOT_CSV.replace("fichier_d_action/", ""), "\n")
    print("\npanier d'actions pour la meilleure rentabilitée :\n")

    for i in panier:
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



