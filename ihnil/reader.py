"""
Python script parsing module.

Description:

    Prounounced "eye-nil"; this tool allows the user to identify and improve
    upon nested "if" loop statements.

Arguments:

    file_name       The target file to parse
    -h, --help      Show help message
    -r, --read      Displays the errors and location in the terminal
    -w, --write     Inserts recommended code changes into the script

"""

import argparse
import os
import tokenize
import operator
import itertools
import keyword


parser = argparse.ArgumentParser(description="Python 'if' loop optimizer",
                                 epilog="For details see \
                                         https://github.com/forstmeier/ihnil")

parser.add_argument("file_name",
                    type=argparse.FileType(),
                    help="input file for %(prog)s optimization")

output = parser.add_mutually_exclusive_group()
output.add_argument("-r", "--read",
                    action="store_true",
                    help="find and print 'if' loop errors to the terminal")
output.add_argument("-w", "--write",
                    action="store_true",
                    help="write 'if' alternatives to the module and terminal")

args = parser.parse_args()
string_name = str(args.file_name.name)
file_extension = os.path.splitext(string_name)[1]


class MainIHNIL(object):
    """Core object for code parsing and output methods."""

    def __init__(self, inpt):
        """
        Establish necessary variables.

        self.inpt       : list of 5-tuple tokenized input module code
        self.ordr       : dictionary of rows and associated tokens
        self.rows       : list of row values of "if" statement tokens
        self.nest       : list of consecutive row value lists
        """
        self.inpt = inpt
        self.ordr = {grp: list(itm)
                     for grp, itm in itertools.groupby(self.inpt,
                                                       lambda x: x.start[0])}
        self.rows = [tkn.start[0] for tkn in self.inpt
                     if tkn.string == "if"]
        self.nest = [lst for lst in
                     [list(map(operator.itemgetter(1), i))
                      for g, i in itertools.groupby(enumerate(self.rows),
                                                    lambda ix: ix[0] - ix[1])]
                     if len(lst) > 1]

    def _read_out(self):
        lines = [[(dct, self.ordr[val][0].line.rstrip().lstrip())
                 for val in nst for dct in self.ordr
                 if val == dct] for nst in self.nest]
        for grp in lines:
            spaces = 2
            start = grp[0][0]
            end = grp[-1][0]
            print("Nested error number {}".format(lines.index(grp) + 1))
            print("Start row: {}, end row: {}\n".format(start, end))
            for row in grp:
                print("[>{}{}".format(" " * spaces, row[1]))
                spaces += 4
            print()

    def _write_out(self):
        kwds = keyword.kwlist

        cond = ["<", ">", "<=", ">=", "!=", "=="]

        bltn_func = [var for var in dir(__builtins__) if "__" not in var]
        stng_func = [var for var in dir(__builtins__.str) if "__" not in var]
        lsts_func = [var for var in dir(__builtins__.list) if "__" not in var]

        combo = [[[(tok.string, tokenize.tok_name[tok.exact_type])
                 for tok in self.ordr[dct]]
                 for val in nst for dct in self.ordr
                 if val == dct] for nst in self.nest]
        for grp in combo:
            for row in grp:
                for itm in row:
                    print(itm[0])

    def _else_out(self):
        for nst in self.nest:
            print("Nested error number {}".format(self.nest.index(nst) + 1))
            print("Start row: {}, end row: {}".format(min(nst), max(nst)))

if file_extension == ".py":
    with open(args.file_name.name, "rb") as t_file:
        tokens = list(tokenize.tokenize(t_file.readline))
    instance = MainIHNIL(tokens)

    if args.read:
        instance._read_out()
    elif args.write:
        instance._write_out()
    else:
        instance._else_out()
else:
    print("\nPlease enter a Python file\n")