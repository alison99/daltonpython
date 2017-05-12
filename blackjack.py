import random
import sys

#practice mode - no dealer
#print both cards you get
#ask if want hit or stand
#if hit, get new_card
#if stand, do nothing
#j, q, k = 10
#if has A, use as 11, unless >21 - then use 1
#if sum > 21, bust

#declarations
usercards = []
dealercards = []
busted = True
usertotal = 0
dealertotal = 0

#can add instructions = how to play?
def practice_module():
	#generate 2 cards
	usercards.append(new_card())
	usercards.append(new_card())
	print("your cards are:")
	i=0
	while i < len(usercards) : 
		print usercards[i]
		i+=1
	actionpractice()

def actionpractice():
	print("would you like to hit or stand?")
	response = raw_input()
	if response=="hit":
		hitpractice()
	elif response=="stand":
		standpractice()
	else:
		print("that is not allowed")

def action():
	print("would you like to hit or stand?")
	response = raw_input()
	if response=="hit":
		hit()
	elif response=="stand":
		stand()
	else:
		print("that is not allowed")

def hitpractice():
	#print usercards
	usercards.append(new_card())
	print("your cards are:")
	i=0
	while i < len(usercards) :
		print usercards[i]
		i+=1
	#check if bust
	bust()
	if busted==False:
		actionpractice()

def hit():
	#print usercards
	usercards.append(new_card())
	print("your cards are:")
	i=0
	while i < len(usercards) :
		print usercards[i]
		i+=1
	#check if bust
	bust()
	if busted==False:
		action()

def standpractice():
	print("you stood!")
	#check if bust
	bust()
	if busted==False:
		if usertotal<=21:	
			print("you won!")
			new_game()

def stand():
	print("you stood!")
	#check if bust
	bust()
	if busted==False:
		#if didn't bust compare with dealer
		#dealer hits until not possible
		while dealertotal<17:
			dealerhit()

		if dealertotal<=21:
			print("the dealer's total is:")
			print dealertotal
			print("your total is:")
			print usertotal
			if usertotal==dealertotal:
				print("push!")
				new_game()
			elif usertotal < dealertotal:
				print("you lost!")
				new_game()
			else:
				print("you won!")
				new_game()

def bust():
	global busted
	global usertotal
	usertotal = 0
	i=0
	while i < len(usercards):
		if usercards[i]=="J":
			usertotal += 10
		elif usercards[i]=="Q":
			usertotal += 10
		elif usercards[i]=="K":
			usertotal += 10
		elif usercards[i]=="A":
			usertotal += 11
		else:
			usertotal += usercards[i]
		i+=1
	print("your total is:")
	print usertotal
	if usertotal > 21:
		if 'A' in usercards:
			print("OR")
			usertotal -= 10
			print usertotal

			if usertotal > 21:
				print("you busted!")
				busted = True
				new_game()
			else:
				busted = False
		else:
			print("you busted!")
			busted = True
			new_game()
	#elif usertotal == 21:
		#new_game()
	else:
		busted = False


def new_game():
	del usercards[:]
	del dealercards[:]
	global usertotal
	global dealertotal
	global busted
	busted = True
	usertotal = 0
	dealertotal = 0

	print("would you like to play? (yes/no)")
	response = raw_input()
	if response=="yes":
		play()
	elif response=="no":
		print("would you like to practice instead? (yes/no)")
		response2 = raw_input()
		if response2=="yes":
			practice_module()
		else:
			print("thanks for playing!")
			sys.exit
	else:
		sys.exit

def play():
	dealer()
	usercards.append(new_card())
	usercards.append(new_card())
	print("your cards are:")
	i=0
	while i < len(usercards) : 
		print usercards[i]
		i+=1
	action()

def dealer():
	dealercards.append(new_card())
	dealercards.append(new_card())
	print("the dealer's cards are:")
	global dealertotal
	i=0
	while i < len(dealercards) : 
		if dealercards[i]=="J":
			dealertotal += 10
		elif dealercards[i]=="Q":
			dealertotal += 10
		elif dealercards[i]=="K":
			dealertotal += 10
		elif dealercards[i]=="A":
			dealertotal += 11
		else:
			dealertotal += dealercards[i]
		print dealercards[i]
		i+=1
	if dealertotal>21:
		print("the dealer has busted!")
		print("you won!")
		new_game()

def dealerhit():
	dealercards.append(new_card())
	global dealertotal
	dealertotal = 0
	i=0
	print("the dealer's cards are:")
	while i < len(dealercards) : 
		if dealercards[i]=="J":
			dealertotal += 10
		elif dealercards[i]=="Q":
			dealertotal += 10
		elif dealercards[i]=="K":
			dealertotal += 10
		elif dealercards[i]=="A":
			dealertotal += 11
		else:
			dealertotal += dealercards[i]
		print dealercards[i]
		i+=1

	if dealertotal>21:
		print("the dealer's total is:")
		print dealertotal
		print("the dealer has busted!")
		print("you won!")
		new_game()


#randomly generate number from 1 to 13
#if 11, 12, 13 print j, q, k
def new_card():
	card = random.randint(1,13)
	if card == 11:
		card = "J"
	elif card == 12:
		card = "Q"
	elif card == 13:
		card = "K"
	elif card == 1:
		card = "A"
	return card;

print("welcome to blackjack")

print("would you like to practice? (yes/no)")
response = raw_input()
if response =="yes":
	practice_module()
elif response =="no":
	print("would you like to play? (yes/no)")
	if raw_input()=="yes":
		play()
	else:
		print("goodbye!")
		sys.exit
