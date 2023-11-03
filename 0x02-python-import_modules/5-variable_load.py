#!/usr/bin/python3
import importlib.util
import sys
if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("variable_module", "./variable_load_5.py")
    variable_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(variable_module)
    a = getattr(variable_module, 'a', None)
    print(a)
