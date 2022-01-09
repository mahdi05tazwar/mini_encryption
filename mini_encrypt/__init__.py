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