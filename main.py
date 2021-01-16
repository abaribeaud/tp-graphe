from Graphe import Graphe

if __name__ == '__main__':
    g = Graphe()
    #g.saisieUser()
    g.constructFromFile("graphe.txt")
    print("Le degré du sommet est : %s" % g.calculeDegre("A"))
    g.plusCourtChemin("A", "G")
    g.plusCourtCheminAvecObstacle("A", "G", "H")
    g2 = Graphe()
    g2.constructFromFile("graphe_to_compare.txt")
    g.comparerGraphe(g2)