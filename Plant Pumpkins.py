def Plant_pumpkins():
	reset()
	i = 0
	while i in range(5):
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if get_ground_type() == Grounds.Turf:
					till()
					plant(Entities.Pumpkin)
					water()
					move(North)
					trade(Items.Pumpkin_Seed)
				elif can_harvest():
					move(North)
				else:
					plant(Entities.Pumpkin)
					water()
					move(North)
					trade(Items.Pumpkin_Seed)
			move(East)
			i += 1
	harvest()
Plant_pumpkins()
	