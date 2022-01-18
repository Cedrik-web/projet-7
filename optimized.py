import csv


# initialise le budget maximun client et les chemins des fichiers d'actions
CLIENT_BUDGET = 500.00
ROOT_CSV = "fichier_d_action/dataset2_Python+P7.csv"


def recovery_action_list():
    """lecture d'un fichier csv et le transforme en liste"""

    list_action = []
    with open(ROOT_CSV, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"]
            cout = float(row["price"])
            benefice = float(row["profit"])
            t = [name, cout, benefice]
            list_action.append(t)
        return list_action


def first_tri_list(data):
    """enleve les actions de valeur négative ou égole à 0 et return un tableau"""

    tab = []
    for i in data:
        cout = i[1]
        if cout > 0:
            tab.append(i)

    return tab


def sort_list_by_profit_percentage(tab):
    """tri à bulles calibré sur le pourcentage et return un tableau"""

    n = len(tab)
    for i in tab:
        i.reverse()

    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j+1] < tab[j]:
                tab[j+1], tab[j] = tab[j], tab[j+1]

    for i in tab:
        i.reverse()

    tab.reverse()
    return tab


def sort_list_by_profit_value(tab):
    """tri a bulles calibré sur le pourcentage en valeur et return un tableau"""

    n = len(tab)
    for i in tab:
        cout = i[1]
        pourcentage = i[2]
        valeur = cout*pourcentage/100
        i.append(valeur)

    for i in tab:
        i.reverse()

    for i in range(n):
        for j in range(0, n - i - 1):
            if tab[j + 1] < tab[j]:
                tab[j + 1], tab[j] = tab[j], tab[j + 1]

    for i in tab:
        i.reverse()

    tab.reverse()
    return tab


def create_bascket_list(data):
    """creation de panier d'action d'un montant défini par le CLIENT_BUDGET initialiser
    en haut du script et return un tableau"""

    cout_global = 0.00
    panier = []

    for i in data:
        cout_action = i[1]
        ecart = CLIENT_BUDGET - cout_global
        if cout_action <= ecart:
            cout_global += cout_action
            panier.append(i)

    return panier


def statistique_panier(tab):
    """calcul le cout et le profit global du panier d'action rentré en parametre et return
    ces informations sous forme de liste"""

    cout_panier = 0.00
    profit_panier = 0.00

    for i in tab:
        cout = i[1]
        profit = cout * i[2] / 100
        cout_panier += cout
        profit_panier += profit

    panier = [cout_panier, profit_panier]
    return panier, tab


def choice_best_list(list1, list2):
    """choisit le panier le plus rentable entre ces deux panier et return ce choix sous
    forme d'une liste contement un tableau et une liste"""

    panier1 = statistique_panier(create_bascket_list(list1))
    panier2 = statistique_panier(create_bascket_list(list2))

    if panier1[1] > panier2[1]:
        return panier1
    else:
        return panier2


def add_customer_basket():
    """appel des fonctions necessaire pour la creation d'un panier d'action avec un budget
    pre_défini calibré sur le meilleur profit et affiche en console le resultat"""

    list_action = first_tri_list(recovery_action_list())
    list_action2 = first_tri_list(recovery_action_list())
    retour = choice_best_list(sort_list_by_profit_value(list_action), sort_list_by_profit_percentage(list_action2))

    valeur_profit = retour[0]
    panier_d_action = retour[1]

    print("\nliste d'action dans le panier du client :\n")
    for i in panier_d_action:
        print(i)
    print("\ncout et profit de ce panier :\n", valeur_profit, "\n")


# appel de fonction
add_customer_basket()
