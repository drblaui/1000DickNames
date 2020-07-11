import random, time

#Big thanks to https://www.reddit.com/r/copypasta/comments/driz4z/a_thousand_ways_to_say_penis/

names = open("1000penis.txt", "r")
lines = names.readlines()

def getRandomDick():
	randLine = random.randint(1,999)
	return(lines[randLine].split('\n')[0])

def getNRandomDicks(number):
	for i in range(0,number):
		print(lines[random.randint(1,1000)].split('\n')[0])
		time.sleep(1)
