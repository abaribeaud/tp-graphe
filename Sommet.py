class Sommet():
    def __init__(self):
        self.name = ""
        self.degre = 0

    def saisie(self):
        """
            Récupère les informations saisie par l'utilisateur et modifie les attributs du Sommet
        """
        self.name = input("\tNom du sommet : ")
