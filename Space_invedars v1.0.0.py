# به اسم الله رحمان رحیم


# techer = MR.tabari
# thanks MR.tabri for your nice teaching


# import the libs:

# import pygame lib
import pygame
from pygame import mixer

# importing the random lib
import random


# import math lib
import math


# start pygame lib
pygame.init()


# i can't make commant for this code _____
with open("-5969627372829233348", "r") as file:
    no_name = file.read()


# score:
player_score = 0

# set a font for game
font = pygame.font.Font("assets/Font/game.ttf", 25)

# set x and y for score text
text_x = 20
text_y = 20


# a var for saving best score
player_Best_score = no_name

# set a font for game
font_best = pygame.font.Font("assets/Font/game.ttf", 35)

# set x and y for score text
text_best_x = 30
text_best_y = 65


# game over:
game_over_time = False


# set a font for game over text
over = pygame.font.Font("assets/Font/game.ttf", 64)

# set x and y for score text
text_over_x = 200
text_over_y = 250


# game sound:
pygame.mixer.music.load("assets/sounds/game_music.wav")
pygame.mixer.music.play(-1)


# funs(functions): 


# a fun(function) for showing the best score text
def score_best(x, y):
    score_best_TXT = font_best.render("best score : " + str(player_Best_score), True, (0, 255, 0))
    main_screen.blit(score_best_TXT, (x, y))


# a fun(function) for best score
def best_score_check(new_score, best_score):
    global player_Best_score
    if new_score > int(best_score):
        player_Best_score = new_score
        with open("-5969627372829233348", "w") as file :
            file.write(f"{player_Best_score}")


# a fun(function) for showing the score text
def score(x, y):
    score_TXT = font.render("score : " + str(player_score), True, (255, 255, 255))
    main_screen.blit(score_TXT, (x, y))


# a fun(function) for showing the game over text
def game_over(x, y):
    global game_over_time, player_score
    over_TXT = over.render("GaMe OvEr", True, (255, 0, 0))
    main_screen.blit(over_TXT, (x, y))
    game_over_time = True
    best_score_check(player_score, player_Best_score)
    player_score = 0


# a fun(function) for showing the player image at main screeen
def Player(x, y):
    main_screen.blit(Player_img, (x, y))


# a fun(function) for showing the space invader image at main screeen
def Space_invader(x, y, X_Y):
    main_screen.blit(Space_invader_image[X_Y], (x, y))


# a fun(function) for showing the Bullet image at main screeen
def Fire_Bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    main_screen.blit(Bullet_image, (x + 16, y + 10))


def BulletCollisin(SpaceInvader_X, SpaceInvader_Y, BulletX, BulletY):
    distance = math.sqrt((math.pow(SpaceInvader_X - BulletX, 2)) + (math.pow(SpaceInvader_Y - BulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# set the Width and Height for screen in 2 vars
Width, Height = 800, 600


# Set the seting of the screen:

# set the game title in to a var
title = "Space Invaders"
# load icon picture in a var
icon = pygame.image.load("assets/img/icon/icon.png")


# player: 

# load the player image in to a var and also set the X and Y data to a var
Player_img = pygame.image.load("assets/img/Player/Player.png")
Player_X, Player_Y = 370, 480
Player_X_Change = 0


# Space invader:


# make a list(Array) for multipel of space inveders
Space_invader_image = []
Space_invader_X = []
Space_invader_Y = []
Space_invader_X_change = []
Space_invader_Y_change = []
number_of_space_inveders = 6


# load thre Space invader image in to a var and also set the X and Y data to a var
for i in range(number_of_space_inveders):
    Space_invader_image.append(pygame.image.load("assets/img/Space Invader/space_inbader3.png"))
    Space_invader_X.append(random.randint(0, 735))
    Space_invader_Y.append(random.randint(50, 150))
    Space_invader_X_change.append(0.3585)
    Space_invader_Y_change.append(40)


# Bullet :

# load thre Bullet image in to a var and also set the X and Y data to a var and set the stuts of the bullet
Bullet_image = pygame.image.load("assets/img/Bullet/bullet.png")
Bullet_X, Bullet_Y = 0, 480
Bullet_X_change, Bullet_Y_change = 0, 0.68
bullet_state = "ready"


# set the background image to var
backGround_img = pygame.image.load("assets/img/background/background.png")


# set the game status to True (start the game)
boot = True


# make the game screen
main_screen = pygame.display.set_mode((Width, Height))


# change the game icon
pygame.display.set_icon(icon)


# change game title
pygame.display.set_caption(title)


# set game speed
clock = pygame.time.Clock()


# check the game status
while boot:

    # the event var get the data of the events
    for event in pygame.event.get():


        # check type of events if it's QUIT off the pygame lib and set the game status to False 
        if event.type == pygame.QUIT:
            boot = False
            pygame.quit()
        

        # check type of events if it's key down(down any key) ... : 
        if event.type == pygame.KEYDOWN:

            # check if the event is right key ... :
            if event.key == pygame.K_RIGHT:
                Player_X_Change = 0.3585
            
            # if the key is Lef key ... :
            if event.key == pygame.K_LEFT:
                Player_X_Change = -0.3585


            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    Bullet_Sound = mixer.Sound("assets/sounds/Bullet.wav")
                    Bullet_Sound.play()
                    Bullet_X = Player_X
                    Fire_Bullet(Bullet_X, Bullet_Y)


            if event.key == pygame.K_r:
                if game_over_time == True:
                    for i in range(number_of_space_inveders):
                        Space_invader_X[i] = random.randint(0, 735)
                        Space_invader_Y[i] = random.randint(50, 150)
                game_over_time == False

        # check type of events if it's key UP(UP any key) ... : 
        if event.type == pygame.KEYUP:

            # if the event is lef or right key , set the moving of Player to False :
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                Player_X_Change = 0


    # x of Player:

    Player_X += Player_X_Change
    # checkin crashing the player image th the wall or not ... :
    if Player_X <= 0:
        Player_X = 0

        
    elif Player_X  >= 736:
        Player_X = 736


    # showing objects:

    # showing the background image
    main_screen.blit(backGround_img, (0, 0))


    # showing, moving and lowing the speed of Bullet, make multiplay of the Bullet
    if Bullet_Y <= 0:
        Bullet_Y = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        Fire_Bullet(Bullet_X, Bullet_Y)
        Bullet_Y -= Bullet_Y_change


    # showing the Player
    Player(Player_X, Player_Y)


    # x of space invader:


    # checkin crashing the player image th the wall or not ... :
    for i in range(number_of_space_inveders):


        if Space_invader_Y[i] > 440:
            for b in range(number_of_space_inveders):
                Space_invader_Y[b] = 2000
            game_over(text_over_x, text_over_y)


        Space_invader_X[i] += Space_invader_X_change[i]
        if Space_invader_X[i] <= 0:
            Space_invader_X_change[i] = 0.3585
            Space_invader_Y[i] += Space_invader_Y_change[i]
        elif Space_invader_X[i] >= 736:
            Space_invader_X_change[i] = -0.3585 
            Space_invader_Y[i] += Space_invader_Y_change[i]


        # cheack collision of Bullet to Space inviders
        Collisin = BulletCollisin(Space_invader_X[i], Space_invader_Y[i], Bullet_X, Bullet_Y)
        if Collisin:
            Space_inveders_Sound = mixer.Sound("assets/sounds/space_inveder_died.wav")
            Space_inveders_Sound.play()
            Bullet_Y = 480
            bullet_state = "ready"
            player_score += 1
            Space_invader_X[i], Space_invader_Y[i] = random.randint(0, 735), random.randint(50, 150)

        # showing the Space invader
        Space_invader(Space_invader_X[i], Space_invader_Y[i], i)

    # showing the score
    score(text_x, text_y)


    # showing best score
    score_best(text_best_x, text_best_y)


    # update the main screen
    pygame.display.update() 

    clock.tick(999)
