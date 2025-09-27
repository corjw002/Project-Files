import random


def read_file(filename):
    infile = open("pokemon.txt", "r")

    pokemon_string = infile.read()
    character_list = pokemon_string.split(", ")
    infile.close()
    return character_list


def choose_word(my_list):
    pokemon_list = read_file("pokemon.txt")

    random_pokemon = random.choice(pokemon_list)
    return random_pokemon



def display_word(random_pokemon, guessed_letters):
    turn = 0
    random_pokemon = random_pokemon.lower()
    rand_poke_list = list(random_pokemon)
    display_answer = []
    current_state = (len(random_pokemon) * "_")
    guesses = 0
    print("\nWelcome to GUESS THE POKEMON!")



    while current_state != random_pokemon:
        print()
        print()
        print("*" * 30)
        print(f"Turn: {guesses}")


        print(current_state)
        print(f"Letters guessed: {guessed_letters}")
        print()

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)
        guessed_letters.sort()
        index = 0

        current_state_list = list(current_state)

        while index < len(random_pokemon):

            if guess == random_pokemon[index]:
                    current_state_list[index] = guess



            index += 1
        current_state = "".join(current_state_list)
        guesses += 1


    print("Well done, you guessed the Pokemon!")
    print(f"It took you {guesses} guesses!")









def play_game():
    pokemon_list = read_file("pokemon.txt")
    random_pokemon = choose_word(pokemon_list)

    guessed_letters = []
    current_state = display_word(random_pokemon, guessed_letters)







play_game()
