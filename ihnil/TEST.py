"""This is the test Python document"""

def multipy(x, y):
    """This is the multipy docstring"""
    print(x * y)

if True:
    print("Only a flesh wound")

def evenpy(num):
    # This is a test comment string
    if num == 0:
        print("Input is zero")
    elif num == 1:
        print("Input is odd")
    elif num % 2 == 0:
        print("Input is even")
    else:
        print("Input is odd")

def manyif(val):
    if val > 0:
        if val != 2:
            if val < 3:
                print("Eggs & spam")

class Basic():
    """This is the Basic docstring"""
    def __init__(self, val):
        self.val = val

    # Here is another comment
    def printr(self):
        print("The input value is " + str(self.val))

def listif(inp, num):
    if inp + num > 0:
        if num % 2 == 0:
            if 20 > inp:
                if inp != "SPAMELOT":
                    if inp in [1, 2, 3]:
                        if inp != num:
                            if num + 10 != inp + 20:
                                if inp == (num % 2):
                                    print(inp)

def brutal(val1, val2):
    if val1 != 5:
        if 1 < val2 < 10 < val1 < 20:
            if val1 < val2 != 15 + val1:
                print("THE HOLY GRAIL")
