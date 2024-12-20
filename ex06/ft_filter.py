
def ft_filter(S: str, N: int) -> str:
    """"
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items
    of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    return [word for word in S.split() if len(word) > N]
