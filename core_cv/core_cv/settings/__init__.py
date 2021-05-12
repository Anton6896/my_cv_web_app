from .base import *

try:
    from .local import *

    live = False
except ImportError:
    live = True

if live:
    from .prod import *

"""
dont forget to add BASE_DIR parent dir !! because of different settings 
"""
