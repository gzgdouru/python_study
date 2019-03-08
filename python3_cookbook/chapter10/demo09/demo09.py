import os
import sys

mydir_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(mydir_path, "mydir"))

from spam import spam
from bar import bar

spam()
bar()