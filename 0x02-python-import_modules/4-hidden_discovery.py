#!/usr/bin/python3
import importlib.util
import sys
if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_module",
                                                  "./hidden_4.pyc")
    hidden_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_module)
    names = dir(hidden_module)
    names = [name for name in names if not name.startswith('__')]
    names.sort()
    for name in names:
        print(name)
