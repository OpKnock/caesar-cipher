"""Tests for Caesar cipher CLI."""

import pytest
from typer.testing import CliRunner
from caesar_cipher.main import app

runner = CliRunner()


def test_encrypt_command():
    result = runner.invoke(app, ["encrypt", "HELLO", "--key", "3"])
    assert result.exit_code == 0
    assert "KHOOR" in result.output


def test_decrypt_command():
    result = runner.invoke(app, ["decrypt", "KHOOR", "--key", "3"])
    assert result.exit_code == 0
    assert "HELLO" in result.output


def test_crack_command():
    ciphertext = "KHOOR"
    result = runner.invoke(app, ["crack", ciphertext, "--top", "3"])
    assert result.exit_code == 0
    assert "KHOOR" in result.output or "shift" in result.output.lower()


def test_crack_all_flag():
    result = runner.invoke(app, ["crack", "HELLO", "--all"])
    assert result.exit_code == 0
    assert "Shift" in result.output


def test_freq_command():
    result = runner.invoke(app, ["freq", "HELLO WORLD"])
    assert result.exit_code == 0
    assert "Frequency" in result.output


def test_invalid_key():
    result = runner.invoke(app, ["encrypt", "HELLO", "--key", "30"])
    assert result.exit_code != 0


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "encrypt" in result.output
    assert "decrypt" in result.output
    assert "crack" in result.output