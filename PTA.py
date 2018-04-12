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

def wrapInt(i):
	if (i > 25):
		i = i % 26
		i = i + 97
		return i
	else:
		i = i + 97
		return i


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
	
	if (i % 9 == 0):
		element = plaintext[i] + x1
		element = chr(wrapInt(element))
		ciphertext += element
	
	if (i % 9 == 1):
		element = plaintext[i] + y1
		element = chr(wrapInt(element))
		ciphertext += element

	if (i % 9 == 2):
		element = plaintext[i] + z1
		element = chr(wrapInt(element))
		ciphertext += element

	if (i % 9 == 3):
		element = plaintext[i] + x2
		element = chr(wrapInt(element))
		ciphertext += element
			
	if (i % 9 == 4):
		element = plaintext[i] + y2
		element = chr(wrapInt(element))
		ciphertext += element
			
	if (i % 9 == 5):
		element = plaintext[i] + z2
		element = chr(wrapInt(element))
		ciphertext += element

	if (i % 9 == 6):
		element = plaintext[i] + x3
		element = chr(wrapInt(element))
		ciphertext += element
			
	if (i % 9 == 7):
		element = plaintext[i] + y3
		element = chr(wrapInt(element))
		ciphertext += element
			
	if (i % 9 == 8):
		element = plaintext[i] + z3
		element = chr(wrapInt(element))
		ciphertext += element

print("Ciphertext: {0}").format(ciphertext)
