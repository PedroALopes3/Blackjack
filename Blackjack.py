from Deck import deck
import random


# Get info
User = input("Insira o seu username? ")
Money_inicial = input("Bem vindo " + User + "!!! \nQual o valor que pretendes apostar? ")
print(User + " " + Money_inicial + "$")

# Variaveis
gameover = False
Money = int(Money_inicial)
round_counter = 0
N_players = 2  # user 2 é o dealer
deck = deck()
y1 = 0
y2 = 0
cards = []
score = [[0 for i in range(N_players)]]
As = [[0 for i in range(N_players)]]
for i in range(N_players):
    cards.append([])


# game
while not gameover:

    #inicio da ronda
    round_counter += 1
    print("Round " + str(round_counter) + ":")
    round_bet = input(User + " quando queres apostar nesta ronda? ")
    Money -= int(round_bet)

    #atribuiçao de cartas
    y = 0
    for x in range(N_players):
        cards[x].append([])
        for u in range(2):
            y = 0
            while y == 0:
                y1 = random.randint(0, 3)
                y2 = random.randint(0, 12)
                if deck.cards[y1][y2] != 0:
                    y = 0
                else:
                    y = 1
            deck.cards[y1][y2] = x+1

            if 0 < y2 < 10:
                score[x] += y2+1
            elif y2 == 0:
                As[x] += 1
            else:
                score[x] += 10

            cards[x][round_counter-1].append((y1,y2))

    for a in range(N_players):
        print(Score[a])




    print(Money)
    print(cards)
    print(deck.cards)
    if Money <= 0:
        gameover = True
