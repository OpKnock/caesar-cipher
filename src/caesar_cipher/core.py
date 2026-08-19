"""Caesar cipher core implementation with frequency analysis."""

import string
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple

ENGLISH_FREQ = {
    'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75,
    's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78,
    'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23, 'g': 2.02, 'y': 1.97,
    'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
    'q': 0.10, 'z': 0.07
}

ALPHABET = string.ascii_lowercase


def caesar_shift(text: str, key: int, encrypt: bool = True) -> str:
    """Apply Caesar cipher shift to text."""
    shift = key if encrypt else -key
    result = []
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(char)
    
    return ''.join(result)


def frequency_analysis(text: str) -> dict:
    """Calculate letter frequency percentages in text."""
    letters = [c.lower() for c in text if c.isalpha()]
    if not letters:
        return {}
    
    total = len(letters)
    counts = Counter(letters)
    return {char: (count / total) * 100 for char, count in counts.items()}


def chi_squared_score(observed: dict) -> float:
    """Calculate chi-squared statistic against English frequency."""
    score = 0.0
    for char, expected_pct in ENGLISH_FREQ.items():
        observed_pct = observed.get(char, 0.0)
        if expected_pct > 0:
            score += ((observed_pct - expected_pct) ** 2) / expected_pct
    return score


@dataclass
class CrackResult:
    """Result of a brute-force crack attempt."""
    shift: int
    plaintext: str
    score: float
    frequency: dict


def crack_caesar(ciphertext: str) -> List[CrackResult]:
    """Brute-force all 26 shifts with frequency analysis ranking."""
    results = []
    
    for shift in range(26):
        plaintext = caesar_shift(ciphertext, shift, encrypt=False)
        freq = frequency_analysis(plaintext)
        score = chi_squared_score(freq)
        results.append(CrackResult(
            shift=shift,
            plaintext=plaintext,
            score=score,
            frequency=freq
        ))
    
    results.sort(key=lambda r: r.score)
    return results


def format_crack_results(results: List[CrackResult], top_n: int = 5) -> str:
    """Format crack results for display."""
    lines = []
    lines.append(f"{'Shift':<6} {'Score':<10} {'Preview'}")
    lines.append("-" * 60)
    
    for i, result in enumerate(results[:top_n]):
        preview = result.plaintext[:50].replace('\n', ' ')
        if len(result.plaintext) > 50:
            preview += "..."
        marker = " -> BEST" if i == 0 else ""
        lines.append(f"{result.shift:<6} {result.score:<10.2f} {preview}{marker}")
    
    return "\n".join(lines)