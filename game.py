import random


def showinstructions():
    print('''
RPG Game
========
rooms - hall, kitchen, balcony; hell to quit.
Commands:
  go to [direction]
  get [item]
  
''')


def showstatus():
    print('---------------------------')
    print('player health = ', end="")
    print(playerhealth)
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "items" in rooms[currentRoom]:
        print("you see : ", end="")
        print(rooms[currentRoom]['items'])
    print("---------------------------")
    print("available exits are = " + str(rooms[currentRoom]['exits']))


inventory = []
monsters = {"evil slime": 100,
            "dragon": 500,
            "bascilisk": 150}
playerhealth = 300
healthpotion = 50
shieldhp =100


def fight(ph, mh, sh):
    playerhealth1 = ph
    monsterhealth1 = mh
    shieldhp = sh
    while True:
        print("player health = " + str(playerhealth1))
        print("monster health = " + str(monsterhealth1))
        if 'bronzesword' in inventory:
            playerdamage = random.randint(10, 20)
            print("player attacks the monster with bronze sword, damage dealt =" + str(playerdamage))
            monsterhealth1 -= playerdamage
            if monsterhealth1 <= 0:
                del rooms[currentRoom]['monster']
                print("monster has been killed")
                return playerhealth1
        if 'silversword' in inventory:
            print("player attacks the monster with silver sword")
            playerdamage = random.randint(18, 28)
            print("damage dealt =" + str(playerdamage))
            monsterhealth1 -= playerdamage
            if monsterhealth1 <= 0:
                del rooms[currentRoom]['monster']
                print("monster has been killed")
                return playerhealth1
        monsterdamage = random.randint(5, 10)
        if 'bronzeshield' in inventory:
            reduc = monsterdamage//5
            sh -= reduc
            monsterdamage -= reduc
        if 'silvershield' in inventory:
            reduc = (monsterdamage*2) // 5
            sh -= reduc
            monsterdamage -= reduc
        print("monster attacks you and deals " + str(monsterdamage) + "damage")
        playerhealth1 -= monsterdamage
        if playerhealth1 <= 0:
            return 0


rooms = {

    'hall': {
        'exits': ['kitchen', 'bedroom'],
        'items': ['bronzeshield', 'bronzesword']
    },

    'kitchen': {
        'exits': ['balcony', 'hall'],
        'monster': 'evil slime'
    },
    'balcony': {
        'exits': ['kitchen'],
        'items': ['healthpotion', 'armour', 'silversword'],
        'monster': 'bascilisk'
    },
    'bedroom': {
        'exits': ['hall'],
        'items': ['silvershield']
    }

}

currentRoom = 'hall'

showinstructions()


while True:
    showstatus()
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()
    if move[0] == 'go':
        if move[2] == 'hell':
            print("you have killed yourself you depressed piece of shit")
            break
        if move[2] in rooms[currentRoom]['exits']:
            currentRoom = move[2]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        if move[1] in rooms[currentRoom]['items']:
            if move[1] != 'healthpotion':
                inventory += [move[1]]
            print(move[1] + ' got!')
            lol = rooms[currentRoom]['items']
            lol.remove(move[1])
            rooms[currentRoom]['items'] = lol
        else:
            print('Can\'t get ' + move[1] + '!')
        if move[1] == 'healthpotion':
            if move[1] in rooms[currentRoom]['items']:
                if playerhealth >= 300:
                    print("your health is full")
                if playerhealth <= 250:
                    playerhealth += healthpotion
                    continue
                if playerhealth >= 250:
                    playerhealth = 300
            else:
                print("there is no healthpotion available")
        if (move[1] == 'silversword') and ('bronzesword' in inventory):
            swap = 'bronzesword'
            rooms[currentRoom]['items'].append(swap)
            inventory.remove(swap)

        if (move[1] == 'bronzesword') and ('silversword' in inventory):
            swap = 'silversword'
            rooms[currentRoom]['items'].append(swap)
            inventory.remove(swap)

    if 'monster' in rooms[currentRoom]:
        print("A " + rooms[currentRoom]['monster'] + " has appeared")
        monsterhealth = monsters[rooms[currentRoom]['monster']]

        playerhealth = fight(playerhealth, monsterhealth,100)
        if playerhealth <= 0:
            print("you have been killed")
            break
        else:
                print("you have " + str(playerhealth) + "hp left")




