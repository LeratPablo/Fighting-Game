import pygame

class Button:

	'''
		Cette classe sert a créer des boutons ainsi que de savoir si l'on clique sur celui ci.
		L'appelle a la fonction "draw" permet de dessiner a l'écran les différents boutons.
		L'appelle a la fonction "mouse_clicked premet de renvoyer un booléen qui servira a savoir si l'on clique ou non sur le bouton.
	'''

	def __init__(self, x, y, image, scale):
		self.width = image.get_width()
		self.height = image.get_height()
		self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))

		self.x, self.y = x, y
		
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, screen): # Cette fonction permet de dessiner les boutons a l'écran
		self.clicked = False
		screen.blit(self.image, (self.x, self.y))
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
			else:
				self.clicked = False

	def mouse_clicked(self): # Cette fonction renvoie True ou False en fonction de si on clic avec la souris
		return self.clicked

class Menu_principal:

	'''
		Cette class permet la création et l'affichage des bouttons du menu principal comme les bouttons start et exit.
		L'appelle a la fonction "draw" permet l'affichage a l'écran du menu principal.
		L'appelle a la fonction "exited" permet de savoir si l'on clique sur le bouton exit.
		L'appelle a la fonction "play" permet de savoir si l'on clique sur le bouton play.
	'''

	def __init__(self, screen, screen_size):

		self.screen = screen
		self.screen_size = screen_size

		self.start_btn = pygame.image.load("Assets/start_btn.png")
		self.start_btn_size = self.start_btn.get_size()
		self.start_button = Button((self.screen_size[0] // 2) - self.start_btn_size[0] // 2.5, (self.screen_size[1] // 2.8) - self.start_btn_size[1] // 2, self.start_btn, 0.8)
			
		self.exit_btn = pygame.image.load("Assets/exit_btn.png")
		self.exit_btn_size = self.exit_btn.get_size()
		self.exit_button = Button((self.screen_size[0] // 2) - self.exit_btn_size[0] // 2.5, (self.screen_size[1] // 2) - self.exit_btn_size[1] // 2, self.exit_btn, 0.8)

	def draw(self):
		self.start_button.draw(self.screen)
		self.exit_button.draw(self.screen)

	def exited(self):
		return self.exit_button.mouse_clicked()

	def play(self):
		return self.start_button.mouse_clicked()

class Selection_competence_droite:

	'''
		Cette class permet la création et l'affichage des bouttons de selections des compétences lors de la partie pour le joueur 2.
		Elle permet également renvoyer quel bouttons a été presser.
	'''

	def __init__(self, screen, screen_size):

		self.screen = screen
		self.screen_size = screen_size

		self.position = None
		self.pressed = None

		self.compet_1_droite = pygame.image.load("Assets\competence_1.png")
		self.competence_1_size_droite = self.compet_1_droite.get_size()
		self.competence_1_droite = Button((self.screen_size[0] // 2) + self.competence_1_size_droite[0], (self.screen_size[1] // 3.5) - self.competence_1_size_droite[1] // 2, self.compet_1_droite, 0.75)

		self.compet_2_droite = pygame.image.load("Assets\competence_2.png")
		self.competence_2_size_droite = self.compet_2_droite.get_size()
		self.competence_2_droite = Button((self.screen_size[0] // 2) + self.competence_2_size_droite[0], (self.screen_size[1] // 2.4) - self.competence_2_size_droite[1] // 2, self.compet_2_droite, 0.75)

		self.compet_3_droite = pygame.image.load("Assets\competence_3.png")
		self.competence_3_size_droite = self.compet_3_droite.get_size()
		self.competence_3_droite = Button((self.screen_size[0] // 2) + self.competence_3_size_droite[0], (self.screen_size[1] // 1.8) - self.competence_3_size_droite[1] // 2, self.compet_3_droite, 0.75)

		self.compet_4_droite = pygame.image.load("Assets\competence_4.png")
		self.competence_4_size_droite = self.compet_4_droite.get_size()
		self.competence_4_droite = Button((self.screen_size[0] // 2) + self.competence_4_size_droite[0], (self.screen_size[1] // 1.4) - self.competence_4_size_droite[1] // 1.5, self.compet_4_droite, 0.75)

		self.action_btn = pygame.image.load("Assets/action_button.png")
		self.action_btn_size = self.action_btn.get_size()
		self.action_button = Button((self.screen_size[0] // 2) - self.action_btn_size[0] // 2, self.screen_size[1] // 1.5, self.action_btn, 0.8)

		# Boutton selectionné

		self.compet_1_droite_selec = pygame.image.load("Assets\competence_1_selec.png")
		self.competence_1_size_droite_selec = self.compet_1_droite_selec.get_size()
		self.competence_1_droite_selec = Button((self.screen_size[0] // 2) + self.competence_1_size_droite_selec[0], (self.screen_size[1] // 3.5) - self.competence_1_size_droite[1] // 2, self.compet_1_droite_selec, 0.75)

		self.compet_2_droite_selec = pygame.image.load("Assets\competence_2_selec.png")
		self.competence_2_size_droite_selec = self.compet_2_droite_selec.get_size()
		self.competence_2_droite_selec = Button((self.screen_size[0] // 2) + self.competence_2_size_droite_selec[0], (self.screen_size[1] // 2.4) - self.competence_2_size_droite[1] // 2, self.compet_2_droite_selec, 0.75)

		self.compet_3_droite_selec = pygame.image.load("Assets\competence_3_selec.png")
		self.competence_3_size_droite_selec = self.compet_3_droite_selec.get_size()
		self.competence_3_droite_selec = Button((self.screen_size[0] // 2) + self.competence_3_size_droite_selec[0], (self.screen_size[1] // 1.8) - self.competence_3_size_droite[1] // 2, self.compet_3_droite_selec, 0.75)

		self.compet_4_droite_selec = pygame.image.load("Assets\competence_4_selec.png")
		self.competence_4_size_droite_selec = self.compet_4_droite_selec.get_size()
		self.competence_4_droite_selec = Button((self.screen_size[0] // 2) + self.competence_4_size_droite_selec[0], (self.screen_size[1] // 1.4) - self.competence_4_size_droite[1] // 1.5, self.compet_4_droite_selec, 0.75)

		self.action_btn = pygame.image.load("Assets/action_button.png")
		self.action_btn_size = self.action_btn.get_size()
		self.action_button = Button((self.screen_size[0] // 2) - self.action_btn_size[0] // 2, self.screen_size[1] // 1.5, self.action_btn, 0.8)



	def draw_on_screen(self):
		self.competence_1_droite.draw(self.screen)
		self.competence_2_droite.draw(self.screen)
		self.competence_3_droite.draw(self.screen)
		self.competence_4_droite.draw(self.screen)

		if self.pressed == 1:
			self.competence_1_droite_selec.draw(self.screen)
		elif self.pressed == 2:
			self.competence_2_droite_selec.draw(self.screen)
		elif self.pressed == 3:
			self.competence_3_droite_selec.draw(self.screen)
		elif self.pressed == 4:
			self.competence_4_droite_selec.draw(self.screen)

		self.action_button.draw(self.screen)

	def clic_btn1(self):
			return self.competence_1_droite.mouse_clicked()

	def clic_btn2(self):
		return self.competence_2_droite.mouse_clicked()

	def clic_btn3(self):
		return self.competence_3_droite.mouse_clicked()

	def clic_btn4(self):
		return self.competence_4_droite.mouse_clicked()

	def clic_action_btn(self):
		return self.action_button.mouse_clicked()

	def set_pressed(self, who):
		self.pressed = who

	def resset_pressed(self):
		self.pressed = None

class Selection_competence_gauche:

	'''
		Cette class permet la création et l'affichage des bouttons de selections des compétences lors de la partie pour le joueur 2.
		Elle permet également renvoyer quel bouttons a été presser
	'''

	def __init__(self, screen, screen_size):

		self.screen = screen
		self.screen_size = screen_size

		self.position = None
		self.pressed = None

		self.compet_1_gauche = pygame.image.load("Assets\competence_1.png")
		self.competence_1_size_gauche = self.compet_1_gauche.get_size()
		self.competence_1_gauche = Button(self.screen_size[0] // 4, (self.screen_size[1] // 3.5) - self.competence_1_size_gauche[1] // 2, self.compet_1_gauche, 0.75)

		self.compet_2_gauche = pygame.image.load("Assets\competence_2.png")
		self.competence_2_size_gauche = self.compet_2_gauche.get_size()
		self.competence_2_gauche = Button(self.screen_size[0] // 4, (self.screen_size[1] // 2.4) - self.competence_2_size_gauche[1] // 2, self.compet_2_gauche, 0.75)

		self.compet_3_gauche = pygame.image.load("Assets\competence_3.png")
		self.competence_3_size_gauche = self.compet_3_gauche.get_size()
		self.competence_3_gauche = Button(self.screen_size[0] // 4, (self.screen_size[1] // 1.8) - self.competence_3_size_gauche[1] // 2, self.compet_3_gauche, 0.75)

		self.compet_4_gauche = pygame.image.load("Assets\competence_4.png")
		self.competence_4_size_gauche = self.compet_4_gauche.get_size()
		self.competence_4_gauche = Button(self.screen_size[0] // 4, (self.screen_size[1] // 1.4) - self.competence_4_size_gauche[1] // 1.5, self.compet_4_gauche, 0.75)

		self.action_btn = pygame.image.load("Assets/action_button.png")
		self.action_btn_size = self.action_btn.get_size()
		self.action_button = Button((self.screen_size[0] // 2) - self.action_btn_size[0] // 2, self.screen_size[1] // 1.3, self.action_btn, 0.8)

		# Bouttons selectionné

		self.compet_1_gauche_selec = pygame.image.load("Assets\competence_1_selec.png")
		self.competence_1_size_gauche_selec = self.compet_1_gauche_selec.get_size()
		self.competence_1_gauche_selec = Button(self.screen_size[0] // 4, (self.screen_size[1] // 3.5) - self.competence_1_size_gauche[1] // 2, self.compet_1_gauche_selec, 0.75)

		self.compet_2_gauche_selec = pygame.image.load("Assets\competence_2_selec.png")
		self.competence_2_size_gauche_selec = self.compet_2_gauche_selec.get_size()
		self.competence_2_gauche_selec = Button(self.screen_size[0] // 4, (self.screen_size[1] // 2.4) - self.competence_2_size_gauche[1] // 2, self.compet_2_gauche_selec, 0.75)

		self.compet_3_gauche_selec = pygame.image.load("Assets\competence_3_selec.png")
		self.competence_3_size_gauche_selec = self.compet_3_gauche_selec.get_size()
		self.competence_3_gauche_selec = Button(self.screen_size[0] // 4, (self.screen_size[1] // 1.8) - self.competence_3_size_gauche[1] // 2, self.compet_3_gauche_selec, 0.75)

		self.compet_4_gauche_selec = pygame.image.load("Assets\competence_4_selec.png")
		self.competence_4_size_gauche_selec = self.compet_4_gauche_selec.get_size()
		self.competence_4_gauche_selec = Button(self.screen_size[0] // 4, (self.screen_size[1] // 1.4) - self.competence_4_size_gauche[1] // 1.5, self.compet_4_gauche_selec, 0.75)


	def draw_on_screen(self):

		self.competence_1_gauche.draw(self.screen)
		self.competence_2_gauche.draw(self.screen)
		self.competence_3_gauche.draw(self.screen)
		self.competence_4_gauche.draw(self.screen)

		if self.pressed == 1:
			self.competence_1_gauche_selec.draw(self.screen)
		elif self.pressed == 2:
			self.competence_2_gauche_selec.draw(self.screen)
		elif self.pressed == 3:
			self.competence_3_gauche_selec.draw(self.screen)
		elif self.pressed == 4:
			self.competence_4_gauche_selec.draw(self.screen)

		self.action_button.draw(self.screen)

	def clic_btn1(self):
		return self.competence_1_gauche.mouse_clicked() or self.competence_1_gauche_selec.mouse_clicked()

	def clic_btn2(self):
		return self.competence_2_gauche.mouse_clicked() or self.competence_2_gauche_selec.mouse_clicked()

	def clic_btn3(self):
		return self.competence_3_gauche.mouse_clicked() or self.competence_3_gauche_selec.mouse_clicked()

	def clic_btn4(self):
		return self.competence_4_gauche.mouse_clicked() or self.competence_4_gauche_selec.mouse_clicked()

	def clic_action_btn(self):
		return self.action_button.mouse_clicked()

	def set_pressed(self, who):
		self.pressed = who

	def resset_pressed(self):
		self.pressed = None

class Stats:

	'''
		Cette class permet d'afficher les statistique des personnages tel que les PV.
		L'appelle a la fonction "display_stats" permet l'affichage du texte a l'écran.
	'''

	def __init__(self, stat, x, y, screen):
		self.pv = stat[0]
		self.mana = stat[1]
		self.font = pygame.font.init()
		self.my_font = pygame.font.SysFont('Comic Sans MS', 69)

		self.x = x
		self.y = y
		self.screen = screen

	def display_stats(self):
		text_surface = self.my_font.render(f'PV : {self.pv}', True, (0, 0, 0))
		self.screen.blit(text_surface, (self.x, self.y))