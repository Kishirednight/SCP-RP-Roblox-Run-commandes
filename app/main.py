# === Fonctions === #
def chargement(data: str) -> dict:
    '''
    Renvoie le fichier JSON sous forme de dictionnaire.

    Le dictionnaire peut être vide.
    '''

    import json
    import os

    JSON = {}
    fJSON = {}

    if not os.path.exists(data):
        with open(data, "w", encoding="utf-8") as fichier:
            json.dump({}, fichier, ensure_ascii=False)

    if os.path.getsize(data) == 0:
        with open(data, "w", encoding="utf-8") as fichier:
            json.dump({}, fichier, ensure_ascii=False)

    with open(data, "r", encoding="utf-8") as fichier:
        JSON = json.load(fichier)

    if isinstance(JSON, dict):
        for indice, valeur in JSON.items():
            if "nom" not in valeur:
                print(f'La commande run n°{indice} n\'as pas de clé "nom".')
                continue
            if "commandes" not in valeur:
                print(f'La commande run n°{indice} n\'as pas de clé "commandes".')
                continue
            if not isinstance(valeur["commandes"], list):
                print(f"La commande run n°{indice}, sa liste de commandes n'est pas de type list.")
                continue

            fJSON[str(indice)] = JSON[indice]
    else:
        print(f"Le fichier au chemin {data} n'est pas un dictionnaire.")

    return fJSON


def choix(liste: list) -> int:
    '''
    Retourne l'index (ou indice) du choix de l'utilisateur sur une liste.
    '''

    print("Options disponibles:")

    for indice in range(len(liste)):
        print(f"{indice + 1} - {liste[indice]}")

    while True:
        reponse = input("Choix ?:")

        try:
            reponse = int(reponse)
        except ValueError:
            continue

        if 0 < reponse <= len(liste):
            return reponse


# === Scripts === #
if __name__ == "__main__":
    try:
        import sys

        if len(sys.argv) > 1:
            fichier_nom = input("Fichier se trouvant dans Data ?: ").strip()
            if not fichier_nom:
                raise ValueError("Le nom du fichier est vide.")

            fichier = "./Data/" + fichier_nom + ".json"
            JSON = chargement(fichier)

            option = ["Listes de commandes", "Créer une commande RUN", "Récupérer une commande RUN", "Info", "Quitter"]

            while True:
                print()

                nombre = choix(option) - 1
                print()

                if nombre == option.index("Listes de commandes"):
                    from scripts import prints
                    prints.tolist(JSON)

                elif nombre == option.index("Créer une commande RUN"):
                    from scripts import create
                    create.main(fichier, JSON)

                elif nombre == option.index("Récupérer une commande RUN"):
                    from scripts import recup
                    liste_commande = []

                    for valeur in JSON.values():
                        liste_commande.append(valeur["nom"])

                    run_index = choix(liste_commande)
                    run_key = list(JSON.keys())[run_index - 1]
                    recup.main(run_key, JSON)

                elif nombre == option.index("Info"):
                    from scripts import prints
                    prints.info()

                elif nombre == option.index("Quitter"):
                    break

            print("Fin du programme.")
            exit()
        else:
            exit()
    except Exception as erreur:
        print(f"Une erreur est survenue. Erreur: {erreur}")
        input()
        exit()