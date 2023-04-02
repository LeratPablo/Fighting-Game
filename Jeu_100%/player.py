import pygame
import random

liste_competence = []
class competence:

    '''
        Cette classe permet la création de compétences qui pourront être utiliser pour attaquer l'adversaire.
    '''

    def __init__(self, dgt, nom):
        self.dgt, self.precision, self.mana = dgt
        self.nom = nom
    
    def __str__(self):
        return ""+str(self.nom)+","+str(self.dgt)+","+str(self.precision)
    
class gens:

    '''
        Cette classe permet la création de personnage et plus précisément les statistiques des personnages.
        L'appelle a la fonction "est_vivant" permet de renvoyer un Booléen qui indique si le personnage est vivant ou non.
        L'appelle a la fonction "fight" permet de lancer une attaque et de faire des dégats au personnage adverse.
        L'appelle a la fonction "get_stats" permet de récupérer un tuple contenant les pv et d'autres statistiques concernant le personnage.
    '''

    def __init__(self, stat, nom, compétence):
        self.pv, self.atk, self.deff, self.mana = stat
        self.nom = nom
        self.compétence = compétence #liste de compétence mais pour l'instant c'est qu'un objet

    def __str__(self):
        return str(self.nom, self.pv, self.atk, self.deff, self.mana, self.compétence)

    def est_vivant(self):
        return self.pv > 0
    
    def fight(self, compétence, victime):
        if self.mana < compétence.mana:
            return False
        if compétence.precision < 100:
            esquiveee = 100 - random.randint(0, 100)
            # print(esquiveee)
            # print(100 - esquiveee)
            if (esquiveee) > compétence.precision:
                return True
        reduction = victime.deff
        self.mana -= compétence.mana
        puissance = self.atk
        dgt_reçus = compétence.dgt + int((compétence.dgt * puissance)/100)
        #pour les test
        # print("réduction", reduction/100)
        true_dgt_reçus = int((dgt_reçus * reduction)/100)
        victime.pv -= true_dgt_reçus

    def get_stats(self):
        return (self.pv, self.mana)

class Perso:

    '''
        Cette classe permet la création de personnage qui pourront être afficher a l'écran. Cette classe permet également de faire déplacer les personages.
        L'appelle a la fonction "draw" permet de dessiner a l'écran l'image du perssonage passer en paramètre de l'initialisateur.
        L'appelle a la fonction "move" permet de modifier les coordonée du personnage et ainsi il peut être déplacer. Cette fonction prend en paramètre des coordonées x, y qui vont être ajoutées aux coordonées actuelle.
    '''

    def __init__(self, x, y, image, scale, screen):
        self.screen = screen
        self.width = image.get_width()
        self.height = image.get_height()
        self.scale = scale
        self.img = image
        self.image = pygame.transform.scale(self.img, (int(self.width * self.scale), int(self.height * self.scale)))

        self.x, self.y = x, y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.draw()

    def rescale(self, new_scale):
        self.scale = new_scale
        self.image = pygame.transform.scale(self.img, (int(self.width * self.scale), int(self.height * self.scale)))