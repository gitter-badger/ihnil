"""
IHNIL main parsing module.

Provides the interface for evaluating a given target file
"""

import argparse
import os
import ast
import codegen
import copy


parser = argparse.ArgumentParser(description="Python 'if' loop optimizer",
                                 epilog="For details see "
                                 "https://github.com/forstmeier/ihnil")

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


class ReadIHNIL(ast.NodeVisitor):
    """This class provides simple error node code print out."""

    count = 1

    def visit_If(self, node):
        """Subclassed ast module method."""
        if isinstance(node.body[0], ast.If):
            print("[> Nested 'if' error number {} <]".format(self.count))
            print("[> Error node starts on {} <]\n".format(node.lineno))
            print(codegen.to_source(node) + "\n")
            input("Hit Enter to continue\n")
            self.count += 1


class WriteIHNIL(ast.NodeVisitor):
    """This class allows for comprehensive code optimization."""

    def visit_If(self, node):
        """Subclassed ast module method."""
        if isinstance(node.body[0], ast.If) and node.orelse == []:

            self.next_line(node)

            decider = input("Would you like to:\n"
                            "Accept change  ->  'a'\n"
                            "Edit manually  ->  'e'\n"
                            "Mark complete  ->  'c'\n"
                            "Provide your choice and hit Enter: ")

            if decider == "a":
                self._accept_change()
            elif decider == "e":
                self._edit_manually()
            elif decider == "c":
                self._mark_complete()
            else:
                print("No action taken")

    def next_line(self, line):
        """Node line evaluation function called recursively."""
        if isinstance(line, ast.If) and line.orelse == []:

            print(self.sort_algo(line))

            self.next_line(line.body[0])

    def sort_algo(self, input_line):
        line_holder = list()
        if isinstance(input_line.test, ast.Compare):
            if len(input_line.test.ops) > 1:
                line_holder.append(input_line)
            else:
                self.eval_left(input_line, line_holder)
        else:
            line_holder.append(input_line)
        return line_holder  # stores all lines & line alternative collections

    def eval_left(self, input_line, line_holder):
        alt_holder = list()
        alt_holder.append(input_line.test.ops[0])
        alt_holder.append(input_line.test.comparators[0])
        if isinstance(input_line.test.left, ast.Name):
            alt_holder.insert(0, input_line.test.left.id)
            line_holder.append(alt_holder)
        elif isinstance(input_line.test.left, ast.BinOp):
            self.eval_binop(input_line.test.left, alt_holder, line_holder)
        return line_holder

    def eval_binop(self, input_line, alt_holder, line_holder):
        if isinstance(input_line.left, ast.Name):
            left_holder = copy.copy(alt_holder)
            left_holder.append(self.oper_swap(ast.dump(input_line.op)))
            left_holder.append(input_line.right)
            left_holder.insert(0, input_line.left.id)
            line_holder.append(left_holder)
            del(left_holder)
        elif isinstance(input_line.left, ast.BinOp):
            self.eval_binop(input_line.left, left_holder, line_holder)
        if isinstance(input_line.right, ast.Name):
            right_holder = copy.copy(alt_holder)
            right_holder.append(self.oper_swap(ast.dump(input_line.op)))
            right_holder.append(input_line.left)
            right_holder.insert(0, input_line.right.id)
            line_holder.append(right_holder)
            del(right_holder)


    def oper_swap(self, oper):
        OPER_DICT = {"Add()": "-", "Sub()": "+",
                     "Mult()": "/", "Div()": "*",
                     "FloorDiv()": "//", "Mod()": "%", "Pow()": "**",
                     "Gt()": "Lt()", "Lt()": "Gt()",
                     "GtE()": "LtE()", "LtE()": "GtE()",
                     "Eq()": "NotEq()", "NotEq()": "Eq()",
                     "Is()": "IsNot()", "IsNot()": "Is()",
                     "In()": "NotIn()", "NotIn()": "In()"}
        return OPER_DICT[oper]

    def _accept_change(self):
        """Private method to automatically apply optimized code."""
        pass

    def _edit_manually(self):
        """Private method to allow for manual code adjustments."""
        pass

    def _mark_complete(self):
        """Private method to mark and ignore non-optimized code."""
        pass


class ElseIHNIL(ast.NodeVisitor):
    """This class is the default error node line number identifier."""

    count = 1

    def visit_If(self, node):
        """Subclassed ast module method."""
        if isinstance(node.body[0], ast.If):
            print("[> Nested 'if' number {} start "
                  "line {}".format(self.count, node.lineno))
            self.end_line(node, self.count)
            self.count += 1

    def end_line(self, node, count):
        """Private recursive method to loop down to the last node line."""
        if isinstance(node, ast.If):
            self.endno = node.lineno
            self.end_line(node.body[0], count)
        else:
            print("[> Nested 'if' number {} end "
                  "line {}".format(count, self.endno))


if file_extension == ".py":
    with open(args.file_name.name) as f:
        file_contents = f.read()
    module = ast.parse(file_contents)

    if args.read:
        ReadIHNIL().visit(module)
    elif args.write:
        WriteIHNIL().visit(module)
    else:
        ElseIHNIL().visit(module)
else:
    print("\nPlease enter a Python file\n")
