def Plant_hay():
	reset()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				harvest()
				till()
				move(North)
			else:
				harvest()
				move(North)
		move(East)
Plant_hay()