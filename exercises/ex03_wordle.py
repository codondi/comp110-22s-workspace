"""Structured and more realistic wordle."""

__author__ = "730449161"


def contains_char(word_being_searched: str, character_being_searched: str) -> bool:
    """When given a two strings, the first of any length, the second a single character, will return True if the single character of the second string is found in the first string."""
    assert len(character_being_searched) == 1
    i = 0
    while i < len(word_being_searched):
        if word_being_searched[i] == character_being_searched:
            return True
        i += 1
    
    return False


def emojified(player_guess: str, secret_word: str) -> str:
    """Given two strings of equal length, will return a string of emojis who's colr codifies the same."""
    assert len(player_guess) == len(secret_word)

    i = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    resulting_emojis: str = ""
    
    while i < len(player_guess):
        if player_guess[i] == secret_word[i]:
            resulting_emojis += GREEN_BOX
        else:
            if contains_char(secret_word, player_guess[i]):
                resulting_emojis += YELLOW_BOX
            else:
                resulting_emojis += WHITE_BOX
        i += 1
    
    return resulting_emojis


def input_guess(expected_length: int) -> str:
    """Will prompt the user for a guess until one is made of the proper length. Returns the guess."""
    characters_match: bool = False
    
    player_guess: str = str(input(f"Enter a { expected_length } character word: "))
    
    if len(player_guess) == expected_length:
        characters_match = True

    while not characters_match:
        player_guess = str(input(f"That wasn't { expected_length } chars! Try again: "))
        if len(player_guess) == expected_length:
            characters_match = True
    
    return player_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    used_turns: int = 1
    user_won: bool = False

    while used_turns <= 6 and not user_won:
        print(f"=== Turn {used_turns}/6 ===")
        player_guess: str = input_guess(len(secret_word))
        print(emojified(player_guess, secret_word))
        if player_guess == secret_word:
            user_won = True
        
        used_turns += 1

    used_turns -= 1
    if user_won:
        print(f"You won in { used_turns }/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()