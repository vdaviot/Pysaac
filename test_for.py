#!/usr/bin/python2.7

string = "Hello Everyone"
for char in string:
	if char in "AEIOUYaeiouy":
		print(char)
	else:
		print("*")