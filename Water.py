def water():
	if get_water() <= PERCENT:
		use_item(Items.Water_Tank)
