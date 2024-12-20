from ft_filter import ft_filter
import sys


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        S = sys.argv[1]
        N = sys.argv[2]
        assert N.isdigit(), "the arguments are bad"
        N = int(N)
        assert isinstance(S, str), "the arguments are bad"
        assert all(char.isalpha() or char.isspace() for char in S), "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return

    result = ft_filter(S, N)
    print(result)


if __name__ == "__main__":
    main()
