""""Examples of importing in Python."""


# helpers represents the global frame
from lessons import helpers

# Allows us to alias/shorthand helper as hp. Ex. hp.powerful
from lessons import helpers as hp

# Import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))


# Idiom for making a module able to run as a program
# or have its global definitions imported elsewhere.
if __name__ == "__main__":
    main()
else:
    # it is notidiomatic to have an else branch
    print(f"helper.py was imported: {__name__}")