#!/usr/bin/python3
'''
Write a method that determines if all the boxes can be opened.
'''


def getKeys(Boxes, keys):
	'''a recursive function to get all the keys in opened boxes'''
	updatedKeys = set()
	updatedKeys.update(keys)
	set_init_size = len(updatedKeys)

	for k in keys:
		if k < len(Boxes):
			updatedKeys.update(Boxes[k])

	if set_init_size != len(updatedKeys):
		return getKeys(Boxes, updatedKeys)
	else:
		return updatedKeys
	
def canUnlockAll(Boxes):
	'''check if all Boxes can be opened'''
	if len(Boxes) == 0:
		return False
	
	keys = getKeys(Boxes, [0])
	
	for i in range(len(Boxes)):
		if i not in keys:
			return False
	
	return True
	
