"""
A small `dog` class example.
"""

from typing import List, Optional


class Dog:
    """🐕"""

    name: str
    """The name of our dog."""
    friends: list[str]
    """The friends of our dog."""

    def __init__(self, name: str, friends: Optional[List[str]] = None) -> None:
        """Make a Dog."""
        self.name = name
        self.friends = friends or []

    def bark(self, loud: bool = True) -> str:
        """*woof*"""
        sound = "*woof* " + " *woof* ".join(self.friends)
        return f"{sound.upper()}!!!" if loud else sound
