# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/codesnap/blob/master/NOTICE.txt

import sys
import argparse
from . import CodeSnap

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--tracer", nargs="?", choices=["c", "python"], default="c")
    parser.add_argument("--output_file", "-o", nargs="?", default="result.html")
    parser.add_argument("--quiet", action="store_true", default=False)
    parser.add_argument("--max_stack_depth", nargs="?", type=int, default=-1)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    options = parser.parse_args(sys.argv[1:])
    try:
        f = options.command[0]
        code_string = open(f).read()
    except FileNotFoundError:
        print("No such file as {}".format(f))
        exit(1)
    sys.argv = options.command[1:]
    if options.quiet:
        verbose = 0
    else:
        verbose = 1
    snap = CodeSnap(
        tracer=options.tracer, 
        verbose=verbose,
        max_stack_depth=options.max_stack_depth
    )
    snap.start()
    exec(code_string)
    snap.stop()
    snap.save(output_file=options.output_file)
