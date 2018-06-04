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

def wrapOrd(i):
	if (i > 25):
		i = i % 26
		i = i + 97
		return i
	else:
		i = i + 97
		return i

def encrypt():
        print("[+] ENCRYPTING")
        plaintext = raw_input('Input plaintext to encrpyt: ')
        ciphertext = ''
        print("")
        print("Plaintext:  {0}").format(plaintext)
        
        plaintext = plaintext.lower()
        plaintext = list(plaintext)

        last = int(len(plaintext))
        
        for i in range(0, last):
                
                plaintext[i] = ord(plaintext[i]) - 97
                
                if (i % 9 == 0):
                        element = plaintext[i] + x1
                        element = chr(wrapOrd(element))
                        ciphertext += element
                
                if (i % 9 == 1):
                        element = plaintext[i] + y1
                        element = chr(wrapOrd(element))
                        ciphertext += element

                if (i % 9 == 2):
                        element = plaintext[i] + z1
                        element = chr(wrapOrd(element))
                        ciphertext += element

                if (i % 9 == 3):
                        element = plaintext[i] + x2
                        element = chr(wrapOrd(element))
                        ciphertext += element
                                
                if (i % 9 == 4):
                        element = plaintext[i] + y2
                        element = chr(wrapOrd(element))
                        ciphertext += element
                                
                if (i % 9 == 5):
                        element = plaintext[i] + z2
                        element = chr(wrapOrd(element))
                        ciphertext += element

                if (i % 9 == 6):
                        element = plaintext[i] + x3
                        element = chr(wrapOrd(element))
                        ciphertext += element
                                
                if (i % 9 == 7):
                        element = plaintext[i] + y3
                        element = chr(wrapOrd(element))
                        ciphertext += element
                                
                if (i % 9 == 8):
                        element = plaintext[i] + z3
                        element = chr(wrapOrd(element))
                        ciphertext += element
                        
        return ciphertext

def decrypt():
        print("[+] DECRYPTING")
        ciphertext = raw_input('Input ciphertext to decrpyt: ')
        plaintext = ''
        print("")
        print("Ciphertext:  {0}").format(ciphertext)

        ciphertext = ciphertext.lower()
        ciphertext = list(ciphertext)

        last = int(len(ciphertext))
        
        for i in range(0, last):
                
                ciphertext[i] = ord(ciphertext[i]) - 97
                
                if (i % 9 == 0):
                        element = ciphertext[i] - x1
                        element = chr(wrapOrd(element))
                        plaintext += element
                
                if (i % 9 == 1):
                        element = ciphertext[i] - y1
                        element = chr(wrapOrd(element))
                        plaintext += element

                if (i % 9 == 2):
                        element = ciphertext[i] - z1
                        element = chr(wrapOrd(element))
                        plaintext += element

                if (i % 9 == 3):
                        element = ciphertext[i] - x2
                        element = chr(wrapOrd(element))
                        plaintext += element
                                
                if (i % 9 == 4):
                        element = ciphertext[i] - y2
                        element = chr(wrapOrd(element))
                        plaintext += element
                                
                if (i % 9 == 5):
                        element = ciphertext[i] - z2
                        element = chr(wrapOrd(element))
                        plaintext += element

                if (i % 9 == 6):
                        element = ciphertext[i] - x3
                        element = chr(wrapOrd(element))
                        plaintext += element
                                
                if (i % 9 == 7):
                        element = ciphertext[i] - y3
                        element = chr(wrapOrd(element))
                        plaintext += element
                                
                if (i % 9 == 8):
                        element = ciphertext[i] - z3
                        element = chr(wrapOrd(element))
                        plaintext += element
                        
        return plaintext

encrypted_data = encrypt()
print("Encrypted data: {}\n").format(encrypted_data)
decrypted_data = decrypt()
print("Decrypted data: {}\n").format(decrypted_data)
