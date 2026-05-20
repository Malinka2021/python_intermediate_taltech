"""Banknotes needed for amount."""


def banknotes(amount: int) -> int:
    """How many banknotes are required for the amount.

    Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.
    Given the amount, return how many banknotes does it take to cover the sum. Task is to cover the sum with as little
    banknotes as possible.
    The amount of different banknotes is not limited in the machine.
    Example:
    The amount is 72€
    We use four banknotes to cover it. The banknotes are 50€, 20€, 1€ and 1€.
    The result is 4.
    """
    total_banknotes = 0

    # Available denominations
    denominations = [100, 50, 20, 10, 5, 1]

    for note in denominations:
        if amount >= note:
            count = amount // note  # How many of this note we need
            total_banknotes += count  # Itiration
            amount -= count * note  # Reduce the remaining amount

    return total_banknotes


if __name__ == '__main__':
    print(banknotes(12))

