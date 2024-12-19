import sys


def main():
    total = 0
    uppercase = 0
    lowercase = 0
    punctuation = 0
    spaces = 0
    digits = 0
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            argument = sys.argv[1]
        elif len(sys.argv) == 1:
            print("What is the text to count ?")
            argument = input() + '\n'
        for char in argument:
            if char.isupper():
                uppercase += 1
            elif char.islower():
                lowercase += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1
            else:
                punctuation += 1
            total += 1
        print(f"The text contains {total} characters:")
        print(f"{uppercase} upper letters")
        print(f"{lowercase} lower letters")
        print(f"{punctuation} punctuation marks")
        print(f"{spaces} spaces")
        print(f"{digits} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        print("Quitting program")


if __name__ == "__main__":
    main()
