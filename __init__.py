"""
MCC/__init__.py

A Master Correlated Catalog Creation Package.
"""

__author__      = "Brian Leist  (brian.leist@louisville.edu)"
__license__     = "University of Louisville"
__version__     = "beta"

from .Master            import Master
from .Correlation       import correlate, clean_duplicates, combine
from .Create            import create
