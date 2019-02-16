"""

Before reading this file or using it please read the readme_a2.pdf included in the zip file. The logic and other things have slightly been changed according to the assignment.
Everything about the resources used to make this file are in the above said file. Do not proceed without reading that.

"""

# All the major changes are explained with a comment rest most of the code is same as a2p1.py

import sys

message = sys.argv[3:]
key = int(sys.argv[1])
mode = sys.argv[2] 


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''


message = ' '.join(message)
message = message.upper()


counter = 0 # Initializing the position for the shift of the first character in the text according to the key. 
for symbol in message:
    if symbol in LETTERS:

        # The assignment difference to shift the first character by the key

        if counter == 0:  
            num = LETTERS.find(symbol)

            if mode == 'encrypt':  # For encryption
                num = num + key

            elif mode == 'decrypt': # For decryption
                num = num-key

            if num>=len(LETTERS):
                num = num - len(LETTERS)
            elif num<0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
            counter = counter + 1
    
       # After the first character shift according to the previous message position.

        else:
        
            if mode == 'encrypt':
                num = LETTERS.find(message[counter-1])  # For encryption we use the previous original message position
                key1 = LETTERS.find(symbol)
                num = num + key1

            if mode == 'decrypt':
                num = LETTERS.find(symbol)
                key1 = LETTERS.find(translated[counter-1])  # For decryption we use the previous position of the cipher text as that was the key shift in the encryption
                num = num - key1

            if num>=len(LETTERS):
                num = num -len(LETTERS)

            elif num<0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]
            counter = counter + 1
    else:
        translated = translated + symbol

print(translated)    
    
