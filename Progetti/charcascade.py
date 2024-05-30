import random
import string
import time

stringa = ""

for ch in "Hello World!":
	for rnd in range(0, 60000):
		randomLetter = random.choice(string.ascii_letters)
		print(stringa + randomLetter)

	stringa += ch
	print(stringa)

#hello world