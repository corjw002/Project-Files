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
    print(current_state)
    print(random_pokemon)


    while current_state != random_pokemon:
        guess = input("Guess a letter: ")
        guessed_letters.append(guess)
        index = 0

        current_state_list = list(current_state)

        while index < len(random_pokemon):

            if guess == random_pokemon[index]:
                current_state_list[index] = guess

            index += 1
        current_state = "".join(current_state_list)
        print(current_state)

    print("Well done, you guessed the Pokemon!")



    """
            display_answer_str = "".join(display_answer)

        if current_state != display_answer_str:
            current_state = display_answer_str
    """







def main():
    pokemon_list = read_file("pokemon.txt")
    random_pokemon = choose_word(pokemon_list)

    guessed_letters = []
    display_word(random_pokemon, guessed_letters)





main()
