from __builtins__.py import *
while True:
	reset()
	
	PERCENT = 0.65
	REQ = 100000
	
	
	#Grow Hay
	
	while num_items(Items.Hay) <= REQ:
		Plant_hay()
		
	#Grow Wood
	
	while num_items(Items.Wood) <= REQ:
		Plant_tree()
		
	#Grow Carrots
	
	while num_items(Items.Carrot) <= REQ:
		Plant_carrot()
	
	#Grow Pumpkins
			
	while num_items(Items.Pumpkin) <= REQ:
		Plant_pumpkins()