print ("guessing game")

from random import randint
lucknum = randint(1,100)

guess = int(input("What is your first guess? "))

listguess = []

if guess == lucknum:
	print("Congratulations")
	quit()
elif abs(guess-lucknum) <=10:
	print("Warm")
else:
	print("Cold")
listguess.append(guess)

while True:
	guess = int(input("What is your {} guess: ".format(len(listguess)+1)))
	if(guess==lucknum):
		print("Congratulations")
		break
	elif(abs(guess-lucknum)<abs(listguess[-1]-lucknum)):
		print("Warmer")
	else:
		print ("Cooler")
	listguess.append(guess)
print("Number of guesses: {}".format(len(listguess)))
for item in listguess:
	print (item)



	