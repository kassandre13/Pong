import pygame,sys,random # (sys = systeme; sert surtout a fermer le progamme, random = direction de la balle)

def ball_anim(): # animation de la balle (vitesse...)
   global ball_vitesse_x,ball_vitesse_y
   ball.x += ball_vitesse_x
   ball.y += ball_vitesse_y 

   if ball.top <= 0 or ball.bottom >=window_height:
      ball_vitesse_y *= -1
   if ball.left <= 0 or ball.right >= window_width:
      ball_restart()
   
   if ball.colliderect(player) or ball.colliderect(opponent):
      ball_vitesse_x *= -1

def player_anim(): # animation de la barre (joueur)
   player.y += player_speed      
   if player.top <= 0:
      player.top = 0
   if player.bottom >= window_height :
      player.bottom = window_height

def opponent_ai():
   if opponent.top < ball.y:
      opponent.top += opponent_vitesse
   if opponent.bottom > ball.y:
      opponent.bottom -= opponent_vitesse
   if opponent.top <= 0:
      opponent.top = 0
   if opponent.bottom >= window_height :
      opponent.bottom = window_height

def ball_restart(): # quand on perd la balle reviens au milieu
   global ball_vitesse_x, ball_vitesse_y
   ball.center = (window_width/2,window_height/2)
   ball_vitesse_y *= random.choice((1,-1))
   ball_vitesse_x *= random.choice((1,-1))




pygame.init()
clock = pygame.time.Clock() # variable qui sert a delimiter le nombre d'image par sec (voir en bas pour plus d'explication)

# creation fenetre 

window_width= 1280
window_height = 960
window_height= pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('pong')

ball = pygame.Rect(window_width/2 - 15,window_height/2 - 15,30,30)
player = pygame.Rect(window_width - 20,window_height/2 - 70,10,140)
opponent = pygame.Rect(10,window_height/2 - 70,10,140)

color_principal = pygame.Color('grey12')
light_grey = (200,200,200)

# Jeu

ball_vitesse_x = 7 *random.choice((1,-1))
ball_vitesse_y = 7 *random.choice((1,-1))
player_vitesse = 0
opponent_vitesse = 7

while True: # boucle qui sert a fermer le programme...

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            player_speed += 7
         if event.key == pygame.K_UP:
            player_speed -=7
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            player_speed -= 7
         if event.key == pygame.K_UP:
            player_speed +=7

   ball_anim()
   player_anim()
   opponent_ai()

   

# background du jeu 

   window.fill(color_principal)
   pygame.draw.rect(window,light_grey,player)
   pygame.draw.rect(window,light_grey,opponent)
   pygame.draw.ellipse(window,light_grey,ball) 
   pygame.draw.aaline(window,light_grey,(window_width/2,0), (window_width/2,window_height))


   pygame.display.flip()
   clock.tick(60) # permet d'indiquer le nombre maximal d'images affichées par seconde et ainsi de limiter et de contrôler la vitesse (soit ici 60)