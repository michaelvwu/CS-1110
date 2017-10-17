# Michael Wu (mvw5mf)
# Cesar Roucco-Montanez (cr3fd)

# What to be implemented: 1. Spirits/Characters, 2. Collectables, 3. Health Bar, 4. Sound/music, 5. Two players
import pygame
import gamebox
import random

character_score = 0
character_health = 100
computer_score = 0
computer_health = 100
game_on = False

camera = gamebox.Camera(800, 600)
backsheet = gamebox.load_sprite_sheet("http://openbookproject.net/thinkcs/python/english3e/_images/background.png",1,1)
sheet = gamebox.load_sprite_sheet("http://openbookproject.net/thinkcs/python/english3e/_images/duke_spritesheet.png", 1, 10)
sheet2 = gamebox.load_sprite_sheet("http://i.stack.imgur.com/WRTsK.png", 1, 8)
coin_sound = gamebox.load_sound("coin.wav")
scream_sound = gamebox.load_sound("scream1.wav")
frame = 0
frame2 = 0
counter = 0
counter2 = 0
back = gamebox.from_image(400, 300, backsheet[0])
character = gamebox.from_image(200, 200, sheet[frame])
computer = gamebox.from_image(500, 500, sheet2[frame2])
coin = gamebox.from_color(random.randint(200,500), random.randint(200,500), "yellow", 20, 20)
text = gamebox.from_text(400, 290, "Go to 10 to win!!!", "Courier New", 17, "white", True)


ground = gamebox.from_color(-100, 600, "black", 3000, 150)
character.yspeed = 0

enemies = [
    gamebox.from_color(random.randint(200,600), 0, "dark blue", 10, 10),
    gamebox.from_color(random.randint(200,600), 0, "dark blue", 10, 10),
    gamebox.from_color(random.randint(200,600), 0, "dark blue", 10, 10),
]



def tick(keys):
    # variables
    global game_on
    global character_score
    global character_health
    global computer_score
    global computer_health
    global frame
    global frame2
    global counter
    global counter2


    # animating sprite sheets for movement
    if frame >= 10:
        frame = 0
    character.image = sheet[frame]

    if frame2 >= 8:
        frame2 = 0
    computer.image = sheet2[frame2]

    # starting the game/activate the game
    if pygame.K_SPACE in keys:
        game_on = True

    #player 2 movement
    if pygame.K_d in keys:
        character.x += 5
        frame += 1
        counter += 1
    if pygame.K_a in keys:
        character.x -= 5
        frame += 1
        counter += 1
    if pygame.K_w in keys:
        character.yspeed = -10
        frame += 1
        counter += 1

    #Player 1 movement
    if pygame.K_RIGHT in keys:
        computer.x += 5
        frame2 += 1
        counter2 += 1
    if pygame.K_LEFT in keys:
        computer.x -= 5
        frame2 += 1
        counter2 += 1
    if pygame.K_UP in keys:
        computer.yspeed = -10
        frame2 += 1
        counter2 += 1

    # Start/Splash Screen
    if game_on is False:
        camera.draw(gamebox.from_color( 0, 0,"black",1600, 1200))
        camera.draw(text)
        camera.draw(gamebox.from_text(400, 200, "MOST RAD GAME EVER", "Courier New", 40, "Blue", True))
        camera.draw(gamebox.from_text(400, 380, "Press the SPACE bar to begin playing", "Courier New", 20, "orange", True))
        camera.draw(gamebox.from_text(400, 410, "Get the most coins!", "Courier New", 20, "orange", True))
        camera.draw(gamebox.from_text(400, 440, "Don't get hit by your opponent!", "Courier New", 20, "orange", True))
        camera.draw(gamebox.from_text(400, 470, "Don't get hit by the enemies!", "Courier New", 20, "orange", True))

    # Implements the game scenery and background items
    if game_on is True:
        camera.clear("white")
        camera.draw(back)
        camera.draw(character)
        camera.draw(computer)
        camera.draw(coin)
        camera.draw(gamebox.from_text(300, 50, "Score: " + str(character_score), "Courier New", 20, "purple", True))
        camera.draw(gamebox.from_text(100, 50, "Health: " + str(character_health),"Courier New", 20, "red", True))
        camera.draw(gamebox.from_color(100, 75, "red", int(character_health), 5))
        camera.draw(gamebox.from_text(500, 50, ("Score:" + str(computer_score)), "Courier New", 20, "red", True))
        camera.draw(gamebox.from_text(700, 50, ("Health:" + str(computer_health)), "Courier New", 20, "red", True))
        camera.draw(gamebox.from_color(700, 75, "red", int(computer_health), 5))

    camera.display()
    character.yspeed += 1
    character.y = character.y + character.yspeed
    computer.yspeed += 1
    computer.y = computer.y + computer.yspeed


    # Character interactions with game
    if character.bottom_touches(ground):
        character.yspeed = 0

    if character.touches(ground):
        character.move_to_stop_overlapping(ground)

    if character.touches(computer):
        character.move_to_stop_overlapping(computer)
        scream_sound.play()
        computer_health -= 5

    if game_on is True:
        for enemy in enemies:
            camera.draw(enemy)
            enemy.y += 15
            enemy.x += random.randint(-20,20)
            if enemy.y >= 600:
                enemy.y = 0
            if enemy.touches(character):
                scream_sound.play()
                character_health -= 5
                enemy.y = 0
                enemy.x = random.randint(200,600)
            if enemy.touches(computer):
                scream_sound.play()
                computer_health -= 5
                enemy.y = 0
                enemy.x = random.randint(200,600)

    if computer.bottom_touches(ground):
        computer.yspeed = 0

    if computer.touches(ground):
        computer.move_to_stop_overlapping(ground)

    if computer.touches(character):
        computer.move_to_stop_overlapping(character)
        scream_sound.play()
        character_health -= 5


    if character.touches(coin):
        coin_sound.play()
        character_score += 1
        coin.x = random.randint(100,700)
        coin.y = random.randint(150,450)

    if computer.touches(coin):
        coin_sound.play()
        computer_score += 1
        coin.x = random.randint(100, 700)
        coin.y = random.randint(150, 450)

    # Code on how game should end
    if character_score == 10:
        camera.draw(gamebox.from_color( 0, 0,"black",1600, 1200))
        camera.draw(gamebox.from_text(400, 260, "GAME OVER", "Courier New", 60, "Purple", True))
        camera.draw(gamebox.from_text(400, 330, "Player1 Wins!", "Courier New", 40, "Purple", True))
        gamebox.pause()
    if computer_score == 10:
        camera.draw(gamebox.from_color(0,0,"black",1600, 1200))
        camera.draw(gamebox.from_text(400, 260, "GAME OVER", "Courier New", 60, "Red", True))
        camera.draw(gamebox.from_text(400, 330, "Player2 Wins!", "Courier New", 40, "Red", True))
        gamebox.pause()
    if character_health <= 10:
        camera.draw(gamebox.from_color(0, 0, "black", 1600, 1200))
        camera.draw(gamebox.from_text(400, 260, "GAME OVER", "Courier New", 60, "Purple", True))
        camera.draw(gamebox.from_text(400, 330, "Player2 Wins!", "Courier New", 40, "Purple", True))
        gamebox.pause()
    if computer_health <= 10:
        camera.draw(gamebox.from_color(0, 0, "black", 1600, 1200))
        camera.draw(gamebox.from_text(400, 260, "GAME OVER", "Courier New", 60, "Purple", True))
        camera.draw(gamebox.from_text(400, 330, "Player1 Wins!", "Courier New", 40, "Purple", True))
        gamebox.pause()
    camera.display()

ticks_per_second = 30



# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)