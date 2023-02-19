import random , en

languages = ["en", "de", "es", "pycc"]

def game_lang():
    while True:
        inp = input(f"\nPlease enter your desired Language!\nThe Languages available are {languages}: ")

        if inp.isdigit():
            print("\nInvalid Input! Number and Symbols not allowed!\n")

        else:
            if inp in languages:
                game_language = inp
                break

            else:
                print(f"Language not found!\n")
                continue

    return game_language


