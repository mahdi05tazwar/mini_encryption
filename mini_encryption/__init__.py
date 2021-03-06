def explain():
    print("This is a simple program that encrypts texts/text files and also decrypts 'em. All you need to do is, call the \"crypt\" function and pass text in the form of a list (each character should be a separate element, in the correct order) into it, then another variable which has the value 0. If you want to encrypt a text file, just use the file management functions of python to store every character into a list, in the correct order. In case you find the instructions confusing, I'll leave examples below.\n")
    print("To import(the main function of) the library:\nfrom mini_encryption import crypt\n\n")
    print("To call the function:\ncount = 0\ncrypt1 = crypt(list, count)\n\n")
    print("List encryption:\nIf you want to encrypt your name (e.g. Mahdi Tazwar; it's my name), then you need to have a list that looks like this: ['M', 'a', 'h', 'd', 'i', ' ', 'T', 'a', 'z', 'w', 'a', 'r']\n\n")
    print("Encrypting a file:\nThe following code shows how to encrypt a file. It's not compulsory that you can use this method only, but I find it pretty easy. \nfilename = input(\"Enter file name\") #Or just directly enter it \ntext = []\nfile = open(filename, 'r')\nwhile True:\nchar = file.read(1)\n    if not char:\n        break\n    text.append(char)\nfile.close()\n\n")
    print("License:\nCopyright 2022 Mahdi Tazwar Raeed\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n")
    print("Conclusion:\nP.S. I have created a program using this package of mine, and it's called 'Minicrypt'. I would be very happy if you check it out. You can download it from my website: mahditaz.pythonanywhere.com")

def crypt(text, count):
    for i in text:
        if i == 'a':
            text[count] = 'Z'
        elif i == 'b':
            text[count] = 'Y'
        elif i == 'c':
            text[count] = 'X'
        elif i == 'd':
            text[count] = 'W'
        elif i == 'e':
            text[count] = 'V'
        elif i == 'f':
            text[count] = 'U'
        elif i == 'g':
            text[count] = 'T'
        elif i == 'h':
            text[count] = 'S'
        elif i == 'i':
            text[count] = 'R'
        elif i == 'j':
            text[count] = 'Q'
        elif i == 'k':
            text[count] = 'P'
        elif i == 'l':
            text[count] = 'O'
        elif i == 'm':
            text[count] = 'N'
        elif i == 'n':
            text[count] = 'M'
        elif i == 'o':
            text[count] = 'L'
        elif i == 'p':
            text[count] = 'K'
        elif i == 'q':
            text[count] = 'J'
        elif i == 'r':
            text[count] = 'I'
        elif i == 's':
            text[count] = 'H'
        elif i == 't':
            text[count] = 'G'
        elif i == 'u':
            text[count] = 'F'
        elif i == 'v':
            text[count] = 'E'
        elif i == 'w':
            text[count] = 'D'
        elif i == 'x':
            text[count] = 'C'
        elif i == 'y':
            text[count] = 'B'
        elif i == 'z':
            text[count] = 'A'
        elif i == 'A':
            text[count] = 'z'
        elif i == 'B':
            text[count] = 'y'
        elif i == 'C':
            text[count] = 'x'
        elif i == 'D':
            text[count] = 'w'
        elif i == 'E':
            text[count] = 'v'
        elif i == 'F':
            text[count] = 'u'
        elif i == 'G':
            text[count] = 't'
        elif i == 'H':
            text[count] = 's'
        elif i == 'I':
            text[count] = 'r'
        elif i == 'J':
            text[count] = 'q'
        elif i == 'K':
            text[count] = 'p'
        elif i == 'L':
            text[count] = 'o'
        elif i == 'M':
            text[count] = 'n'
        elif i == 'N':
            text[count] = 'm'
        elif i == 'O':
            text[count] = 'l'
        elif i == 'P':
            text[count] = 'k'
        elif i == 'Q':
            text[count] = 'j'
        elif i == 'R':
            text[count] = 'i'
        elif i == 'S':
            text[count] = 'h'
        elif i == 'T':
            text[count] = 'g'
        elif i == 'U':
            text[count] = 'f'
        elif i == 'V':
            text[count] = 'e'
        elif i == 'W':
            text[count] = 'd'
        elif i == 'X':
            text[count] = 'c'
        elif i == 'Y':
            text[count] = 'b'
        elif i == 'Z':
            text[count] = 'a'
        elif i == '0':
            text[count] = '6'
        elif i == '1':
            text[count] = '5'
        elif i == '2':
            text[count] = '3'
        elif i == '3':
            text[count] = '2'
        elif i == '4':
            text[count] = '9'
        elif i == '5':
            text[count] = '1'
        elif i == '6':
            text[count] = '0'
        elif i == '7':
            text[count] = '8'
        elif i == '8':
            text[count] = '7'
        elif i == '9':
            text[count] = '4'
        elif i == '!':
            text[count] = '?'
        elif i == '@':
            text[count] = '>'
        elif i == '#':
            text[count] = '<'
        elif i == '$':
            text[count] = '"'
        elif i == '%':
            text[count] = ':'
        elif i == '^':
            text[count] = '|'
        elif i == '&':
            text[count] = '}'
        elif i == '*':
            text[count] = '{'
        elif i == '(':
            text[count] = '+'
        elif i == ')':
            text[count] = '_'
        elif i == '_':
            text[count] = ')'
        elif i == '+':
            text[count] = '('
        elif i == '{':
            text[count] = '*'
        elif i == '}':
            text[count] = '&'
        elif i == '|':
            text[count] = '^'
        elif i == ':':
            text[count] = '%'
        elif i == '"':
            text[count] = '$'
        elif i == '<':
            text[count] = '#'
        elif i == '>':
            text[count] = '@'
        elif i == '?':
            text[count] = '!'
    
        elif i == '-':
            text[count] = '/'
        elif i == '=':
            text[count] = '.'
        elif i == '[':
            text[count] = ','
        elif i == ']':
            text[count] = '\''
        elif i == '\'':
            text[count] = ']'
        elif i == ',':
            text[count] = '['
        elif i == '.':
            text[count] = '='
        elif i == '/':
            text[count] = '-'

        count += 1

    contstr = ""
    for i in text:
        contstr += i
    
    return contstr

explain()