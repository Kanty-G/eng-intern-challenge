import sys

braille_alphabet= {
    'a':'0.....', 'b':'0.0...', 'c':'00....', 'd':'00.0..','e':'0..0..',
    'f':'000...', 'g':'0000..', 'h':'0.00..', 'i':'.00...', 'j':'.000..',
    'k':'0...0.', 'l':'0.0.0.', 'm':'00..0.', 'n':'00.00.', 'o':'0..00.',
    'p':'000.0.', 'q':'00000.', 'r':'0.000.', 's':'.00.0.', 't':'.0000.',
    'u':'0...00', 'v':'0.0.00', 'w':'.000.0', 'x':'00..00', 'y':'00.000', 'z':'0..000',
    '1':'0.....', '2':'0.0...', '3':'00....', '4':'00.0..', '5':'0..0..',
    '6':'000...', '7':'0000..', '8':'0.00..', '9':'.00...', '0':'.000..',
    'capital':'.....0', 'decimal':'.0...0', 'number':'.0.00.',' ':'......', 
    '.':'..00.0', ',':'..0...', '?':'..0.00', '!':'..00.0', ':':'..00..',
    ';':'..0.0.', '-':'....00', '/':'.0..0.', '<':'.00..0', '>':'0..00.',
    '(':'0.0..0', ')':'.0.00.'}
    
english_alphabet = {i: j for j, i in braille_alphabet.items()}


def englist_to_braille(text):
    braille = []
    for i in text:
        if i.isdigit():
            braille.append(braille_alphabet['number'])
            braille.append(braille_alphabet[i])
        elif i.isalpha():
            if i.isupper():
                braille.append(braille_alphabet['capital'])
                braille.append(braille_alphabet[i.lower()])
            braille.append(braille_alphabet[i.lower()])
        elif i == ' ':
            braille.append(braille_alphabet[i])
        elif i in braille_alphabet:
            braille.append(braille_alphabet[i])
    return ''.join(braille)

def braille_to_english(braille):
    txt = []
    is_number = False
    for i in range(0, len(braille),6):
        char = braille[i:i+6]

        if char == braille_alphabet['capital']:
            i+=6
            nxt_char = braille[i:i+6]
            txt.append(english_alphabet[nxt_char].upper())
        elif char == braille_alphabet['number']:
            is_number = True
        elif is_number and char in english_alphabet:
            txt.append(english_alphabet[char])
        elif char in english_alphabet:
            txt.append(english_alphabet[char])

        if is_number and char= == '......':
            is_number = False
    return ''.join(txt)

            
    
#function to check if the text is in braille
def is_braille(text):
    return all(i in '0.' for i in text) and len(text) % 6 == 0

def main():
    if len(sys.argv) < 2:
        print('Write a text to convert to braille or braille to text')
        sys.exit(1)

    if is_braille(sys.argv[1]):
        print(braille_to_english(sys.argv[1]))
    else:
        print(englist_to_braille(sys.argv[1]))
if __name__ == '__main__':
    main()
