#!/usr/bin/python3
from importlib import util
import sys
if __name__ == "__main__":
    spec =util.spec_from_file_location("variable_module", "./variable_load_5.py")
    variable_module = util.module_from_spec(spec)
    spec.loader.exec_module(variable_module)
    a = variable_module.a
    print(a)
