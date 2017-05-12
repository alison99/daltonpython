#just start typing here?


#make a new deck - get number of decks and shuffle
import random
def new_deck(n):
	#i starts from 0
	cards = n*52
	deck = [[i] for i in range(cards)]
	random.shuffle(deck)
	deck[i] % 4;

	print(deck)

new_deck(1);
