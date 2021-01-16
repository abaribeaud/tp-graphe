class Arc():
    """
        Class de l'objet Arc
    """
    def __init__(self):
        self.poid = 0
        self.predecesseur = ""
        self.successeur = ""

    def saisie(self):
        """
            Récupère les informations saisie par l'utilisateur et modifie les attributs de l'Arc
        """
        self.predecesseur = input("\tL’extrémité initiale est le sommet : ")
        self.successeur = input("\tL’extrémité finale est le sommet : ")
        self.poid = int(input("\tSa valeur est : "))