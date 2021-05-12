import sys
from .base import *

# try:
#     from .local import *
#
#     live = False
# except ImportError:
#     live = True
#
# if live:
#     from .prod import *

RUNNING_DEVSERVER = (len(sys.argv) > 1 and sys.argv[1] == 'runserver')
if RUNNING_DEVSERVER:
    from .local import *
else:
    from .prod import *

"""
dont forget to add BASE_DIR parent dir !! because of different settings 
"""
