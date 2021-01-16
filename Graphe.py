from Arc import Arc
from Sommet import Sommet


class Graphe():
    """
        Classe de l'objet Graphe
    """

    def __init__(self):
        self.sommets = []
        self.arcs = []

    def saisieUser(self):
        """
            Récupère les informations saisie par l'utilisateur et instancie les arcs et sommets du nouveau graphe
        """

        nombre_sommet = int(input("Combien y a-t-il de sommets ? : "))

        for i in range(1, nombre_sommet + 1):
            print("Sommet %i" % i)
            s = Sommet()
            s.saisie()
            self.sommets.append(s)

        nombre_arc = int(input("Combien y a-t-il d'arcs ? : "))

        for i in range(1, nombre_arc + 1):
            print("Arc %i" % i)
            a = Arc()
            a.saisie()
            self.arcs.append(a)

    def constructFromFile(self, path):
        """
            Construit un graphe en se basant sur un fichier .txt

        :param path: Chemin vers le fichier
        :type path: str
        """
        f = open(path, "r")

        d = f.readlines()

        sommets = d[0].strip("{}\n")
        sommets = sommets.split(", ")

        for sommet in sommets:
            s = Sommet()
            s.name = sommet
            self.sommets.append(s)

        arcs = d[1:]
        for arc in arcs:
            a = Arc()
            arc = arc.strip("\n")
            arc = arc.split("-")
            a.predecesseur = arc[0]
            a.successeur = arc[1]
            a.poid = arc[2]
            self.arcs.append(a)

    def calculeDegre(self, nom_sommet):
        """
            Caclule le degré d'un sommet

        :param nom_sommet: Nom du sommet à calculer
        :type nom_sommet: str
        :return: Le degré calculé
        :rtype: int
        """
        degre = 0

        for arc in self.arcs:
            if nom_sommet == arc.predecesseur or nom_sommet == arc.successeur:
                degre += 1

        return degre

    def getSommetParNom(self, nom):
        """
            Récupère l'instance d'un objet Sommet à partir de son nom

        :param nom: Nom du sommet à récuperer
        :type nom: str
        :return: Le sommet correspondant
        :rtype: Sommet
        """
        for sommet in self.sommets:
            if sommet.name == nom:
                return sommet

        return "error"

    def getSuccesseur(self, sommet, obstacle=""):
        """
            Récupère les successeurs du sommet

        :param sommet: Sommet sur lequel récuperer les successeurs
        :type sommet: Sommet
        :param obstacle: Nom du sommet obstacle
        :type obstacle: str
        :return: Une liste de successeurs
        :rtype: list
        """
        successeur = []
        for arc in self.arcs:
            if arc.predecesseur == sommet.name and arc.successeur != obstacle:
                successeur.append([arc.successeur, arc.poid])
        return successeur

    def plusCourtChemin(self, depart, arrive):
        """
            Calcule et affiche le plus court chemin entre un sommet de départ et un sommet d'arrivé
            Algorithme basé sur le modèle de Dijkstra

        :param depart: Nom du sommet de départ
        :type depart: str
        :param arrive: Nom du sommet d'arrivé
        :type arrive: str
        """
        sommet = self.getSommetParNom(depart)
        chemin = {depart: 0}

        new_elem = sommet
        new_elem_chemin = depart
        while new_elem.name != arrive:
            for voisin in self.getSuccesseur(new_elem):
                chemin[new_elem_chemin + voisin[0]] = chemin[new_elem_chemin] + int(voisin[1])

            chemin.pop(new_elem_chemin)

            mini = 20
            new_elem = ""
            for elem in chemin:
                if chemin[elem] < mini:
                    mini = chemin[elem]
                    new_elem = elem

            new_elem_chemin = new_elem
            new_elem = self.getSommetParNom(new_elem[-1])

        print("Le plus court chemin est %s de poids total %i" % (new_elem_chemin, chemin[new_elem_chemin]))

    def plusCourtCheminAvecObstacle(self, depart, arrive, obstacle):
        """
            Calcule et affiche le plus court chemin entre un sommet de départ et un sommet d'arrivé en prennant en compte un sommet obstacle
            Algorithme basé sur le modèle de Dijkstra

        :param depart: Nom du sommet de départ
        :type depart: str
        :param arrive: Nom du sommet d'arrivé
        :type arrive: str
        :param obstacle: Nom du sommet obstacle
        :type obstacle: str
        """
        sommet = self.getSommetParNom(depart)
        chemin = {depart: 0}

        new_elem = sommet
        new_elem_chemin = depart
        while new_elem.name != arrive:
            for voisin in self.getSuccesseur(new_elem, obstacle):
                chemin[new_elem_chemin + voisin[0]] = chemin[new_elem_chemin] + int(voisin[1])

            chemin.pop(new_elem_chemin)

            mini = 20
            new_elem = ""
            for elem in chemin:
                if chemin[elem] < mini:
                    mini = chemin[elem]
                    new_elem = elem

            new_elem_chemin = new_elem
            new_elem = self.getSommetParNom(new_elem[-1])

        print("Le plus court chemin avec l'obstacle %s est %s de poids total %i" % (
            obstacle, new_elem_chemin, chemin[new_elem_chemin]))

    def comparerGraphe(self, second_graphe):
        """
            Compare le graphe avec un second graphe passé en paramètre

        :param second_graphe: Graphe à comparer
        :type second_graphe: Graphe
        """
        sommet_commun = []
        for s in second_graphe.sommets:
            for d in self.sommets:
                if s.name == d.name:
                    sommet_commun.append(s.name)

        print("Sommet commun : %s" % sommet_commun)

        arc_commun = []
        for arc in second_graphe.arcs:
            for arc_s in self.arcs:
                if arc.predecesseur == arc_s.predecesseur and arc.successeur == arc_s.successeur and arc.poid == arc_s.poid:
                    arc_commun.append(arc)

        for arc in arc_commun:
            print("Pred : %s / Suc : %s / Poid : %s" % (arc.predecesseur, arc.successeur, arc.poid))
