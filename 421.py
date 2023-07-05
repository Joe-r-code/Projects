import random

def roll_dice():
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	d3 = random.randint(1,6)
	rolls = [d1,d2,d3]
	return rolls
	
dr = roll_dice()	
	
print(dr)