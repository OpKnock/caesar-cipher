"""Caesar cipher CLI with Typer and Rich."""

import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from caesar_cipher.core import (
    caesar_shift,
    crack_caesar,
    format_crack_results,
    frequency_analysis,
    chi_squared_score,
)

app = typer.Typer(
    name="caesar-cipher",
    help="Caesar cipher encryption, decryption, and brute-force cracking CLI with frequency analysis.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def encrypt(
    text: str = typer.Argument(..., help="Plaintext to encrypt"),
    key: int = typer.Option(3, "--key", "-k", help="Shift key (0-25)", min=0, max=25),
):
    """Encrypt plaintext using Caesar cipher with specified shift key."""
    ciphertext = caesar_shift(text, key, encrypt=True)
    
    table = Table(title="Encryption Result")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Plaintext", text)
    table.add_row("Key", str(key))
    table.add_row("Ciphertext", ciphertext)
    
    console.print(table)


@app.command()
def decrypt(
    text: str = typer.Argument(..., help="Ciphertext to decrypt"),
    key: int = typer.Option(3, "--key", "-k", help="Shift key (0-25)", min=0, max=25),
):
    """Decrypt ciphertext back to plaintext with the original key."""
    plaintext = caesar_shift(text, key, encrypt=False)
    
    table = Table(title="Decryption Result")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Ciphertext", text)
    table.add_row("Key", str(key))
    table.add_row("Plaintext", plaintext)
    
    console.print(table)


@app.command()
def crack(
    text: str = typer.Argument(..., help="Ciphertext to crack"),
    top: int = typer.Option(5, "--top", "-t", help="Number of top results to show", min=1, max=26),
    show_all: bool = typer.Option(False, "--all", help="Show all 26 shifts"),
):
    """Brute-force crack unknown ciphertext by testing all 26 shifts with frequency analysis."""
    results = crack_caesar(text)
    
    if show_all:
        for r in results:
            console.print(f"Shift {r.shift:2d} (score: {r.score:6.2f}): {r.plaintext}")
    else:
        output = format_crack_results(results, top_n=top)
        console.print(Panel(output, title="Brute-Force Results (Ranked by Chi-Squared)", border_style="green"))
        
        best = results[0]
        console.print(f"\n[bold green]Most likely shift:[/bold green] {best.shift}")
        console.print(f"[bold green]Plaintext:[/bold green] {best.plaintext}")


@app.command()
def freq(
    text: str = typer.Argument(..., help="Text to analyze"),
):
    """Show letter frequency analysis of text."""
    freq = frequency_analysis(text)
    score = chi_squared_score(freq)
    
    table = Table(title=f"Frequency Analysis (Chi-Squared: {score:.2f})")
    table.add_column("Letter", style="cyan")
    table.add_column("Count %", style="green")
    table.add_column("English %", style="yellow")
    
    from caesar_cipher.core import ENGLISH_FREQ
    for char in sorted(freq.keys()):
        table.add_row(char.upper(), f"{freq[char]:.2f}", f"{ENGLISH_FREQ.get(char, 0):.2f}")
    
    console.print(table)


def main():
    app()


if __name__ == "__main__":
    main()