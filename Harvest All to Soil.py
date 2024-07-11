def Harvest_to_soil():
	reset()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				till()
				harvest()
				move(North)
			else:
				harvest()
				move(North)
		move(East)
Harvest_to_soil()