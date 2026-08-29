def main(fichier: str, dico: dict) -> None:
    import json

    nom = input("Le nom de votre commande run ?: ").strip()
    while not nom:
        nom = input("Merci de rentrer une valeur valide: ").strip()

    commandes = []

    while True:
        print("Saisissez votre commande: ")
        print("- Des variables peuvent être mises entre {}.")
        print("- Les variables pouvant être mises (en majuscules) sont {PSEUDO}, {RANG}, {NOMDECODE}, {VALEUR1}, {VALEUR2}.")

        commande = input().strip()
        while not commande:
            commande = input("Entrer une commande valide: ").strip()

        commande = commande.replace('"', '\\"')
        commandes.append(commande)

        print('Pour mettre fin à l\'édition, tapez "non"')
        if input().strip().lower() == "non":
            break

    dico[str(len(dico) + 1)] = {"nom": nom, "commandes": commandes}

    with open(fichier, "w", encoding="utf-8") as fichier_json:
        json.dump(dico, fichier_json, indent=4, ensure_ascii=False)