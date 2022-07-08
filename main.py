from time import sleep

# Morse to English / English to Morse Dictionaries

ENGLISH_TO_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "": "Please enter something here",
    " ": " "}

MORSE_TO_ENGLISH = {}
for key, value in ENGLISH_TO_MORSE.items():
    MORSE_TO_ENGLISH[value] = key


# clears the screen
def clear_screen():
    print("\n" * 70)


# main called function
def main_func():
    # asks the user is he wants to do another translation
    def again():
        clear_screen()
        user_input = input("Do you want to commit another translation? Type 'y' for yes and 'n' for no:\n").lower()
        if user_input == "y":
            main_func()
        elif user_input == "n":
            raise SystemExit(0)
        else:
            print("The input you entered was not valid.")
            sleep(5)
            clear_screen()
            again()

    # asks the user what way he wants to translate
    def ask_mode():
        clear_screen()
        print("Welcome to Adrian's Morse Code Translator\n\nPlease choose the mode you want to use")
        user_mode = input(
            "Type 'm' to enter morse code and receive "
            "english and type 'e' to enter english and receive"
            " morse code or type 'exit' to stop the program:\n").lower()

        if user_mode == "m":
            return "m"
        elif user_mode == "e":
            return "e"
        elif user_mode == "exit":
            return "exit"
        else:
            print("THE MODE YOU ENTERED DOES NOT EXIST. TRY AGAIN")
            sleep(5)
            clear_screen()
            ask_mode()

    # asks the user to type in morse text
    def ask_morse():

        # checks if there was an error --> if not then prints the morse code
        def morse_if(morse_prop):
            if morse_prop == "error":
                ask_morse()
            else:
                morse_real_text = "".join(morse_prop)
                print(f"MORSE: {morse_real_text}")

        # formats the morse code
        def format_morse(morse_text):
            return morse_text.split("   ")

        clear_screen()

        # converts text from morse to english (try's to append it to a list but also checks for errors)
        def morse_to_eng(morse_list):
            eng = []
            for i in morse_list:
                try:
                    eng.append(MORSE_TO_ENGLISH[i])

                except KeyError:

                    try:
                        print(f"THE KEY {i} AT POSITION {eng.index(i)} IS NOT PROPER MORSE.")
                        sleep(5)
                        return "error"

                    except ValueError:
                        print("AN ERROR HAS OCCURED. PLEASE CHECK YOUR SPACES AS WELL AS YOUR MORSE")
                        sleep(5)
                        return "error"

            return eng

        print("""MORSE TO ENGLISH\n\nRULES FOR TYPING MORSE IN THIS TRANSLATOR:\n1. THE SPACE BETWEEN 
        TWO LETTERS IS 3 SPACES\n2. THE SPACE BETWEEN TWO WORDS IS 7 SPACES\n3. ENTER REAL MORSE OR THE TRANSLATOR
        WILL RETURN AN ERROR.\n\n\n""")
        morse_user = input("Enter your morse here: ")
        morse_format = format_morse(morse_user)
        morse_trans = morse_to_eng(morse_format)
        morse_if(morse_trans)

    # asks the user to type in english text
    def ask_eng():

        def eng_if(eng_prop):
            if eng_prop == "error":
                ask_eng()
            else:
                eng_real_text = "   ".join(eng_prop)
                print(f"ENGLISH: {eng_real_text}")

        # formats the english text
        def format_eng(eng_text):
            return list(eng_text)

        clear_screen()

        # translates english to morse
        def eng_to_morse(eng_list):
            morse = []
            for i in eng_list:
                try:
                    morse.append(ENGLISH_TO_MORSE[i])

                except KeyError:

                    try:
                        print(f"THE KEY {i} AT POSITION {morse.index(i)} DOES NOT EXIST IN ENGLISH.")
                        sleep(5)
                        return "error"

                    except ValueError:
                        print("AN ERROR HAS OCCURED. PLEASE CHECK YOUR SPACES AS WELL AS YOUR ENGLISH LETTERS")
                        sleep(5)
                        return "error"

            return morse

        print("""ENGLISH TO MORSE\n\nRULES FOR TYPING ENGLISH IN THIS TRANSLATOR:\n1. THE SPACE BETWEEN 
        TWO LETTERS IS 0 SPACES\n2. THE SPACE BETWEEN TWO WORDS IS 1 SPACES\n3. ENTER REAL ENGLISH LETTERS OR THE 
        TRANSLATOR WILL RETURN AN ERROR.\n\n\n""")
        eng_user = input("Enter your English here: ").lower()
        eng_format = format_eng(eng_user)
        eng_trans = eng_to_morse(eng_format)
        eng_if(eng_trans)

    # checks the mode returned from the ask_mode() func
    mode = ask_mode()
    if mode == "m":
        ask_morse()
    elif mode == "e":
        ask_eng()
    elif mode == "exit":
        raise SystemExit(0)

    again()


main_func()
