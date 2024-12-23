import sys
import time


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progress bar every time a value is requested.
    """
    total = len(lst)
    length = 50
    filler = '█'

    for i, item in enumerate(lst, start=1):
        percent = (100 * i / total)
        filled_length = int(length * i // total)
        bar = filler * filled_length + ' ' * (length - filled_length)
        sys.stdout.write(f'\r{percent:.0f}%|{bar}| {i}/{total}')
        sys.stdout.flush()
        yield item
    print()


if __name__ == "__main__":
    for item in ft_tqdm(range(333)):
        time.sleep(0.05)
