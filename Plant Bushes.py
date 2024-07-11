def Plant_bush():
	reset()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			harvest()
			plant(Entities.Bush)
			move(North)
		move(East)
Plant_bush()