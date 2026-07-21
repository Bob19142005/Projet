
# ==========================
# CREATION CLASSE ET OBJET
# ==========================

class Membre:
    def __ini__(self, numero, nom, succursale, duree, prix, actif):
        self.numero = numero
        self.nom = nom
        self.succursale = succursale
        self.duree = duree
        self.prix = prix
        self.actif = actif

    def afficher(self):
        print(f"Numéro : {self.numero}")
        print(f"Nom : {self.nom}")
        print(f"Succursale : {self.succursale}")
        print(f"Durée : {self.duree} mois")
        print(f"Prix mensuel : {self.prix}$")
        print(f"Actif : {self.actif}")


membre1 = Membre(1, "Rose Bernard", "Montréal", 12, 45.99, "Oui")
membre2 = Membre(2, "Jean Martin", "Laval", 6, 59.99, "Non")

# Test de la méthode afficher()
membre1.afficher()
membre2.afficher()

# ======================
# ENCASULATION
# ======================

class Membre:
    def __init__(self, numero, nom, succursale, duree, prix, actif):
        self.__numero = numero
        self.__nom = nom
        self.__succursale = succursale
        self.__duree = duree
        self.__prix = prix
        self.__actif = actif

# Numero
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    # Nom
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    # Succursale
    @property
    def succursale(self):
        return self.__succursale

    @succursale.setter
    def succursale(self, succursale):
        self.__succursale = succursale

        # Durée
    @property
    def duree(self):
        return self.__duree

    @duree.setter
    def duree(self, duree):
        if duree > 0:
            self.__duree = duree
        else:
            print("Durée invalide.")

    # Prix
    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if prix > 0:
            self.__prix = prix
        else:
            print("Prix invalide.")

    # Actif
    @property
    def actif(self):
        return self.__actif

    @actif.setter
    def actif(self, actif):
        if actif.lower() == "oui":
            self.__actif = "Oui"
        elif actif.lower() == "non":
            self.__actif = "Non"
        else:
            print("État invalide.")

         # Affichage
    def afficher(self):
        print(f"Numéro : {self.numero}")
        print(f"Nom : {self.nom}")
        print(f"Succursale : {self.succursale}")
        print(f"Durée : {self.duree} mois")
        print(f"Prix mensuel : {self.prix}$")
        print(f"Actif : {self.actif}")

# ================
# HERITAGE
# ================
class MembreStandard(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, casier):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.casier = casier

    def afficher(self):
        super().afficher()
        print(f"Casier : {self.casier}")


# Classe dérivée Premium
class MembrePremium(Membre):
    def __init__(self, numero, nom, succursale, duree, prix, actif, coach):
        super().__init__(numero, nom, succursale, duree, prix, actif)
        self.coach = coach

    def afficher(self):
        super().afficher()
        print(f"Coach personnel : {self.coach}")


