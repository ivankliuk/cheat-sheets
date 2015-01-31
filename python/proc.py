__doc__ = """
Processes handling.
"""

import os
import sys

# Exit from parent process (forking)
if os.fork():
    sys.exit()
