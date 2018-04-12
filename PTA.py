#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#  PTA.py
#

import sys

p = 5
q = 3

x1 = ((2 * p*p) + (2 * p * q)) % 26
y1 = ((q*q) + (2 * p * q)) % 26
z1 = ((2 * p*p) + (q*q) + (2 * p * q)) % 26

x2 = ((2 * p*p) - (2 * p * q)) % 26
y2 = ((q*q) - (2 * p * q)) % 26
z2 = ((2 * p*p) + (q*q) - (2 * p * q)) % 26

x3 = (2 * p * q) % 26
y3 = ((p*p) - (q*q)) % 26
z3 = ((p*p) + (q*q)) % 26

plaintext = raw_input('Input plaintext to encrpyt: ')
ciphertext = ''

print("")
print("Plaintext:  {0}").format(plaintext)

plaintext = plaintext.lower()
plaintext = list(plaintext)

last = int(len(plaintext))

for i in range(0, last):
	if(plaintext[i] == ' '):
		ciphertext += ' '
		continue
		
	plaintext[i] = ord(plaintext[i]) - 97
	
	# i MOD 9 == 0 ~ x1
	if (i % 9 == 0):
		element = plaintext[i] + x1
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element
	
	# i MOD 9 == 1 ~ y1
	if (i % 9 == 1):
		element = plaintext[i] + y1
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element

	# i MOD 9 == 2 ~ z1
	if (i % 9 == 2):
		element = plaintext[i] + z1
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element

	# i MOD 9 == 3 ~ x2
	if (i % 9 == 3):
		element = plaintext[i] + x2
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element
			
	# i MOD 9 == 4 ~ y2
	if (i % 9 == 4):
		element = plaintext[i] + y2
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element
			
	# i MOD 9 == 5 ~ z2
	if (i % 9 == 5):
		element = plaintext[i] + z2
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element

	# i MOD 9 == 6 ~ x3
	if (i % 9 == 6):
		element = plaintext[i] + x3
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element
			
	# i MOD 9 == 7 ~ y3
	if (i % 9 == 7):
		element = plaintext[i] + y3
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element
			
	# i MOD 9 == 8 ~ z3
	if (i % 9 == 8):
		element = plaintext[i] + z3
		if (element > 25):
			element = element % 26
			element = element + 97
			element = chr(element)
			ciphertext += element
		else:
			element = element + 97
			element = chr(element)
			ciphertext += element

print("Ciphertext: {0}").format(ciphertext)
