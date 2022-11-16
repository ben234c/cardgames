import deckofcards as doc # 52 cards
import random

for i in doc.cards:
    if i.number > 10:
        i.number = 10

def drawcard():
    x = random.randint(0, len(doc.cards) - 1)
    return doc.cards[x]

def hit(list):
    list.append(drawcard())

def cardsum(list):
    x = 0
    for i in list:
        x += (i.number)
    return x

score = 0

while (len(doc.cards)) >= 2:
    hand = []
    dealerhand = []
    hit(hand)
    hit(hand)
    stay = False

    while (cardsum(hand) < 21) and (stay == False):
        for i in hand:
            print(i.number, i.suit)
            if i in doc.cards:
                doc.cards.remove(i)
        
        print(cardsum(hand))
        hitstay = int(input('1 to Hit, 2 to Stay: '))

        print('----------------')

        if hitstay == 1:
            hit(hand)
        else:
            stay = True

    if stay == True:
        print('Dealer\'s Turn')
        hit(dealerhand)
        hit(dealerhand)

        while cardsum(dealerhand) <= 17:
            print(cardsum(dealerhand))
            for i in dealerhand:
                print(i.number, i.suit)
                if i in doc.cards:
                    doc.cards.remove(i)

            hit(dealerhand)
            print(cardsum(dealerhand))

            print('++++++++++++++++++')


    for i in hand:
        print(i.number, i.suit)
    print('Your Hand:', cardsum(hand))

    for i in dealerhand:
        print(i.number, i.suit)
    print('Dealer Hand:', cardsum(dealerhand))

    if cardsum(hand) > 21:
        print('Bust')
    elif cardsum(dealerhand) > 21:
        score += 1
        print('You Win, Dealer Bust, score =', score)
    elif (cardsum(hand) == 21) or (cardsum(hand) > cardsum(dealerhand)):
        score += 1
        print('You Win, score =', score)
    elif cardsum(hand) == (cardsum(dealerhand)):
        print('Tie')
    elif cardsum(hand) < cardsum(dealerhand):
        print('Dealer Wins')
    
    print('/////////////////')