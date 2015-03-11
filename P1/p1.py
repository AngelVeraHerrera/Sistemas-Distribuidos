#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down, pass it around, 98 bottles of beer on the wall.
import os

def drinkRon(n):
	for i in reversed(range(1, n)):
		print i, "bottles of beer on the wall,", i, "bottles of beer"
		print"Take one down, pass it around,", i-1, "bottles of beer on the wall.\n"


drinkRon(100)