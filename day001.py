import random

answer = random.randint(1, 100)
chance = 7

while chance!= 0:
	guess = int(input("Input number 1~100: "))
	if guess == answer:
		print(f'You win. Answer is {answer}')
		break
	elif guess > answer:
		print(f'{guess} is bigger than answer. \nChance left : {chance}')
		chance = chance -1
	else:
		print(f'{guess} is lower than answer. \n Chance left : {chance}')
		chance = chance -1


else:
	print(f'You lost. Answer is {answer}')