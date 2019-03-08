import sys

sys.path.extend(["foo-package", "bar-package"])

import spam

print(spam.__path__)

from spam.grok import grok
from spam.blah import blah

grok()
blah()
