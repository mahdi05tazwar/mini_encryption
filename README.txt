This is a simple program that encrypts texts/text files and also decrypts 'em. All you need to do is, call the "crypt" function and pass text in the form of a list (each character should be a separate element, in the correct order) into it. If you want to encrypt a text file, just use the file management functions of python to store every character into a list, in the correct order. In case you find the instructions confusing, I'll leave examples below.

List: If you want to encrypt your name (e.g. Mahdi Tazwar; it's my name), then you need to have a list that looks like this: ['M', 'a', 'h', 'd', 'i', ' ', 'T', 'a', 'z', 'w', 'a', 'r']

File: The following code shows how to encrypt a file. It's not compulsory that you can use this method only, but I find it pretty easy.

filename = input("Enter file name") #Or just directly enter it 
text = []
file = open(filename, 'r')
while True:
char = file.read(1)
    if not char:
        break
    text.append(char)
file.close()

P.S. I have created a program using this package of mine, and it's called 'Minicrypt'. I would be very happy if you check it out. You can download it from my website: 
mahditaz.pythonanywhere.com

Thank you!
Mahdi Tazwar Raeed
