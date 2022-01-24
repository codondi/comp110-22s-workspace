"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730449161"

character_word: str = str(input("Enter a 5-character word: "))
if len(character_word) != 5: 
    print("Error: Word must contain 5 characters")
    quit()

single_character: str = str(input("Enter a single character: "))
if len(single_character) != 1:
    print("Error: Character must be a single character")
    quit()

print("Searching for " + single_character + " in " + character_word)

number_of_indices: int = 0

if character_word[0] == single_character: 
    print(single_character + " found at index 0")
    number_of_indices = number_of_indices + 1

if character_word[1] == single_character: 
    print(single_character + " found at index 1")
    number_of_indices = number_of_indices + 1

if character_word[2] == single_character: 
    print(single_character + " found at index 2")
    number_of_indices = number_of_indices + 1

if character_word[3] == single_character: 
    print(single_character + " found at index 3")
    number_of_indices = number_of_indices + 1

if character_word[4] == single_character: 
    print(single_character + " found at index 4")
    number_of_indices = number_of_indices + 1

if number_of_indices > 1:    
    print(str(number_of_indices) + " instances of " + single_character + " found in " + character_word)
else:
    if number_of_indices == 0:
        print("No instances of " + single_character + " found in " + character_word)
    else:
        if number_of_indices == 1:
            print(str(number_of_indices) + " instance of " + single_character + " found in " + character_word)
                
