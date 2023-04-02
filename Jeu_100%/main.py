import pygame
import menu
import player
import random
from pygame import mixer 

class FENETRE:

	'''
		Cette classe sert a contenir la fenêtre graphique et les fonctions principales tel que l'initialisation ou l'actualisation.
	'''
	
	def __init__(self): # Initialisateur de la classe
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.screen_size = self.screen.get_size()

		self.end = False # Permet de savoir si le jeu doit être fermé
		self.pause = True # Permet de savooir si le jeu doit être mis en pause
		self.menu = True # Permet de savoir si le menu doit être afficher
		self.win_screen = False # Permet de savoir si il faut afficher l'écran de victoire

		# self.current_player = random.randint(0, 1)
		self.current_player = 0
		self.competence = None
		self.can_switch = False
		self.winner = None
		self.time = 120

		self.mouse_pos = ()
		
	def initialisation(self): # Initialise la fenêtre de jeu
		pygame.init()
		pygame.display.set_caption("La majestuatisation incroyable du jeu dans l'incroyablitude")
		self.screen.fill("#1E5287")
	
	def start(self): # Contient la boucle qui permet l'affichage constant de la fenêtre et les interactions avec elle

			self.initialisation()

			# Chargement de l'arrière plan
			BG = pygame.image.load("Assets/BG.jpg")
			bg_width = BG.get_width()
			bg_height = BG.get_height()	
			background = pygame.transform.scale(BG, (int(bg_width), int(bg_height)))

			# Chargement des écran de victoire
			winner_1 = pygame.image.load("Assets\winner_1.png")
			win_screen_1 = pygame.transform.scale(winner_1, (winner_1.get_width(), winner_1.get_height()))

			winner_2 = pygame.image.load("Assets\winner_2.png")
			win_screen_2 = pygame.transform.scale(winner_2, (winner_2.get_width(), winner_2.get_height()))

			#Chargement de la musique de fond
			musique = mixer.Sound("BGM\music.wav")
			musique.set_volume(0.2)
			musique.play(0, 0, 2000)
			
			# Création des menus
			menu_principale = menu.Menu_principal(self.screen, self.screen_size)

			menu_competence_gauche = menu.Selection_competence_gauche(self.screen, self.screen_size)
			menu_competence_droite = menu.Selection_competence_droite(self.screen, self.screen_size)

			# Chargement du sprite des personnages
			perso_A = pygame.image.load("Assets/perso_A.png")
			personnage_A = player.Perso(self.screen_size[0]//10, self.screen_size[1]//5, perso_A, 0.2, self.screen)

			perso_B = pygame.image.load("Assets/Perso_B.png")
			personnage_B = player.Perso(self.screen_size[0]//1.4, self.screen_size[1]//9, perso_B, 0.2, self.screen)

			# Création des compétences
			competence_1 = player.competence([10, 100, 0], "competence 1")
			competence_2 = player.competence([25, 80, 0], "competence 2")
			competence_3 = player.competence([40, 40, 0], "competence 3")
			competence_4 = player.competence([55, 55, 0], "competence 4")

			# Création des joueurs
			joueur_1 = player.gens([50, 100, 10, 42], "Bob", [competence_1, competence_2, competence_3, competence_4])
			joueur_2 = player.gens([50, 100, 10, 42], "Lebricoleur", [competence_1, competence_2, competence_3, competence_4])

			menu_stats_j1 = menu.Stats(joueur_1.get_stats(), self.screen_size[0] // 10, self.screen_size[1] // 1, self.screen)
			menu_stats_j2 = menu.Stats(joueur_2.get_stats(), self.screen_size[0] // 0.5, self.screen_size[1] // 5, self.screen)

			while not self.end: # Boucle principale du jeu. Permet l'affichage des frames du jeu (60 fps)

				pygame.time.delay(15)
				pygame.display.flip()

				for event in pygame.event.get(): # Cette boucle permet de récupérer les entrées clavier de l'utilisateur (Fermeture, clavier, souris, ...)
					if event.type == pygame.QUIT:
						self.end = True
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							self.end = True

				# Affichage du menu principale
				if self.menu:
					menu_principale.draw()
					if menu_principale.exited():
						self.end = True
					elif menu_principale.play():
						self.menu = False
						self.pause = False

				# Affichage du jeu en lui même
				if not self.pause and not self.menu: # Ce bloc contient le programme principale de la boucle quand le jeu n'est pas en pause

					self.screen.fill("#696969")
					self.screen.blit(background, (0, 0))

					menu_stats_j1 = menu.Stats(joueur_1.get_stats(), self.screen_size[0] / 7, self.screen_size[1] / 1.3, self.screen)
					menu_stats_j2 = menu.Stats(joueur_2.get_stats(), self.screen_size[0] / 1.3, self.screen_size[1] / 1.3, self.screen)
					menu_stats_j1.display_stats()
					menu_stats_j2.display_stats()

					# Affichage du joueur si il est encore vivant
					if joueur_1.est_vivant():
						personnage_A.draw()
					if joueur_2.est_vivant():
						personnage_B.draw()

					# Condition pour que le joueur 1 joue
					if self.current_player == 0:
						
						if joueur_2.est_vivant():
							menu_competence_gauche.draw_on_screen()

						if menu_competence_gauche.clic_action_btn() and self.can_switch == True:

							menu_competence_gauche.resset_pressed()

							for x in range(125):
								self.screen.fill("#696969")
								self.screen.blit(background, (0, 0))
								personnage_A.move(8, 0)
								personnage_B.draw()
								pygame.display.flip()
							
							for y in range(125):
								self.screen.fill("#696969")
								self.screen.blit(background, (0, 0))
								personnage_A.move(-8, 0)
								personnage_B.draw()
								pygame.display.flip()

							joueur_1.fight(self.competence, joueur_2)
							self.current_player = 1
							self.can_switch = False
						
						if menu_competence_gauche.clic_btn1():
							menu_competence_gauche.set_pressed(1)
							self.competence = competence_1
							self.can_switch = True

						elif menu_competence_gauche.clic_btn2():
							menu_competence_gauche.set_pressed(2)
							self.competence = competence_2
							self.can_switch = True

						elif menu_competence_gauche.clic_btn3():
							menu_competence_gauche.set_pressed(3)
							self.competence = competence_3
							self.can_switch = True

						elif menu_competence_gauche.clic_btn4():
							menu_competence_gauche.set_pressed(4)
							self.competence = competence_4
							self.can_switch = True

					# Condition pour que le joueur 2 joue
					if self.current_player == 1:
						
						if joueur_1.est_vivant():
							menu_competence_droite.draw_on_screen()

						if menu_competence_droite.clic_action_btn() and self.can_switch == True:

							menu_competence_droite.resset_pressed()

							for x in range(125):
								self.screen.fill("#696969")
								self.screen.blit(background, (0, 0))
								personnage_B.move(-8, 0)
								personnage_A.draw()
								pygame.display.flip()
							for y in range(125):
								self.screen.fill("#696969")
								self.screen.blit(background, (0, 0))
								personnage_B.move(8, 0)
								personnage_A.draw()
								pygame.display.flip()

							joueur_2.fight(self.competence, joueur_1)

							self.current_player = 0
							self.can_switch = False
						
						elif menu_competence_droite.clic_btn1():
							menu_competence_droite.set_pressed(1)
							self.competence = competence_1
							self.can_switch = True

						elif menu_competence_droite.clic_btn2():
							menu_competence_droite.set_pressed(2)
							self.competence = competence_2
							self.can_switch = True

						elif menu_competence_droite.clic_btn3():
							menu_competence_droite.set_pressed(3)
							self.competence = competence_3
							self.can_switch = True

						elif menu_competence_droite.clic_btn4():
							menu_competence_droite.set_pressed(4)
							self.competence = competence_4
							self.can_switch = True
				
				if not joueur_1.est_vivant():
					self.win_screen = True
					self.pause = True
					self.winner = 1
				elif not joueur_2.est_vivant():
					self.win_screen = True
					self.pause = True
					self.winner = 0

				# Affichage de l'écran de victoire
				if self.win_screen:

					#arrêt de la musique
					musique.fadeout(1500)

					if self.winner == 0:
						self.screen.fill("blue")
						self.screen.blit(win_screen_1, (0, 0))
					elif self.winner == 1:
						self.screen.fill("purple")
						self.screen.blit(win_screen_2, (0, 0))
						
FENETRE().start()