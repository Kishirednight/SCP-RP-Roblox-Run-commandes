def main(run: str, JSON: dict) -> None:
    liste = JSON[run]
    variables = {}

    for nom_variable in ["PSEUDO", "RANG", "NOMDECODE", "VALEUR1", "VALEUR2"]:
        if any(f"{{{nom_variable}}}" in commande for commande in liste["commandes"]):
            variables[nom_variable] = input(f"Choissisez la valeur pour {nom_variable}: ")

    commandes_formatees = []
    for commande in liste["commandes"]:
        if isinstance(commande, str):
            try:
                commande = commande.format(**variables)
            except KeyError:
                pass
        commandes_formatees.append(commande)

    message = " & ".join(commandes_formatees)

    print("=" * 50)
    print("run " + message)
    print("=" * 50)