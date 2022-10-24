"""Write a python program to compute RSA.
Your primes should be between 200 and 400.
Use math.gcd() to verify a choice for e.
find d, according to my notes, or if you can think of a better way"""
import math
import random
import sympy as sympy

"""define multiplicative inverse- part of private key, is
a number that when multiplied by original number gives product as 1"""
def mult_inverse(e, tote):
    d = 0
    x1 = 0
    x2 = 0
    y1 = 1
    temp_tote = tote #totient function counts how many ints below n are coprime

    while e > 0:
        temp1 = temp_tote//e #integer division
        temp2 = temp_tote - temp1 * e
        temp_tote = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_tote == 1:
        return d + tote

"""define function to generate both public and private key"""
#accepts 2 random numbers: p and q, which are both prime and secret
def gen_keypair(p, q):
    n = p * q #modulus
    tote = ((p - 1) * (q - 1)) #totient function of n

    e = random.randrange(1, tote)

    g = math.gcd(e, tote) #returns greatest comm. denominator of e and tote

    while g != 1: #while divisor !=1
        e = random.randrange(1, tote) #obtain e such that e and tote are coprime
        g = math.gcd(e, tote)

    d = mult_inverse(e, tote) #d is private key exponent

    return ((e, n), (d,n)) #returns pair of tuples:one for pub key and one for private

#encrypt() takes tuple publicKey and original text to be encrypted
def encrypt(pk, regText):
    key, n = pk #public key contains e and modulus n
    cipher = [(ord(char) ** key) % n for char in regText] #Text is encrypted one char at a time using or()
    return cipher

"""decrypt() takes tuple private key and the encrypted text
does reverse of encrypt() and decrypts text one character at a time"""
def decrypt(pk, ciphertext):
    key, n = pk #private key tuple conatins exponent d and modulus n
    regular = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(regular) #use join() to turn into a string

p = sympy.randprime(200, 400) #generate primes p and q between 200 and 400
q = sympy.randprime(200, 400)

public, private = gen_keypair(p, q) #pass values to key generator
                                    #will generate and return pub and private keys

ogmessage = input("Enter message to be encrypted: ") #ask user to input text

encryptedmessage = encrypt(public, ogmessage)  #will be encrypted with public key, then decrypted with private

print(f"Encrypted message is: {encryptedmessage}") #use f-strings for formatting

print(f"Decrypted message is: {decrypt(private, encryptedmessage)}")


