#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as ex:
        import sys
        print("Exception: {}".format(ex.args[0]), file=sys.stderr)
