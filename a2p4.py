"""

Before reading this file or using it please read the readme_a2.pdf included in the zip file. The logic and other things have slightly been changed according to the assignment.
Everything about the resources used to make this file are in the above said file. Do not proceed without reading that.


All the major changes are explained with a comment rest most of the code is same as a2p2.py for the encryption and decryption process except instead shifting only the first character
we shift the first n characters with the corresponding shift in the key where n is the length of the key.

"""


import sys

message = sys.argv[3:]
key = sys.argv[1]
mode = sys.argv[2] 


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = ' '.join(message)
message = message.upper()

key = key.upper()

counter = 0   # Initializing position for the shift according to the key string.
pointer = 0   # Initializing position for the shift according to the characters in the message.

for symbol in message:

    if symbol in LETTERS:

        # Logic used below is that if the position of the symbol in message is less than the length of the key then shift it with the corresponding key position.
        # The logic for encryption and decryption is same except the '+' and '-' difference. 

        if counter<len(key):   

            keyA = LETTERS.find(key[counter])
            keyB = LETTERS.find(message[counter])
            if mode == 'encrypt':
                keyB = keyA + keyB

            elif mode == 'decrypt':
                keyB = keyB - keyA

            if keyB>=len(LETTERS):
                keyB = keyB - len(LETTERS)

            elif keyB<0:
                keyB = keyB + len(LETTERS)

            translated += LETTERS[keyB]
            counter += 1

        # If the position of the symbol in message is greater than the length then shift it according to (symbol-n) position.

        else:
                
            if mode == 'encrypt':
                while LETTERS.find(message[pointer])==-1: #This while loop makes sure if there are any spaces in the message then don't use it to encrypt instead move to the next position.
                    pointer += 1
                keyC = LETTERS.find(message[counter])
                keyD = LETTERS.find(message[pointer])
                keyD = keyC + keyD
            elif mode == 'decrypt':
                while LETTERS.find(translated[pointer])==-1: #This while loop makes sure if there are any spaces in the translated text then don't use it for decryption and skip it.
                    pointer += 1
                keyC = LETTERS.find(symbol)
                keyD = LETTERS.find(translated[pointer])
                keyD = keyC - keyD

            if keyD>=len(LETTERS):
                keyD = keyD - len(LETTERS)
            elif keyD<0:
                keyD = keyD + len(LETTERS)

            translated = translated + LETTERS[keyD]
            pointer += 1
            counter += 1


    else:

        translated = translated + symbol
        counter = counter + 1

print(translated)            

  
    
