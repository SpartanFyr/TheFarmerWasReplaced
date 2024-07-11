def Plant_carrot():
	reset()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Turf:
				harvest()
				till()
				plant(Entities.Carrots)
				move(North)
				trade(Items.Carrot_Seed)
			else:
				harvest()
				plant(Entities.Carrots)
				move(North)
				trade(Items.Carrot_Seed)
		move(East)
Plant_carrot()