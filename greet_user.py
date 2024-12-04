def greet(name: str) -> None:
    """
    Prints a greeting for the given name.
    :param name: The name of the person to greet.
    """
    print(f"Greetings {name}!")

def main():
 name: str = input("What's your name? ")
 greet(name)
if __name__ == "__main__":
    main()