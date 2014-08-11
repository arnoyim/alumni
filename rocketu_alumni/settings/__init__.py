"""
Settings used by rocketu_alumni project.

This consists of the general produciton settings, with an optional import of any local
settings.
"""

# Import production settings.
from rocketu_alumni.settings.production import *

# Import optional local settings.
try:
    from rocketu_alumni.settings.local import *
except ImportError:
    pass