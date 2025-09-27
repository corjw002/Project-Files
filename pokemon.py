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
    rand_poke_list = []

    for letter in random_pokemon:
        rand_poke_list.append(letter)

    poke_str = "".join(rand_poke_list)

    answer = [len(rand_poke_list) * "_"]
    answer_str = "".join(answer)

    index = 0

    while index < len(rand_poke_list):

        guess = input("Guess a letter: ")
        guessed_letters.append(guess)

        for letter in rand_poke_list:
            if guess == rand_poke_list[index]:
                answer[index].replace(answer[index], guess)

        print(answer)
        index += 1

    print(rand_poke_list)


def main():
    pokemon_list = read_file("pokemon.txt")
    random_pokemon = choose_word(pokemon_list)
    guessed_letters = []
    display_word(random_pokemon, guessed_letters)


main()
