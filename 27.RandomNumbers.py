import random

#print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9","J", "Q", "K", "A"]


#number = random.randint(1,6) #for a random integer we use this method
#a random number from 1 to 6

#randint() gjeneron një numër të plotë (integer) midis dy vlerave që i japim.
#ne kte rast i japim variabla.Mjafton qe ato te jene intiger
# number = random.randint(low,high)

#number = random.random() # random.random()	Numër decimal nga 0 deri para 1
#print(number)

#random.choice(list)	Zgjedh një element rastësisht
#option = random.choice(options) #this method will give a random choice from options
#print(option)

#Using the shuffle method we can shuffle this sequence
#Metoda shuffle() përdoret për të përzier në mënyrë rastësore elementet e një liste.

random.shuffle(cards)

print(cards)




