import random
import time

while True:
	dSides = raw_input("How many sides should the dice have? : ")
	rollAgain = ""
	
	if dSides.lower() == "q" or dSides.lower() == "quit":
		break

	elif dSides.isdigit():
		print "Rolling dice..."
		time.sleep(1)
		diceRoll = random.randint(1, int(dSides))
		print "Your dice roll is %s" % diceRoll
		rollAgain = raw_input("Would you like to roll again? : ")
		if rollAgain.lower() == "yes" or rollAgain.lower() == "y":
			True
		if rollAgain.lower() != "yes" or rollAgain.lower() == "y":
			break

	elif dSides.isdigit() == False:
		print "That was not a number, please enter a number without a decimal place"
