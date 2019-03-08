import importlib

spam = importlib.import_module("spam")
bar = importlib.import_module("bar")

spam.spam()
bar()