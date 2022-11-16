# Use classes to make a deck of cards

class PlayingCard():
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

suits = ['Spade', 'Club', 'Heart', 'Diamond']
numbers = list(range(1, 14))
cards = []

for i in suits:
    for j in numbers:
        x = PlayingCard(i, j)
        cards.append(x)

# for i in cards:
  #   print(i.suit, i.number)