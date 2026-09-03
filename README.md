# RunFlashSCP (SCP RP)
## Sommaire:
- Information sur le repo
- Installation
- Propriété intellectuelle du Repo
- Contexte
- Prévention
- Fonctionnement

## Information sur le repo

- Nom: RunFlashSCP 0.0
- Version: 0.0.0.0
- Crédit:
    - kishirednight

## Installation

### Prérequis
- Avoir Git installé sur votre PC
- Téléchargez Git gratuitement ici : [git-scm.com](https://git-scm.com)

### Ouvrir l'invite de commande
- **Windows** : Appuyez sur `Win + R`, tapez `cmd`, puis appuyez sur `Enter`
- **Alternative** : Ouvrez l'Explorateur de fichiers, allez au dossier où vous voulez télécharger le projet, puis faites un clic-droit et sélectionnez "Ouvrir le terminal ici"

### Copier et coller cette commande
```bash
git clone https://github.com/Kishirednight/SCP-RP-Roblox-Run-commandes.git
```

## Propriété intellectuelle du Repo

### Le contenu
Le contenu de ce repo est la propriété de kishirednight. Son utilisation est gratuite, y compris les mises à jour. 

Aucune copie du contenu ne peut être utilisée à des fins commerciales ou pour s'attribuer les droits sur le contenu du repo.

### L'utilisation de l'IA
L'IA a pu être utilisée pour la correction, la compréhension et le débogage du code. Certains contributeurs l'ont utilisée à cette fin et nous l'acceptons. 

Cependant, il est important de noter que l'IA n'a pas produit le contenu initial en son intégralité. Elle a été utilisée pour le mettre au propre, corriger des erreurs et faciliter la création du contenu.

### La contribution
Les améliorations et les ajouts de fonctionnalités sont autorisés et seront crédités sur le repo.
Un contributeur ne possède le droit que sur les modifications qu'il a apportées, et non sur le repo dans son intégralité.

## Contexte

### Plateforme
Ce repo vise à simplifier les commandes run pour SCP RP sur Roblox. Jeu réalisé par <u>MetaMethod</u>."

### Limite
Le repo est lancé via un terminal en cliquant sur "run.bat". Il n'existe aucune connexion directe entre le contenu du repo et le jeu lui-même.

## Prévention

Toute modification du code doit être effectuée via un fork GitHub. Cela permettra de tester vos idées en toute sécurité et de les proposer ultérieurement au repo original.

### Erreur
Le script n'est pas parfait et peut engendrer des erreurs inattendues. En cas d'erreur, merci de signaler le problème et sa reproduction via une issue sur GitHub.

Ne tentez pas de corriger l'erreur vous-même.

## Fonctionnement

### Ajouter vos fichiers ".json"

Tous les fichiers au format "JSON" contenant une liste de commandes run dédiées à un rôle précis doivent être placés dans le dossier `"Dossier"/Data"`.

#### Format

```json
{
    "1": {
        "nom": "Nom de votre commande run", //  Nom donné à votre ensemble de commandes.
        "commandes": [ // Liste des commandes à exécuter. "[]" Obligatoire.
            "Commande1",
            "Commande2"
        ]
    }, // Ajouter une virgule pour vos prochaines commandes run.
}
```

#### Information supplémentaire

Le script peut gérer la création de nouvelles commandes run en intégrant directement vos fichiers "JSON" dès le départ. Cette approche permet d'éviter les erreurs potentielles et un format "JSON" corrompu.