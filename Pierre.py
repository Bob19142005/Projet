# Code De Bob 
def charger_membres():
    membres = []

    try:
        with open("membres.txt", "r") as fichier:

            for ligne in fichier:
                donnees = ligne.strip().split(";")

                type_membre = donnees[0]  

                if type_membre == "STANDARD":
                    membre = MembreStandard(
                        int(donnees[1]),
                        donnees[2],
                        int(donnees[3]),
                        donnees[4] == "True"
                    )

                elif type_membre == "PREMIUM":
                    membre = MembrePremium(
                        int(donnees[1]),
                        donnees[2],
                        int(donnees[3]),
                        donnees[4] == "True",
                        donnees[5]
                    )

                membres.append(membre)

    except FileNotFoundError:
        print("Le fichier membres.txt n'existe pas.")

    return membres

membres = charger_membres()

print("Liste des membres chargés :")

for membre in membres:
    print(membre)


def hacher_membre(nom, succursale):

    return hash(nom + succursale)
def detecter_doublons_hash(membres):

    deja_vus = set()
    doublons = []


    for membre in membres:

        cle = hacher_membre(
            membre.nom,
            membre.succursale
        )


        if cle in deja_vus:

            doublons.append(membre)

        else:

            deja_vus.add(cle)


    return doublons

def detecter_doublons_liste(membres):

    deja_vus = []
    doublons = []


    for membre in membres:


        trouve = False


        for ancien in deja_vus:

            if (membre.nom == ancien.nom 
            and membre.succursale == ancien.succursale):

                trouve = True
                break


        if trouve:

            doublons.append(membre)


        deja_vus.append(membre)


    return doublons
def construire_index(membres):

    index_membres = {}


    for membre in membres:

        index_membres[membre.numero] = membre


    return index_membres        