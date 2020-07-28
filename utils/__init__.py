import sys
try:
    from utils.decorator import *
    from utils.provider import *
except ImportError:
    print("\tSome dependencies could not be imported (possibly not installed) ")
    print("Type `pip3 install -r requirments.txt` to install all required packages")
    sys.exit(1)