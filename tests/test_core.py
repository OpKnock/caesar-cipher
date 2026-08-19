"""Tests for Caesar cipher core functionality."""

import pytest
from caesar_cipher.core import (
    caesar_shift,
    frequency_analysis,
    chi_squared_score,
    crack_caesar,
    format_crack_results,
    ENGLISH_FREQ,
)


def test_caesar_shift_encrypt():
    assert caesar_shift("HELLO", 3, encrypt=True) == "KHOOR"
    assert caesar_shift("hello", 1, encrypt=True) == "ifmmp"
    assert caesar_shift("XYZ", 2, encrypt=True) == "ZAB"


def test_caesar_shift_decrypt():
    assert caesar_shift("KHOOR", 3, encrypt=False) == "HELLO"
    assert caesar_shift("ifmmp", 1, encrypt=False) == "hello"
    assert caesar_shift("ZAB", 2, encrypt=False) == "XYZ"


def test_caesar_shift_roundtrip():
    original = "Hello, World! 123"
    encrypted = caesar_shift(original, 5, encrypt=True)
    decrypted = caesar_shift(encrypted, 5, encrypt=False)
    assert decrypted == original


def test_caesar_shift_non_alpha():
    assert caesar_shift("Hello 123!", 3, encrypt=True) == "Khoor 123!"
    assert caesar_shift("Test@#$%", 10, encrypt=True) == "Docd@#$%"


def test_frequency_analysis():
    freq = frequency_analysis("aaaabbc")
    assert freq['a'] == 4/7 * 100
    assert freq['b'] == 2/7 * 100
    assert freq['c'] == 1/7 * 100


def test_frequency_analysis_empty():
    assert frequency_analysis("") == {}
    assert frequency_analysis("123!@#") == {}


def test_chi_squared_perfect_match():
    # Perfect match requires all 26 letters to match exactly
    score = chi_squared_score(ENGLISH_FREQ)
    assert score == 0.0


def test_chi_squared_worse_match():
    score1 = chi_squared_score({'e': 12.70})
    score2 = chi_squared_score({'z': 12.70})
    assert score2 > score1


def test_crack_caesar():
    ciphertext = caesar_shift("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 5, encrypt=True)
    results = crack_caesar(ciphertext)
    
    assert len(results) == 26
    assert results[0].shift == 5
    assert "QUICK" in results[0].plaintext.upper()


def test_crack_result_ordering():
    ciphertext = caesar_shift("ETAOIN SHRDLU", 3, encrypt=True)
    results = crack_caesar(ciphertext)
    
    for i in range(len(results) - 1):
        assert results[i].score <= results[i + 1].score


def test_format_crack_results():
    ciphertext = caesar_shift("TEST", 2, encrypt=True)
    results = crack_caesar(ciphertext)
    output = format_crack_results(results, top_n=3)
    
    assert "Shift" in output
    assert "Score" in output
    assert "Preview" in output