e_to_m = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
    'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..',
    'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-..-', 'z':'--..', ' ':' '
    }

m_to_e = {
    '.-':'a', '-...':'b', '-.-.':'c', '-..':'d',
    '.':'e', '..-.':'f', '--.':'g', '....':'h',
    '..':'i', '.---':'j', '-.-':'k', '.-..':'l',
    '--':'m', '-.':'n', '---':'o', '.--.':'p',
    '--.-':'q', '.-.':'r', '...':'s', '-':'t',
    '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
    '-..-':'y', '--..':'z', ' ':' '
    }

print("""Please select the following:
M for Morse-to-English, or """)
morse_original = input("E for English-to-Morse: ")
morse = morse_original.lower()

output = ""

if morse == 'e':
    code_input = input("""Please write/paste sentence here:
: """)
    code = code_input.lower()
    for letter in code:
        output += e_to_m.get(letter, '?')

if morse == 'm':
    code_input = input("""Please write/paste string here:
(periods for dots and hyphens for dashes and spaces
between letters): """)
    code = code_input.split(' ') 
    for letter in code:
        output += m_to_e.get(letter, '?')

print(output)
