#!/usr/bin/python

import time

def edit_line(line):
	if (line.find("Adding")) != -1:
		line = line.replace("Adding collectible ", "Item:")
	if (line.find("RNG Start")) != -1:
		line = line.replace("RNG Start ", "")
	return line

def find_lines(line):
	if (line.find("Adding")) != -1 or (line.find("Curse")) != -1 or (line.find("RNG Start")) != -1:
		return 1
	else:
		return 0

def write_lines(line):
	item_file = open("/nfs/zfs-student-3/users/2014/vdaviot/python/item_isaac/items.txt", "a+")
	item_file.seek(0, 2)
	if (find_lines(line)) == 1:
		newline = edit_line(line)
		item_file.write(newline)

def follow_file(fo):
	log = open(fo, "r")
	log.seek(0, 2)
	while True:
		line = log.readline()
		if not line:
			time.sleep(0.5)
		else:
			write_lines(line)
			continue

follow_file("/nfs/zfs-student-3/users/2014/vdaviot/python/item_isaac/log.txt")
