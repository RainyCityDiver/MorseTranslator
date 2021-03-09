README file for RainyCityDiver's Morse Code Translator

DESCRIPTION:
This program is designed to translate letters and/or numbers into morse code, and visa versa. 
Built on Python 3.6.9.

INSTALLATION:
Download the MorseCodeTranslator.py file from the https://github.com/RainyCityDiver/MorseTranslator repository, or copy-paste the code into a Python file of your own. Please see the license file.

TO START:
1) Open file with your choice of Python-3-capable IDE, or run in a terminal capable of running Python 3 files. 
2) Run the program.
3) Program will first ask for one of two options:
  a) Morse-to-Letter translation.
  b) Letter-to-Morse translation.
4) Select which you wish to use by entering the corresponding letter.

FOR MORSE-TO-LETTERS:
Please Note: The input only accepts hyphens ("-") as dashes, and periods (".") as dots at this time. 
Please Note: Spaces are allowed.
Please Note: Numbers are supported.
1) After selecting Morse-to-Letter, type or copy-paste the string of morse code you wish to convert to English when prompted.
2) It is best to separate each letter with a space. Morse letters are between 2 and 4 dots and/or dashes long. 
  a) If you enter '--.-', the program will return 'q'. If you meant to type '--' '.-', for 'm a' the program can't tell which you intended, unless spaces are used properly.
  
FOR LETTERS-TO-MORSE:
Please Note: Spaces are supported.
Please Note: Numbers are supported.
1) After selecting Letter-to-Morse, type your letters/words/numbers/etc. 
  a) Spaces will not be inserted between letters (see ROADMAP).
  b) You may type with spaces between words OR between each letter, depending on your desired output.README file for RainyCityDiver's Morse Code Translator

OUTPUT:
In Letter-to-Morse mode: dots (periods ('.')) and dashes (hyphens ('-')) in corresponding Morse Code for each input letter displayed on the terminal/IDE output window. 
In Morse-to-Letter mode: letter/character/number corresponding to each seperated (by space) input Morse Code letter displayed on the terminal/IDE output window. 

RE-RUN:
You will be asked if you would like to translate again; simply enter "y" for yes, or "n" for no. 
NOTE: You will need to select Morse-to-Letter translation or Letter-to-Morse translation again. This prevents the user from needing to re-run the entire program to switch between the two modes. This is a feature, not a bug (no, seriously).
  
SUPPORT:
You may reach out to the creator via GitHub with suggestions to improve program (see ROADMAP).

ROADMAP/FUTURE FUNCTIONALITY:
1) Multiple-run functionality is being explored for future implementation. -DONE
2) In Letter-to-Morse mode: Spaces inserted between Morse letters.
3) In Letter-to-Morse mode: Character indicating seperation between words for easier reading.
4) In Morse-to-Letter mode: spaces between letter groups.
5) Support for Arabic numerals. -DONE

CONTRIBUTIONS:
Code contributions are welcome, preferably as messages to the creator containing suggestions to enhance functionality/fix bugs, with template code attached so the creator can problem-solve or implement new code on their own. The creator is currently building experience with Python 3, and with coding in general. Allowing the creator to learn and develope their skills is of more value to them than providing functional code and saying "put this in line X". Thank you for your understanding.

PROJECT STATUS
The Morse Code Translator is under developement. 

CHANGELOG:
2021.03.02: added support for repeated translations without needing to re-run program, and support for arabic numbers. 



This document is not final and is subject to modification. 
