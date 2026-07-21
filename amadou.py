
def demo_partie_4():
    m1 = MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui")
    m2 = MembreStandard(2, "Marc Bouchard", "Est", 6, 40, "Non", "Non")
    m3 = MembrePremium(3, "Sophie Nguyen", "Centre-ville", 12, 80, "Oui", "Oui")
    m4 = MembrePremium(4, "Karim Haddad", "Ouest", 24, 75, "Oui", "Non")

    # une seule boucle qui affiche les 4, peu importe leur type exact
    for m in (m1, m2, m3, m4):
        m.afficher()

    return m1, m2, m3, m4
def creer_membres_exemple():
    membres = []
    membres.append(MembreStandard(1, "Julie Tremblay", "Centre-ville", 12, 45, "Oui", "Oui"))
    membres.append(MembreStandard(2, "Marc Bouchard", "Est", 6, 40, "Non", "Non"))
    membres.append(MembrePremium(3, "Sophie Nguyen", "Centre-ville", 12, 80, "Oui", "Oui"))
    membres.append(MembrePremium(4, "Karim Haddad", "Ouest", 24, 75, "Oui", "Non"))
    return membres
 
 
def afficher_tous(membres):
    for m in membres:
        m.afficher()

def sauvegarder_membres(membres, nom_fichier="membres.txt"):
    with open(nom_fichier, "w", encoding="utf-8") as f:
        for m in membres:
            if isinstance(m, MembreStandard):
                ligne = f"STANDARD;{m.numero};{m.nom};{m.succursale};{m.duree};{m.prix};{m.actif};{m.casier}\n"
            elif isinstance(m, MembrePremium):
                ligne = f"PREMIUM;{m.numero};{m.nom};{m.succursale};{m.duree};{m.prix};{m.actif};{m.coach}\n"
            f.write(ligne)
            