#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Compiler Project - CS335A
Milestone 2: Symbol Table and 3AC
Ashok Vishwakarma | 180151
Viraj | 180870

"""

import sys


class threeAC:

    def __init__(self):
        self.code = []
        self.lNo = -1

    # destination, source1, source2, operator
    def emit(self, des, src1, src2, op):
        self.code.append([des, src1, src2, op])

    def newLabel(self):
        self.lNo += 1
        return "l" + str(self.lNo)

    def output(self):
        for i in self.code:
            print(i)

    def error(self, error):
        self.dump3ACToTXT()
        print(error)
        sys.exit(0)

    def dump3ACToTXT(self):
        # name of txt file
        filename = "threeAC.txt"

        count = 0
        with open(filename, "w") as file:
            for i in self.code:
                count += 1

                if (i[0] == 'ifgoto'):
                    x = i[2].split(' ')
                    file.write(str(
                        count) + ", " + i[0] + ", " + x[0] + ", " + i[1] + ", " + x[1] + ", " + i[3] + "\n")
                elif (i[0] == 'print'):
                    file.write(str(count) + ", print, " + i[1] + "\n")
                elif (i[0] == 'func'):
                    file.write(str(count) + ", func" + "\n")
                elif (i[0] == 'declare'):
                    file.write(str(count) + ", declare" +
                               ", " + i[1] + ", " + i[2] + "\n")
                elif (i[0] == 'label'):
                    file.write(str(count) + ", label, " + i[1] + "\n")
                elif (i[0] == 'goto' or i[0] == 'call'):
                    file.write(str(count) + ", " + i[0] + ", " + i[1] + "\n")
                elif (i[0] == 'input'):
                    file.write(str(count) + ", " + i[0] + ", " + i[1] + "\n")
                elif (i[0] == 'ret'):
                    file.write(str(count) + ", ret" + "\n")
                elif (i[0] == 'error'):
                    file.write(i[1] + " = " + i[2] + "\n")
                    sys.exit(0)
                else:
                    if (i[3] == '='):
                        file.write(str(count) + ", " +
                                   i[3] + ", " + i[0] + ", " + i[1] + "\n")
                    else:
                        file.write(
                            str(count) + ", " + i[3] + ", " + i[0] + ", " + i[1] + ", " + i[2] + "\n")

        print("3AC is generated as threeAC.txt file in the same directory!")
