from typing import Generator, Tuple


def hamming_distance(strand_1: str, strand_2: str) -> int:
    if len(strand_1) != len(strand_2):
        raise ValueError('Input strands should be of equal length.')
    symbol_pairs: Generator[Tuple[str, str], None, None] = (
        (symbol_1, symbol_2)
        for symbol_1, symbol_2 in zip(strand_1, strand_2)
    )
    distance: int = sum(
        symbol_1 != symbol_2
        for symbol_1, symbol_2 in symbol_pairs
    )
    return distance
