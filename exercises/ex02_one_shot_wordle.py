"""One guess wordle game."""

__author__ = "730449161"

secret_word: str = "python"
secret_word_length: int = len(secret_word)

player_guess: str = str(input(f"What is your { secret_word_length }-letter guess? "))

while len(player_guess) != secret_word_length: 
    player_guess = str(input(f"That was not { secret_word_length } letters! Try again: "))
 

word_index_number: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

player_guess_somewhere_else: bool = False

resulting_emojis: str = ""
if len(player_guess) == secret_word_length:
    while word_index_number < secret_word_length:
        index_being_tested: str = player_guess[word_index_number] 
        if index_being_tested == secret_word[word_index_number]:
            resulting_emojis = resulting_emojis + GREEN_BOX
        else:
            player_guess_somewhere_else = False
            alt_word_index_number: int = 0
            while not player_guess_somewhere_else and alt_word_index_number < secret_word_length:
                if index_being_tested == secret_word[alt_word_index_number]:
                    player_guess_somewhere_else = True
                else:
                    alt_word_index_number += 1
            if player_guess_somewhere_else:
                resulting_emojis = resulting_emojis + YELLOW_BOX
        if index_being_tested != secret_word[word_index_number] and not player_guess_somewhere_else:
            resulting_emojis = resulting_emojis + WHITE_BOX
        word_index_number += 1

print(resulting_emojis)

if player_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")  