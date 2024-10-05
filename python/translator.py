import sys

braille_alphabet= {
    'a':'O.....', 'b':'O.O...', 'c':'OO....', 'd':'OO.O..', 'e':'O..O..',
    'f':'OOO...', 'g':'OOOO..', 'h':'O.OO..', 'i':'.OO...', 'j':'.OOO..',
    'k':'O...O.', 'l':'O.O.O.', 'm':'OO..O.', 'n':'OO.OO.', 'o':'O..OO.',
    'p':'OOO.O.', 'q':'OOOOO.', 'r':'O.OOO.', 's':'.OO.O.', 't':'.OOOO.',
    'u':'O...OO', 'v':'O.O.OO', 'w':'.OOO.O', 'x':'OO..OO', 'y':'OO.OOO',
    'z':'O..OOO'}

braille_numbers_and_symbols = {
    '1':'O.....', '2':'O.O...', '3':'OO....', '4':'OO.O..', '5':'O..O..',
    '6':'OOO...', '7':'OOOO..', '8':'O.OO..', '9':'.OO...', 'O':'.OOO..',
    'capital':'.....O', 'decimal':'.O...O', 'number':'.O.OOO',' ':'......', 
    '.':'..OO.O', ',':'..O...', '?':'..O.OO', '!':'..OO.O', ':':'..OO..',
    ';':'..O.O.', '-':'....OO', '/':'.O..O.', '<':'.OO..O', '>':'O..OO.',
    '(':'O.O..O', ')':'.O.OO.'}
    
english_alphabet = {i: j for j, i in braille_alphabet.items()}
symbols_and_numbers = {i: j for j, i in braille_numbers_and_symbols.items()}


def english_to_braille(text):
    braille = []
    prev_char = None # previous character to track the previous character of a number
    for i in text:
        if i.isdigit():
            if prev_char == ' ' or prev_char == None:
                braille.append(braille_numbers_and_symbols['number'])
            braille.append(braille_numbers_and_symbols[i])
        elif i.isalpha():
            if i.isupper():
                braille.append(braille_numbers_and_symbols['capital'])
            braille.append(braille_alphabet[i.lower()])
        elif i == ' ':
            braille.append(braille_numbers_and_symbols[' '])

        elif i in braille_numbers_and_symbols:
            braille.append(braille_numbers_and_symbols[i])
        else:

            braille.append(braille_alphabet[i])
        prev_char = i

    return ''.join(braille)

def braille_to_english(braille):
    txt = []
    is_number = False
    i = 0
    while i < len(braille):
        char =  braille[i:i+6]

        #check if the character is a capital letter
        if char ==braille_numbers_and_symbols['capital']:
            i += 6
            nxt_char = braille[i:i+6]
            txt.append(english_alphabet.get(nxt_char,'#').upper())

        elif char == braille_numbers_and_symbols['number']:
            is_number = True

        elif is_number and char in symbols_and_numbers:
            txt.append(symbols_and_numbers[char])
            if char == braille_numbers_and_symbols[' ']:
                is_number = False

        elif char in english_alphabet:
            txt.append(english_alphabet[char])

        elif char in symbols_and_numbers:
            txt.append(symbols_and_numbers[char])
        else:
            txt.append('#')

        i += 6
    return ''.join(txt)

            
   
#function to check if the text is in braille
def is_braille(text):
    if len(text) % 6 != 0:
        return False
    
    for i in range(0, len(text), 6):
        char = text[i:i+6]
        if char not in english_alphabet and char not in symbols_and_numbers:
            return False
    return True

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    #join all the arguments into a single string
    string = ' '.join(sys.argv[1:])
    if is_braille(string):

        print(braille_to_english(string))

    else:

        print(english_to_braille(string))
if __name__ == '__main__':
    main()
