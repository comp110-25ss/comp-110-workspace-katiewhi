"""My challenge questions in COMP110!"""

__author__ = "730546969"


def mimic(message: str) -> str:
    """Return the exact same message that was provided as input."""
    return message


def main() -> None:
    """Prompt the user for input and print the result of the mimic function."""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()
