# John Clancy
# UWYO COSC 1010
# Submission Date: 11/21/2024
# Lab 10
# Lab Section: 13 
# Sources, people worked with, help given to: 
# Chat GPT assisted with the "found" flag logic for debugging
# lecture notes of files and exceptions


#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

def readPasswords(file):
    
    try:
        file = Path("rockyou.txt")
        contents = file.read_text(encoding='utf-8')
        return contents
    
    except FileNotFoundError:
   
        print("Error: The file 'rockyou.txt' was not found.")
        return None
    
def readHash(file):
    
    try:
        file = Path("hash.txt")
        contents = file.read_text()
        return contents

    except FileNotFoundError:
        print("Error: The file 'hash.txt' was not found.")
        return None


def sortData(passwords):
    lines = passwords.splitlines()
    output = [] 

    for line in lines:
        password = line
        output.append(password)

    return output


def main():
    passwords = Path("rockyou.txt")
    hashcode = Path("hash.txt")
    
    password_contents = readPasswords(passwords)
    hashcode_contents = readHash(hashcode)
    password_list = sortData(password_contents)


    found = False
    
    for entry in password_list:
        hash_value = get_hash(entry)
        if hash_value == hashcode_contents:
            print(f"{entry} was found in cracked passwords!")
            found = True
            break
    if not found:
        print("No passwords found!")

        
    

        



main()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.