#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Compiler Project - CS335A
Milestone 3
Ashok Vishwakarma | 180151
Viraj | 180870

"""


import sys


class symTable:

    def __init__(self):
        self.symTable = {
            'start': {
                'name': 'start',
                'variables': {},
                'function': {},
                'type': 'start',
                'parent': None,
            }
        }
        self.currScope = 'start'
        self.tNo = -1
        self.scopeNo = -1

    def variableAdd(self, idVal, place, idType, idDimension=[]):
        idSize = 4
        scope = self.getScope(idVal)
        if scope != self.currScope:
            sc = str(self.currScope)+'_'+place
            self.symTable[self.currScope]['variables'][idVal] = {
                'place': sc,
                'type': idType,
                'size': idSize,
                'dimension': idDimension
            }
        else:
            sys.exit('Variable '+idVal+" is already initialised in this scope")

    def variableSearch(self, idVal):
        scope = self.getScope(idVal)
        if (scope == None):
            return False
        else:
            return scope

    def functionAdd(self, func):
        # this is added to handle parameterised function
        self.symTable[func] = {
            'name': func,
            'type': 'function',
            'variables': {},
            'function': {},
            'rType': 'UNDEFINED_TYPE',
            'parent': self.currScope,
        }

        self.symTable[self.currScope]['function'][func] = {
            'fName': func
        }
        self.currScope = func

    def newScope(self):
        scope = self.newScopeName()
        self.symTable[scope] = {
            'name': scope,
            'type': 'block',
            'variables': {},
            'function': {},
            'type': 'scope',
            'parent': self.currScope,
        }
        self.currScope = scope

    def endScope(self):
        self.currScope = self.symTable[self.currScope]['parent']

    def endFunction(self):
        self.currScope = self.symTable[self.currScope]['parent']

    def retScope(self):
        return self.currScope

    def getScopeType(self, scope):
        return self.symTable[scope]['type']

    def setRType(self, dataType):
        self.symTable[self.currScope]['rType'] = dataType

    def getRType(self, scope):
        return self.symTable[scope]['rType']

    def getFunction(self):
        scope = self.currScope
        while self.symTable[scope]['type'] not in ['function']:
            scope = self.symTable[scope]['parent']
        return self.symTable[scope]['name']

    def variableSave(self, scope):
        lis = []
        while (self.symTable[scope]['type'] not in ['function']):
            h = self.getScopeVariables(scope)
            lis = lis + h
            scope = self.symTable[scope]['parent']

        h = self.getScopeVariables(scope)
        lis = lis + h
        return lis

    def getScopeVariables(self, scope):
        l = self.symTable[scope]['variables']
        lis = []
        for i in l:
            if (i not in ['in']):
                lis.append(l[i]['place'])
        return lis

    def getData(self, idVal, search):
        scope = self.getScope(idVal)
        if scope != None:
            return self.symTable[scope]['variables'][idVal].get(search)
        else:
            return None

    def setDimension(self, idVal, NewDimension):
        scope = self.getScope(idVal)
        if scope != None:
            self.symTable[scope]['variables'][idVal]['dimension'] = NewDimension
            return
        else:
            return None

    def getScope(self, idVal):
        scope = self.currScope
        while self.symTable[scope]['type'] not in ['start']:
            if idVal in self.symTable[scope]['variables']:
                return scope
            scope = self.symTable[scope]['parent']
        if idVal in self.symTable[scope]['variables']:
            return scope
        return None

    def getTemp(self):
        self.tNo += 1
        newTemp = "t"+str(self.tNo)
        self.variableAdd(newTemp, newTemp, 'INT')
        return self.currScope+'_'+newTemp

    def newScopeName(self):
        self.scopeNo += 1
        newScope = "s"+str(self.scopeNo)
        return newScope
