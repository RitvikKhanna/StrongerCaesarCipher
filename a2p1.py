"""

Before reading this file or using it please read the readme_a2.pdf included in the zip file. The logic and other things have slightly been changed according to the assignment.
Everything about the resources used to make this file are in the above said file. Do not proceed without reading that.

"""

# Nothing new in this program as compared to the original Caesar Cipher except the input from command line.


import sys  # For command line input

message = sys.argv[3:]
key = int(sys.argv[1])
mode = sys.argv[2] 


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = ' '.join(message)
message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        
        translated = translated + LETTERS[num]

    else:
        
        translated = translated + symbol


print(translated)


