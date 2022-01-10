# MINI ENCRYPTION


**Version 0.0.1**


 This is a simple program that encrypts texts/text files and also decrypts 'em. All you need to do is, call the "crypt" function and pass text in the form of a list (each character should be a separate element, in the correct order) into it, then another variable which has the value 0. If you want to encrypt a text file, just use the file management functions of python to store every character into a list, in the correct order. In case you find the instructions confusing, I'll leave examples below.

# TO IMPORT:
from mini_encryption import crypt

# Calling function: 
count = 0
crypt1 = crypt(list, count)

# List: 

If you want to encrypt your name (e.g. Mahdi Tazwar; it's my name), then you need to have a list that looks like this: ['M', 'a', 'h', 'd', 'i', ' ', 'T', 'a', 'z', 'w', 'a', 'r']

# File: 

The following code shows how to encrypt a file. It's not compulsory that you can use this method only, but I find it pretty easy.

filename = input("Enter file name") #Or just directly enter it 
text = []
file = open(filename, 'r')
while True:
char = file.read(1)
    if not char:
        break
    text.append(char)
file.close()


# LICENSE

Copyright 2022 Mahdi Tazwar Raeed

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# CONCLUSION

P.S. I have created a program using this package of mine, and it's called 'Minicrypt'. I would be very happy if you check it out. You can download it from my website: 
mahditaz.pythonanywhere.com

Thank you!
Mahdi Tazwar Raeed

