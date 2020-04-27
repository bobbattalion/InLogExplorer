from os import *
import msvcrt
import random

import BSP
import enemy

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

system("title InLogExplorer")
system("mode con:cols=80 lines=30")

clear()

playerx = 1
playery = 1

playerchar = 10

####pstats####
plevel = 1
pattack = 1
pdefence = 1
pscore = 0
pfloor = 1

maxammo = 10
ammo = maxammo

maxhealth = 20
health = maxhealth

def getTile(x, y, display):
    if(y >= 0 and y < len(display) and x >= 0 and x < len(display[0])):
       return display[y][x]

    else:
       return 1

def setTile(x, y, display, char):
    if(y >= 0 and y < len(display) and x >= 0 and x < len(display[0])):
       display[y][x] = char

def show(display):
    clear()
    out = []
    for k in range(len(display)):
        if(k >= cameray and k < cameray + visibletilesy):
            newstring = ""
            for i in range(len(display[k])):
                if(i >= camerax and i < camerax + visibletilesx):
                    if(display[k][i] == 0):
                        newstring += " "

                    elif(display[k][i] == 1):
                        newstring += "█"

                    elif(display[k][i] == 2):
                        newstring += "▒"

                    elif(display[k][i] == 3):
                        newstring += "*"

                    elif(display[k][i] == 4):
                        newstring += "="

                    elif(display[k][i] == 5):
                        newstring += "@"

                    elif(display[k][i] == 6):
                        newstring += "©"

                    elif(display[k][i] == 7):
                        newstring += "░"

                    elif(display[k][i] == 8):
                        newstring += "+"

                    elif(display[k][i] == 9):
                        newstring += "▓"

                    elif(display[k][i] == 10):
                        newstring += "┼"

                    else:
                        newstring += str(display[k][i])

            out.append(newstring)

    for i in out:
        print(i)

dungeon = BSP.Generator(150, 150)
dungeon.generatemap()

display = dungeon.returnmap()

val = False
while(not val):
    playerx = random.randint(0, len(display[0]) - 1)
    playery = random.randint(0, len(display) - 1)

    if(display[playery][playerx] == 0):
        val = True

enemies = []
for i in range(pfloor * 15):
    y = random.randint(0, len(display)-1)
    x = random.randint(0, len(display[0])-1)
    while(display[y][x] != 0 or (y == playery and x == playerx)):
        y = random.randint(0, len(display)-1)
        x = random.randint(0, len(display[0])-1)
    enemies.append(enemy.enemyC(x, y, pfloor))

val = False
while(not val):
    portalx = random.randint(0, len(display[0]) - 1)
    portaly = random.randint(0, len(display) - 1)

    if(display[portaly][portalx] == 0):
        val = True

portalchar = 5

visibletilesx = 61
visibletilesy = 19


xoffset = int((visibletilesx - 1)/2)
yoffset = int((visibletilesy - 1)/2)

camerax = 0
cameray = 0

gunrange = 4

def turn():
    global turncount
    turncount += 1

show(display)

turncount = 0
run = True
while(run):
    playerin = msvcrt.getch()
    remove = False

    if(playerin == b'w'):
        if(getTile(playerx, playery - 1, display) == 0 or getTile(playerx, playery - 1, display) == 6):
            if(getTile(playerx, playery - 1, display) == 6):
               pscore = pscore + 10
            setTile(playerx, playery, display, 0)
            playery = playery - 1
            turn()

    elif(playerin == b's'):
        if(getTile(playerx, playery + 1, display) == 0 or getTile(playerx, playery + 1, display) == 6):
            if(getTile(playerx, playery + 1, display) == 6):
               pscore = pscore + 10
            setTile(playerx, playery, display, 0)
            playery = playery + 1
            turn()

    elif(playerin == b'a'):
        if(getTile(playerx - 1, playery, display) == 0 or getTile(playerx - 1, playery, display) == 6):
            if(getTile(playerx - 1, playery, display) == 6):
               pscore = pscore + 10
            setTile(playerx, playery, display, 0)
            playerx = playerx - 1
            turn()

    elif(playerin == b'd'):
        if(getTile(playerx + 1, playery, display) == 0 or getTile(playerx + 1, playery, display) == 6):
            if(getTile(playerx + 1, playery, display) == 6):
               pscore = pscore + 10
            setTile(playerx, playery, display, 0)
            playerx = playerx + 1
            turn()

    camerax = playerx - xoffset
    cameray = playery - yoffset

    if(cameray <= 0):
        cameray = 0

    if(camerax <= 0):
        camerax = 0

    if(camerax >= len(display[0]) - visibletilesx):
        camreax = len(display[0]) - visibletilesx

    if(cameray >= len(display) - visibletilesy):
        cameray = len(display) - visibletilesy

    if(playerin == b'M'):
        if(ammo > 0):
            x = 1
            removex = []
            removey = []
            while(x < gunrange + 1):
                if(display[playery][playerx + x] != 0 and display[playery][playerx + x] != 4):
                    break
                setTile(playerx + x, playery, display, 3)
                removex.append(playerx + x)
                removey.append(playery)
                x = x + 1


            remove = True
            turn()
            ammo -= 1

    elif(playerin == b'P'):
        if(ammo > 0):
            x = 1
            removex = []
            removey = []
            while(x < gunrange + 1):
                if(display[playery + x][playerx] != 0 and display[playery + x][playerx] != 4):
                    break
                setTile(playerx, playery + x, display, 3)
                removex.append(playerx)
                removey.append(playery + x)
                x = x + 1

            remove = True
            turn()
            ammo -= 1

    elif(playerin == b'K'):
        if(ammo > 0):
            x = 1
            removex = []
            removey = []
            while(x < gunrange + 1):
                if(display[playery][playerx - x] != 0 and display[playery][playerx - x] != 4):
                    break
                setTile(playerx - x, playery, display, 3)
                removex.append(playerx - x)
                removey.append(playery)
                x = x + 1

            remove = True
            turn()
            ammo -= 1

    elif(playerin == b'H'):
        if(ammo > 0):
            x = 1
            removex = []
            removey = []
            while(x < gunrange + 1):
                if(display[playery - x][playerx] != 0 and display[playery - x][playerx] != 4):
                    break
                setTile(playerx, playery - x, display, 3)
                removex.append(playerx)
                removey.append(playery - x)
                x = x + 1

            remove = True
            turn()
            ammo -= 1

##    tester.moveEnemy(playerx, playery, display)
##    tester.checkHit(display)
##    health = health - tester.checkPlayer(playerx, playery)

    walls = []
    for y in range(len(display)):
        for x in range(len(display[y])):
            if(display[y][x] != 0 and display[y][x] != 6 and display[y][x]):
                walls.append([x, y])

            elif(display[y][x] == 10):
                start = [x, y]

    for i in range(len(enemies)):
        enemies[i].moveEnemy(display, walls, playerx, playery)
        pscore = pscore + enemies[i].checkHit(display)
        health = health - enemies[i].checkPlayer(playerx, playery)
        enemies[i].showEnemy(display)

    setTile(playerx, playery, display, playerchar)
    setTile(portalx, portaly, display, portalchar)

##    tester.showEnemy(display)

    show(display)

    for i in range(len(enemies)):
        enemies[i].replaceChar(display)

    if(getTile(playerx - 1, playery - 1, display) == 5 or getTile(playerx - 1, playery, display) == 5 or getTile(playerx - 1, playery + 1, display) == 5 or getTile(playerx, playery - 1, display) == 5 or getTile(playerx, playery + 1, display) == 5 or getTile(playerx + 1, playery - 1, display) == 5 or getTile(playerx + 1, playery, display) == 5 or getTile(playerx + 1, playery + 1, display) == 5):
        pfloor = pfloor + 1

        dungeon = BSP.Generator(150, 150)
        dungeon.generatemap()

        display = dungeon.returnmap()

        val = False
        while(not val):
            playerx = random.randint(0, len(display[0]) - 1)
            playery = random.randint(0, len(display) - 1)

            if(display[playery][playerx] == 0):
                val = True

        enemies = []
        for i in range(pfloor * 15):
            y = random.randint(0, len(display)-1)
            x = random.randint(0, len(display[0])-1)
            while(display[y][x] != 0 or (y == playery and x == playerx)):
                y = random.randint(0, len(display)-1)
                x = random.randint(0, len(display[0])-1)
            enemies.append(enemy.enemyC(x, y, pfloor))

        val = False
        while(not val):
            portalx = random.randint(0, len(display[0]) - 1)
            portaly = random.randint(0, len(display) - 1)

            if(display[portaly][portalx] == 0):
                val = True

        camerax = playerx - xoffset
        cameray = playery - yoffset

        if(cameray <= 0):
            cameray = 0

        if(camerax <= 0):
            camerax = 0

        if(camerax >= len(display[0]) - visibletilesx):
            camreax = len(display[0]) - visibletilesx

        if(cameray >= len(display) - visibletilesy):
            cameray = len(display) - visibletilesy

        for i in range(len(enemies)):
            enemies[i].showEnemy(display)

        setTile(playerx, playery, display, playerchar)
        setTile(portalx, portaly, display, portalchar)

        show(display)

    num = int((visibletilesx - 5)/2)
    print("#" * num, "STATS", "#" * num, sep = "")

    if(pscore == plevel * 100):
        plevel = plevel + 1
        pattack = pattack + random.randint(1, plevel)
        pdefence = pdefence + random.randint(1, plevel)
        statup = random.randint(0, 1)
        if(statup == 1):
            maxammo = maxammo + 1

        else:
            maxhealth = maxhealth + 1

        print("Level Up")

    if(turncount % 25 == 0):
        if(health < maxhealth):
            health = health + 1
            print("Health Up")

        elif(ammo < maxammo):
            ammo = ammo + 1
            print("Ammo Up")

    print("Level: ", plevel)
    print("Floor: ", pfloor)
    print("Health: ", health, "/", maxhealth)
    print("Ammo: ", ammo, "/", maxammo)
    print("Attack: ", pattack)
    print("Defence: ", pdefence)
    print("Score: ", pscore)

    if(remove):
        for i in range(len(removex)):
            setTile(removex[i], removey[i], display, 0)
