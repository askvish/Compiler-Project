#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Compiler Project - CS335A
Milestone 2: Symbol Table and 3AC
Ashok Vishwakarma | 180151
Viraj | 180870

"""

import sys
import csv


class symTable:

    def __init__(self):
        self.symTable = {
            'main': {
                'name': 'main',
                'identifiers': {},
                'type': 'main',
                'parent': None,
            }
        }
        self.currScope = 'main'
        self.tNo = -1
        self.scopeNo = -1

    def newScope(self):
        scope = self.newScopeName()
        self.symTable[scope] = {
            'name': scope,
            'identifiers': {},
            'type': 'scope',
            'parent': self.currScope,
        }
        self.currScope = scope

    def endScope(self):
        self.currScope = self.symTable[self.currScope]['parent']

    def variableAdd(self, idVal, place, idType, idSize=4):
        if idSize == 4:
            idSize = self.getSize(idType)
        scope = self.getScope(idVal)
        if scope != self.currScope:
            sc = str(self.currScope)+'_'+place
            self.symTable[self.currScope]['identifiers'][idVal] = {
                'place': sc,
                'type': idType,
                'size': idSize
            }
        else:
            sys.exit('Variable '+idVal+" is already initialised in this scope")
        # print(self.symTable[self.currScope]['identifiers'])

    def varSearch(self, idVal):
        scope = self.getScope(idVal)
        # print(scope)
        if (scope == None):
            return False
        else:
            return scope

    def getAttribute(self, idVal, Name):
        scope = self.getScope(idVal)
        if scope != None:
            return self.symTable[scope]['identifiers'][idVal].get(Name)
        else:
            return None

    def addAttribute(self, idVal, Name, Val):
        scope = self.getScope(idVal)
        if scope != None:
            self.symTable[self.getScope(
                idVal)]['identifiers'][idVal][Name] = Val
            return True
            # print("Success")
        else:
            # print("Fail")
            return False

    def getSize(self, typeExpr):
        if typeExpr in ['INT', 'BOOLEAN', 'FLOAT', 'CHAR', 'VOID']:
            return 4

    def getTemp(self):
        self.tNo += 1
        newTemp = "t"+str(self.tNo)
        return newTemp

    def getScope(self, idVal):
        scope = self.currScope
        while self.symTable[scope]['type'] not in ['main']:
            if idVal in self.symTable[scope]['identifiers']:
                return scope
            scope = self.symTable[scope]['parent']

        if idVal in self.symTable[scope]['identifiers']:
            return scope
        return None

    def newScopeName(self):
        self.scopeNo += 1
        newScope = "s"+str(self.scopeNo)
        return newScope

    def dumpSymbolTableToCSV(self):

        # print(self.symTable)
        # header row of csv file
        header = ['Name', 'Identifiers', 'Type', 'Parent']
        # data rows of csv file
        rows = []

        for i in self.symTable:
            row = []
            for j in self.symTable[i]:
                if (j == 'name'):
                    row.append(self.symTable[i]['name'])
                if (j == 'identifiers'):
                    row.append(self.symTable[i]['identifiers'])
                    # for k in self.symTable[i]['identifiers']:
                    #     for iden in self.symTable[i]['identifiers'][k]:
                    #         print("\t-->", self.symTable[i]['identifiers'][k][iden])
                if (j == 'type'):
                    row.append(self.symTable[i]['type'])
                if (j == 'parent'):
                    if (self.symTable[i]['parent'] == None):
                        self.symTable[i]['parent'] = 'None'
                    row.append(self.symTable[i]['parent'])
            rows.append(row)

        # name of csv file
        filename = "symTable.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the header
            csvwriter.writerow(header)

            # writing the data rows
            csvwriter.writerows(rows)

        print("Symbol Table is generated as symTable.csv file in the same directory!")
