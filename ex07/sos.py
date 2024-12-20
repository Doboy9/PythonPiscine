import sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-", "@": ".--.-."
}


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        input = sys.argv[1]
        assert all(
            char.isalnum() or char == " " for char in input
            ), "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    morse_code = " ".join(
        NESTED_MORSE[char.upper()]
        for char in input
        if char.upper() in NESTED_MORSE
    )
    print(morse_code)


if __name__ == "__main__":
    main()
