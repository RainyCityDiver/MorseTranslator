e_to_m = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
    'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-..-', 'z':'--..', ' ':' ', '1':'.----',
    '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...',
    '8':'---..', '9':'----.', '0':'-----'
    }

m_to_e = {
    '.-':'a', '-...':'b', '-.-.':'c', '-..':'d',
    '.':'e', '..-.':'f', '--.':'g', '....':'h',
    '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
    '--':'m', '-.':'n', '---':'o', '.--.':'p',
    '--.-':'q', '.-.':'r', '...':'s', '-':'t',
    '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
    '-..-':'y', '--..':'z', ' ':' ', '.----':'1',
    '..---':'2', '...--':'3', '....-':'4',
    '.....':'5', '-....':'6', '--...':'7',
    '---..':'8', '----.':'9', '-----':'0'
    }

restart = "y"

def from_letters(code_input):
    output = ""
    code = code_input.lower()
    for letter in code:
        output += e_to_m.get(letter, '?')
    print("Here it is in Morse Code:", output)
    

def from_morse(code_input):
    output = ""
    code = code_input.split(' ') 
    for letter in code:
        output += m_to_e.get(letter, '?')
    print("Here it is in characters:", output)
       

while restart != "n":
    print("""Please select the following:
M for Morse-to-Letters, or """)
    morse_original = input("L for Letters-to-Morse: ")
    morse = morse_original.lower()

    if morse == 'l':
        code_input = input("""Please write/paste characters here:
: """)
        from_letters(code_input)
        restart_input = input("Another? (y/n) ")
        restart = restart_input.lower()

    elif morse == 'm':
        code_input = input("""Please write/paste string here:
(periods for dots and hyphens for dashes and spaces
between letters): """)
        from_morse(code_input)
        restart_input = input("Another? (y/n) ")
        restart = restart_input.lower()

    else:
        restart_input = input("Another try? (y/n) ")
        restart = restart_input.lower()

