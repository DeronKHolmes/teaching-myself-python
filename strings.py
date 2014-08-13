#!/usr/bin/python
# Author: Deron K. Holmes
# Date: 8/13/14
# Purpose: Illustrate String Manipulation Functions

import string

message = "New string"
message2 = "New string"
message3 = "deron is a python programmer"
print message
print message, "contains", len(message), "characters."
print "The first character in", message, "is", message[0]
print "Example of slicing", message, message[0:4]

for letter in message:
	print letter


if message == message2:
	print "They match"
else:
	print "No match"

print message.upper()
print message.lower()
print string.capwords(message)
print string.capitalize(message)
print message.split(" ")
print string.join(message)
print string.capwords(message3)

#END