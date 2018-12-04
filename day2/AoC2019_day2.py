data = open("input", "r")
boxes = data.readlines()
boxes = [line.rstrip() for line in boxes]
boxes[:5]

e2 = 0
e3 = 0

for box in boxes:
	be2 = False
	be3 = False
	for letter in box:
		if box.count(letter) == 2:
			be2 = True
		elif box.count(letter) == 3:
			be3 = True
		else:
			continue
	if be2:
		e2 += 1

	if be3:
		e3 += 1

print(e2, e3, e2 * e3)

boxes.sort()

# -----

import Levenshtein

for i in range(len(boxes)-1):

	ld = Levenshtein.distance(boxes[i], boxes[i+1])
	if ld == 1:
		print(boxes[i])
		print(boxes[i+1])
		print(ld)


lufjygedpvfbhftxiwnaorzmq