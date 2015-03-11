#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down, pass it around, 98 bottles of beer on the wall.
import os

def drinkRon(n):
	for i in range(0, n):
		print n-i, "bottles of beer on the wall,", n-i, "bottles of beer"
		print"Take one down, pass it around,", n-i-1, "bottles of beer on the wall.\n"


drinkRon(99)