wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for x,y in wardrobe.items():
	for color in y:
		print("{} {}".format(color,x))