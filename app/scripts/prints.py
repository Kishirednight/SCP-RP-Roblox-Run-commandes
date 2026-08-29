def tolist(dico: dict) -> None:
    '''
    Affiche la liste des commandes d'un ensemble de commandes run.
    '''
    if not dico:
        print("Aucune commande run disponible dans ce fichier.")
        return

    for num, valeur in dico.items():
        print("=" * 50)
        print(f"Run n°{num} - {valeur['nom']}")
        for commande in valeur.get("commandes", []):
            print(f"- {commande}")


def info() -> None:
    '''
    Affiche les informations du script.
    '''
    contributeur = ["kishirednight"]
    print("Crédit:")
    for indice, nom in enumerate(contributeur, start=1):
        print(f"- {indice}: {nom}")

    print()
    print("Version: 0.0.0.0")
    print()
    print("Info:")
    print('- Via le "README.md".')