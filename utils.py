import os

# Constants
gravitational_constant = 10


def clear() -> None:
    """
    Clear the terminal screen.

    This function is cross-platform and will work on both Windows and Unix-like systems.
    """
    
    os.system('cls' if os.name == 'nt' else 'clear')
