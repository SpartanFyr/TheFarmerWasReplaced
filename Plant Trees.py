def Plant_tree():
	reset()
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			water()
			if (x+y) % 2 == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			else:
				if can_harvest():
					harvest()
				plant(Entities.Bush)
			move(North)
		move(East)