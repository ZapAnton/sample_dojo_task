import pytest
from task import hamming_distance


def test_hamming_distance_returns_0_if_two_empty_strings_are_passed():
    strand_1 = ''
    strand_2 = ''
    distance: int = hamming_distance(strand_1, strand_2)
    assert distance == 0


def test_hamming_distance_returns_0_if_two_identical_strings_are_passed():
    strand_1 = 'AGG'
    strand_2 = 'AGG'
    distance: int = hamming_distance(strand_1, strand_2)
    assert distance == 0


def test_hamming_distance_returns_1_if_two_strings_with_1_difference_are_passed():
    strand_1 = 'AGT'
    strand_2 = 'AGG'
    distance: int = hamming_distance(strand_1, strand_2)
    assert distance == 1


def test_hamming_distance_returns_3_if_two_strings_with_3_differences_are_passed():
    strand_1 = 'AGT'
    strand_2 = 'TTG'
    distance: int = hamming_distance(strand_1, strand_2)
    assert distance == 3


def test_hamming_distance_raises_value_error_if_one_string_is_empty_and_other_is_not():
    strand_1 = ''
    strand_2 = 'TTG'
    with pytest.raises(ValueError):
        hamming_distance(strand_1, strand_2)


def test_hamming_distance_raises_value_error_if_one_string_is_longer_than_the_other():
    strand_1 = 'TTGAA'
    strand_2 = 'TTG'
    with pytest.raises(ValueError):
        hamming_distance(strand_1, strand_2)
