# Caesar Cipher

Educational Caesar cipher tool for text encryption and decryption.

## Overview

The Caesar Cipher tool is an educational cryptography utility designed to demonstrate classical substitution cipher techniques. This tool helps students and enthusiasts understand the fundamentals of symmetric encryption, cipher patterns, and basic cryptanalysis in a controlled, educational environment.

**Important:** This tool is intended solely for educational and educational purposes only. Caesar cipher encryption is extremely weak and should never be used for protecting real data. This tool is for learning about historical cipher techniques and basic cryptography concepts only.

## Features

### Encryption and Decryption

- **Caesar cipher encryption**: Shift each letter by a specified number of positions (1-25)
- **Caesar cipher decryption**: Reverse the shift to recover original plaintext
- **Case preservation**: Maintain uppercase/lowercase distinctions during transformation
- **Non-alphabetic character handling**: Leave numbers, symbols, and spaces unchanged

### Brute-Force Cracking

- **All 26 shifts**: Test every possible shift key (0-25, where 0 = no change)
- **Frequency analysis ranking**: Score each decryption attempt by English letter frequency
- **Likely plaintext identification**: The highest-scoring result is most likely the correct plaintext
- **Rich terminal output**: Colored tables displaying each shift and its frequency score

### Educational Focus

- **Historical context**: Understanding of Julius Caesar's original cipher technique
- **Cryptanalysis basics**: Introduction to frequency analysis methods
- **Pattern recognition**: How language patterns can help break simple ciphers
- **Symmetric encryption fundamentals**: Core concepts shared with modern encryption

## Installation

### Requirements

- **Python 3.9+**: caesar-salad-cipher package
- **Optional**: `just` command runner (for command execution)

### UV Tool Installation

```bash
uv tool install caesar-salad-cipher
```

### Just Command Runner

```bash
# Using curl (recommended)
curl -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin

# Or via package manager
# Debian/Ubuntu: apt install just
# Fedora: dnf install just
# macOS: brew install just
```

### Verify Installation

```bash
caesar-cipher --help
just --list
```

## Quick Start

```bash
uv tool install caesar-salad-cipher
caesar-cipher encrypt "HELLO WORLD" --key 3
```

### Using just as Command Runner

Type `just` to see all available commands:

| Command | Description |
|---------|-------------|
| `caesar-cipher encrypt --text "HELLO" --key 3` | Encrypt text |
| `caesar-cipher decrypt --cipher "KHOOR" --key 3` | Decrypt text |
| `caesar-cipher crack --cipher "KHOOR"` | Brute-force with frequency analysis |

## Learn

This project includes step-by-step learning materials covering security theory, architecture, and implementation.

| Module | Topic |
|--------|-------|
| **00 - Overview** | Prerequisites and quick start |
| **01 - Concepts** | Security theory and real-world breaches (historical ciphers) |
| **02 - Architecture** | System design and data flow (encryption/decryption pipeline) |
| **03 - Implementation** | Code walkthrough with file references (substitution cipher logic) |
| **04 - Challenges** | Extension ideas and exercises (Vigenere cipher, rot13, etc.) |

## Legal and Ethical Notes

### Educational Use Only

This tool is designed for educational purposes. Key principles:

- **Caesar cipher is extremely weak** and should never be used for protecting real data
- **Only use on educational materials** you create or have permission to encrypt
- **Never use for securing real communications** or sensitive information
- **Understand historical context** of classical cryptography techniques

### Learning Value

Understanding classical ciphers helps students:

- Grasp fundamental cryptography concepts
- Learn about the evolution of encryption techniques
- Appreciate modern cryptographic security requirements
- Understand why weak ciphers should not be used in production

### Legal Compliance

- Use only on materials you own or have permission to encrypt
- Educational purpose only - do not use for actual security purposes
- Follow institutional policies regarding cryptography tools

## License

MIT - This project is free to use, modify, and distribute for educational purposes. See the LICENSE file for full terms and conditions.