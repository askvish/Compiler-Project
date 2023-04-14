#!/usr/bin python
# -*- coding: utf-8 -*-

"""
Compiler Project - CS335A
Milestone 3
Ashok Vishwakarma | 180151
Viraj | 180870

"""


import ply.lex as lex
import ply.yacc as yacc
from JavaLexer import tokens

from symTable import symTable
from threeAC import threeAC
import sys


stackend = []
stackbegin = []

function = []


# Call this function whenever array is on right hand side of =


def ResolveRHSArray(d):
    if ('isArrayAccess' in d.keys() and d['isArrayAccess']):
        dst1 = ST.getTemp()
        TAC.emit(dst1, d['place']+"["+d['index_place']+"]", '', '=')
        d['place'] = dst1
        d['isArrayAccess'] = False
        del d['index_place']
    return d


def p_CompilationUnit(p):
    '''CompilationUnit : ProgramFile
    '''


def p_ProgramFile(p):
    ''' ProgramFile : ImportStmts TypeDeclarationOptSemi
                | ImportStmts
                | TypeDeclarationOptSemi
    '''


def p_ImportStmts(p):
    '''ImportStmts : ImportStmt
                    | ImportStmts ImportStmt
    '''


def p_ImportStmt(p):
    '''ImportStmt : KEYIMPORT QualifiedName Semicolons
                    | KEYIMPORT QualifiedName SEPDOT OPMULTIPLY Semicolons
    '''


def p_QualifiedName(p):
    '''QualifiedName : Identifier
                | QualifiedName SEPDOT Identifier
    '''
    if (len(p) == 2):
        p[0] = {
            'idVal': p[1],
            'isnotjustname': False
        }
    else:
        p[0] = {
            'idVal': p[1]['idVal']+"."+p[3]
        }


def p_Semicolons(p):
    '''Semicolons : SEPSEMICOLON
                | Semicolons SEPSEMICOLON
    '''


def p_TypeSpec(p):
    '''TypeSpec : TypeName
            | TypeName Dims
    '''
    if (len(p) == 2):
        p[0] = {
            'type': p[1].upper()
        }
        return
    else:
        p[0] = {
            'type': p[1].upper(),
            'dim': p[2]
        }


# don't know what is Dims
def p_TypeName(p):
    '''TypeName : PrimitiveType
            | QualifiedName
    '''
    p[0] = p[1]['idVal']


def p_PrimitiveType(p):
    '''PrimitiveType : KEYBOOLEAN
                | KEYCHAR
                | KEYDOUBLE
                | KEYBYTE
                | KEYSHORT
                | KEYINT
                | KEYLONG
                | KEYVOID
                | KEYFLOAT
                | KEYSTRING
    '''
    # it is idenname because in the case of struct, we are passing the type as iden name through qualified type
    p[0] = {
        'idVal': p[1]
    }


def p_ClassNameList(p):
    '''ClassNameList : QualifiedName
                 | ClassNameList SEPCOMMA QualifiedName
    '''


def p_TypeDeclarationOptSemi(p):
    '''TypeDeclarationOptSemi : TypeDeclaration
                    | TypeDeclaration Semicolons
    '''


def p_TypeDeclaration(p):
    '''TypeDeclaration : ClassHeader SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
                    | ClassHeader SEPLEFTPARAN SEPRIGHTPARAN
    '''


def p_ClassHeader(p):
    '''ClassHeader : Modifiers ClassWord Identifier
                | ClassWord Identifier
    '''


def p_ClassWord(p):
    '''ClassWord : KEYCLASS'''


def p_FieldDeclarations(p):
    '''FieldDeclarations : FieldDeclarationOptSemi
                    | FieldDeclarations FieldDeclarationOptSemi
    '''


def p_FieldDeclarationOptSemi(p):
    '''FieldDeclarationOptSemi : FieldDeclaration
                               | FieldDeclaration Semicolons
    '''


def p_FieldDeclaration(p):
    '''FieldDeclaration : FieldVarDeclaration SEPSEMICOLON
                        | MethodDeclaration
                        | TypeDeclaration
    '''


def p_FieldVarDeclaration(p):
    '''FieldVarDeclaration : Modifiers TypeSpec VarDeclarators
                                | TypeSpec VarDeclarators
    '''
    if (len(p) == 3):
        for i in p[2]:
            if (p[1]['type'] == 'SCANNER'):
                p[1]['type'] = 'INT'
            # add variables in the symbol table and it's type
            ST.variableAdd(i, i, p[1]['type'])

    else:
        TAC.error("We are not supporting Modifiers to Primitive Datatypes")


def p_VarDeclarators(p):
    '''VarDeclarators : VarDeclarator
                            | VarDeclarators SEPCOMMA VarDeclarator
    '''

    # add list of variables
    if (len(p) == 2):
        p[0] = p[1]
        return
    p[0] = p[1]+p[3]


def p_VarDeclarator(p):
    ''' VarDeclarator : DeclaratorName
                            | DeclaratorName OPEQUAL VariableInit
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return

    if (type(p[3]) != type({})):
        return
    if ('isarray' in p[3].keys() and p[3]['isarray']):
        TAC.emit('declare', p[1][0], p[3]['place'], p[3]['type'])
        p[0] = p[1]
    else:
        if ('isArrayAccess' in p[3].keys() and p[3]['isArrayAccess']):
            ResolveRHSArray(p[3])
            rt = ST.retScope()
            TAC.emit(rt+'_'+p[1][0], p[3]['place'], '', p[2])
        else:
            rt = ST.retScope()
            TAC.emit(rt+'_'+p[1][0], p[3]['place'], '', p[2])
        p[0] = p[1]


def p_VariableInit(p):
    '''VariableInit : Expression
                            | SEPLEFTPARAN SEPRIGHTPARAN
                            | SEPLEFTPARAN ArrayInit SEPRIGHTPARAN
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_ArrayInit(p):
    '''ArrayInit : VariableInit
                            | ArrayInit SEPCOMMA VariableInit
                            | ArrayInit SEPCOMMA
    '''


def p_MethodDeclaration(p):
    '''MethodDeclaration : Modifiers TypeSpec MethodDeclarator MethodBody FMark2
                        | Modifiers TypeSpec MethodDeclarator Throws MethodBody FMark3
                        | TypeSpec MethodDeclarator Throws MethodBody FMark3
                        | TypeSpec MethodDeclarator MethodBody FMark2
    '''


def p_FMark2(p):
    '''FMark2 : '''
    if (p[-2][1] not in ['main0']):
        TAC.emit('ret', '', '', '')


def p_FMark3(p):
    '''FMark3 : '''
    if (p[-3][1] not in ['main0']):
        TAC.emit('ret', '', '', '')


def p_Throws(p):
    '''Throws : KEYTHROWS ClassNameList
    '''


def p_MethodDeclarator(p):
    '''MethodDeclarator : DeclaratorName SEPLEFTBRACE SEPRIGHTBRACE
                    | DeclaratorName SEPLEFTBRACE ParamList SEPRIGHTBRACE
                    | MethodDeclarator OP_DIM
    '''
    if (len(p) == 4):
        arg = 0
        p[0] = ['funct']+p[1]
        g = p[1][0]+str(arg)
        p[0][1] = g
        if (g in function):
            TAC.error(
                'Error: function with same name and same number of arguments is already defined')
        else:
            function.append(g)
        TAC.emit('func', g, p[0], '')
    elif (len(p) == 5):
        p[0] = ['funct']+p[1]+p[3]
        arg = len(p[3])
        g = p[1][0]+str(arg)
        p[0][1] = g
        if (g in function):
            TAC.error(
                'Error: function with same name and same number of arguments is already defined')
        else:
            function.append(g)
        TAC.emit('func', g, p[0], '')


def p_ParamList(p):
    '''ParamList : Parameter
                    | ParamList SEPCOMMA Parameter
    '''
    if (len(p) == 2):
        l = []
        l = l + p[1]['place']+[p[1]['type']]
        p[0] = [l]
        return
    else:
        l = []
        l = l + p[3]['place']+[p[3]['type']]
        p[0] = p[1] + [l]


def p_Parameter(p):
    '''Parameter : TypeSpec DeclaratorName
       '''
    # Array being passed is not handled
    p[0] = {
        'type': p[1]['type'],
        'place': p[2]
    }


def p_DeclaratorName(p):
    '''DeclaratorName : Identifier
                    | DeclaratorName OP_DIM
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
        return


def p_MethodBody(p):
    '''MethodBody : Block
                | SEPSEMICOLON
    '''


# 3
def p_Modifiers(p):
    '''Modifiers : Modifier
                | Modifiers Modifier
    '''


def p_Modifier(p):
    '''Modifier : KEYPUBLIC
                | KEYPROTECTED
                | KEYPRIVATE
                | KEYSTATIC
                | KEYFINAL
    '''


def p_Block(p):
    '''Block : SEPLEFTPARAN BMark1 LocalVarDeclarationsAndStmt BMark2 SEPRIGHTPARAN
            | SEPLEFTPARAN SEPRIGHTPARAN
    '''


def p_BMark1(p):
    '''BMark1 : '''
    if (p[-2] != None):
        if (p[-2][0] == 'funct'):
            ST.functionAdd(p[-2][1])
            ST.setRType(p[-3]['type'])
            l = len(p[-2])
            for i in range(2, l):
                ST.variableAdd(p[-2][i][0], p[-2][i][0], p[-2][i][1])
            return
    ST.newScope()


def p_BMark2(p):
    '''BMark2 : '''
    if (p[-4] != None):
        if (p[-4][0] == 'funct'):
            ST.endFunction()
            return
    ST.endScope()


def p_LocalVarDeclarationsAndStmt(p):
    '''LocalVarDeclarationsAndStmt : LocalVarDeclarationOrStmt
                        | LocalVarDeclarationsAndStmt LocalVarDeclarationOrStmt
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_LocalVarDeclarationOrStmt(p):
    '''LocalVarDeclarationOrStmt : LocalVarDeclarationStmt
                                | Stmt
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_LocalVarDeclarationStmt(p):
    '''LocalVarDeclarationStmt : TypeSpec VarDeclarators  SEPSEMICOLON
    '''
    for i in p[2]:
        if (p[1]['type'] == 'SCANNER'):
            p[1]['type'] = 'INT'
        ST.variableAdd(i, i, p[1]['type'])


def p_Stmt(p):
    '''Stmt : EmptyStmt
                | ExpStmt SEPSEMICOLON
                | LabelStmt
                | SelectionStmt
                | IterationStmt
                | JumpStatement
                | Block
    '''


def p_EmptyStmt(p):
    ''' EmptyStmt : SEPSEMICOLON
    '''


def p_LabelStmt(p):
    ''' LabelStmt : Identifier SEPCOLON
                | KEYCASE ConstExp SEPCOLON
                | KEYDEFAULT SEPCOLON
    '''


def p_ExpStmt(p):
    '''ExpStmt : Expression
    '''
    p[0] = p[1]


# IF else ........................
precedence = (
    ('right', 'THAN', 'KEYELSE'),
)


def p_SelectionStmt(p):
    '''SelectionStmt : KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE IfMark1 Stmt IfMark2 %prec THAN
                        | KEYIF SEPLEFTBRACE Expression SEPRIGHTBRACE IfMark1 Stmt KEYELSE IfMark4 Stmt IfMark5
    '''


def p_IfMark1(p):
    '''IfMark1 : '''
    l1 = TAC.newLabel()
    l2 = TAC.newLabel()
    # need to handle p[-2].place big work..
    ResolveRHSArray(p[-2])
    TAC.emit('ifgoto', p[-2]['place'], 'eq 0', l2)
    TAC.emit('goto', l1, '', '')
    TAC.emit('label', l1, '', '')
    ST.newScope()
    p[0] = [l1, l2]


def p_IfMark2(p):
    '''IfMark2 : '''
    ST.endScope()
    TAC.emit('label', p[-2][1], '', '')


def p_IfMark4(p):
    '''IfMark4 : '''
    l3 = TAC.newLabel()
    TAC.emit('goto', l3, '', '')
    TAC.emit('label', p[-3][1], '', '')
    p[0] = [l3]


def p_IfMark5(p):
    '''IfMark5 : '''
    ST.endScope()
    TAC.emit('label', p[-2][0], '', '')


# IF else end here .................


# Iteration statements start here ..................
def p_IterationStmt(p):
    '''IterationStmt : KEYWHILE WhMark1 SEPLEFTBRACE Expression SEPRIGHTBRACE WhMark2 Stmt WhMark3
                        | KEYFOR FoMark0 SEPLEFTBRACE ForInt FoMark1 ForExpr FoMark6 ForIncr FoMark7 SEPRIGHTBRACE FoMark2 Stmt FoMark3
                        | KEYFOR FoMark0 SEPLEFTBRACE ForInt FoMark1 ForExpr SEPRIGHTBRACE FoMark4 Stmt FoMark5
    '''


def p_WhMark1(p):
    '''WhMark1 : '''
    l1 = TAC.newLabel()
    l2 = TAC.newLabel()
    l3 = TAC.newLabel()
    stackbegin.append(l1)
    stackend.append(l3)
    ST.newScope()
    TAC.emit('label', l1, '', '')
    p[0] = [l1, l2, l3]


def p_WhMark2(p):
    '''WhMark2 : '''
    TAC.emit('ifgoto', p[-2]['place'], 'eq 0', p[-4][2])
    TAC.emit('goto', p[-4][1], '', '')
    TAC.emit('label', p[-4][1], '', '')


def p_WhMark3(p):
    '''WhMark3 : '''
    TAC.emit('goto', p[-6][0], '', '')
    TAC.emit('label', p[-6][2], '', '')
    ST.endScope()
    stackbegin.pop()
    stackend.pop()


def p_FoMark0(p):
    '''FoMark0 : '''
    ST.newScope()


def p_FoMark1(p):
    '''FoMark1 : '''
    l1 = TAC.newLabel()
    l2 = TAC.newLabel()
    l3 = TAC.newLabel()
    l4 = TAC.newLabel()
    l5 = TAC.newLabel()
    tempvar = ST.getTemp()
    TAC.emit(tempvar, '0', '', '=')
    stackbegin.append(l5)
    stackend.append(l3)
    TAC.emit('label', l1, '', '')
    lab = [l1, l2, l3, l4, l5]
    p[0] = {
        'label': lab,
        'temp': tempvar
    }


def p_FoMark2(p):
    '''FoMark2 : '''
    TAC.emit('ifgoto', p[-5]['place'], 'eq 0', p[-6]['label'][2])
    TAC.emit('goto', p[-6]['label'][1], '', '')
    TAC.emit('label', p[-6]['label'][1], '', '')


def p_FoMark4(p):
    '''FoMark4 : '''
    TAC.emit('ifgoto', p[-2]['place'], 'eq 0', p[-3]['label'][2])
    TAC.emit('goto', p[-3]['label'][1], '', '')
    TAC.emit('label', p[-3]['label'][1], '', '')


def p_FoMark3(p):
    '''FoMark3 : '''
    TAC.emit('goto', p[-8]['label'][4], '', '')
    TAC.emit('label', p[-8]['label'][2], '', '')
    ST.endScope()
    stackbegin.pop()
    stackend.pop()


def p_FoMark5(p):
    '''FoMark5 : '''
    TAC.emit('goto', p[-5]['label'][0], '', '')
    TAC.emit('label', p[-5]['label'][2], '', '')
    ST.endScope()
    stackbegin.pop()
    stackend.pop()


def p_FoMark6(p):
    '''FoMark6 : '''
    TAC.emit('ifgoto', p[-2]['temp'], 'eq 0', p[-2]['label'][3])
    TAC.emit('label', p[-2]['label'][4], '', '')


def p_FoMark7(p):
    '''FoMark7 : '''
    TAC.emit('goto', p[-4]['label'][0], '', '')
    TAC.emit('label', p[-4]['label'][3], '', '')


def p_ForInt(p):
    '''ForInt : ExpStmts SEPSEMICOLON
            | LocalVarDeclarationStmt
            | SEPSEMICOLON
    '''


def p_ForExpr(p):
    '''ForExpr : Expression SEPSEMICOLON
            | SEPSEMICOLON
    '''
    if (len(p) > 2):
        p[0] = p[1]
        return
    else:
        tempvar = ST.getTemp()
        TAC.emit(tempvar, '1', '', '=')
        p[0] = {
            'place': tempvar,
            'type': 'INT'
        }


def p_ForIncr(p):
    '''ForIncr : ExpStmts
    '''


# Iteration Stmts end here......


def p_ExpStmts(p):
    '''ExpStmts : ExpStmt
                    | ExpStmts SEPCOMMA ExpStmt
    '''


def p_JumpStatement(p):
    '''JumpStatement : KEYBREAK Identifier SEPSEMICOLON
                | KEYBREAK SEPSEMICOLON
                | KEYCONTINUE Identifier SEPSEMICOLON
                | KEYCONTINUE SEPSEMICOLON
                | KEYRETURN Expression SEPSEMICOLON
                | KEYRETURN  SEPSEMICOLON
                | KEYTHROW Expression SEPSEMICOLON
    '''
    if (len(p) == 3 and p[1] == 'break'):
        TAC.emit('goto', stackend[-1], '', '')
        return
    if (len(p) == 3 and p[1] == 'continue'):
        TAC.emit('goto', stackbegin[-1], '', '')
        return
    if (len(p) == 3 and p[1] == 'return'):
        TAC.emit('ret', '', '', '')
        return
    if (len(p) == 4 and p[1] == 'return'):
        fun = ST.getFunction()
        if (ST.getRType(fun) in ['VOID']):
            TAC.error(
                'Error : function is of void type , do not return any value')
        else:
            TAC.emit('ret', p[2]['place'], '', '')
            # TAC.emit('ret','','','')
        return


def p_PrimaryExp(p):
    '''PrimaryExp : QualifiedName
                    | NotJustName
    '''
    p[0] = {
        'place': 'undefined',
        'type': 'UNDEFINED_TYPE'
    }
    if (p[1]['isnotjustname'] == False):
        if ST.variableSearch(p[1]['idVal']):
            p[0]['place'] = ST.getData(p[1]['idVal'], 'place')
            p[0]['type'] = ST.getData(p[1]['idVal'], 'type')
            p[0]['idVal'] = p[1]['idVal']
        else:
            TAC.error('Error : undefined variable '+p[1]['idVal']+' is used.')
    else:
        p[0] = p[1]['val']


def p_NotJustName(p):
    '''NotJustName : SpecialName
                | NewAllocExp
                | ComplexPrimary
    '''
    p[0] = {
        'isnotjustname': True,
        'val': p[1],
    }


def p_ComplexPrimary(p):
    '''ComplexPrimary : SEPLEFTBRACE Expression SEPRIGHTBRACE
            | ComplexPrimaryNoParenthesis
    '''
    if (len(p) > 2):
        p[0] = p[2]
        return
    p[0] = p[1]


def p_ComplexPrimaryNoParenthesis(p):
    '''ComplexPrimaryNoParenthesis : BooleanLiteral
                            | IntLiteral
                            | FlLiteral
                            | ChLiteral
                            | StLiteral
                            | ArrayAccess
                            | FieldAccess
                            | MethodCall
    '''
    p[0] = p[1]


def p_IntLiteral(p):
    '''IntLiteral : IntegerLiteral
    '''
    p[0] = {
        'type': 'INT',
        'place': p[1],
        'novar': True
    }


def p_FlLiteral(p):
    '''FlLiteral : FloatingLiteral
    '''
    p[0] = {
        'type': 'FLOAT',
        'place': p[1],
        'novar': True
    }


def p_ChLiteral(p):
    '''ChLiteral : CharacterLiteral
    '''
    p[0] = {
        'type': 'CHAR',
        'place': p[1]
    }


def p_StLiteral(p):
    '''StLiteral : StringLiteral
    '''
    p[0] = {
        'type': 'STRING',
        'place': p[1]
    }


def p_ArrayAccess(p):
    '''ArrayAccess : QualifiedName SEPLEFTSQBR Expression SEPRIGHTSQBR
                | ComplexPrimary SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
    p[0] = p[1]
    if ('isArrayAccess' in p[0].keys() and p[0]['isArrayAccess']):
        dim = ST.getData(p[0]['idVal'], 'dimension')
        multiplier = 1
        d = dim[p[1]['index_pos']+1:-1]
        for i in d:
            multiplier = i*multiplier
        tempvar1 = ST.getTemp()
        tempvar2 = ST.getTemp()
        TAC.emit(tempvar1, str(multiplier), p[3]['place'], '*')
        TAC.emit(tempvar2, tempvar1, p[1]['index_place'], '+')
        p[0]['isArrayAccess'] = True
        p[0]['type'] = p[1]['type']
        p[0]['place'] = p[1]['place']
        p[0]['idVal'] = p[1]['idVal']
        p[0]['index_place'] = tempvar2
        p[0]['index_pos'] = p[1]['index_pos']+1

    else:
        dim = ST.getData(p[0]['idVal'], 'dimension')
        multiplier = 1
        d = dim[0:-1]
        for i in d:
            multiplier = i*multiplier
        tempvar1 = ST.getTemp()
        tempvar2 = ST.getTemp()
        TAC.emit(tempvar1, str(multiplier), p[3]['place'], '*')
        TAC.emit(tempvar2, tempvar1, '0', '+')

        p[0]['isArrayAccess'] = True
        p[0]['type'] = ST.getData(p[0]['idVal'], 'type')
        p[0]['place'] = ST.getData(p[0]['idVal'], 'place')
        p[0]['index_place'] = tempvar2  # p[3]['place']
        p[0]['index_pos'] = 0


def p_FieldAcess(p):
    '''FieldAccess : NotJustName SEPDOT Identifier
            | RealPostfixExp SEPDOT Identifier
            | QualifiedName SEPDOT KEYTHIS
            | QualifiedName SEPDOT KEYCLASS
            | PrimitiveType SEPDOT KEYCLASS
    '''


def p_MethodCall(p):
    ''' MethodCall : MethodAccess SEPLEFTBRACE argList SEPRIGHTBRACE
            | MethodAccess SEPLEFTBRACE SEPRIGHTBRACE
    '''
    if (len(p) > 4):
        x = p[1]['idVal'].split('.')
        if (p[1]['idVal'] == 'System.out.println'):
            TAC.emit('print', p[3][0], '', '')
            p[0] = p[1]
        elif (p[1]['idVal'] == 'System.out.printf'):
            TAC.emit('printf', p[3], '', '')
            p[0] = p[1]
        elif (x[len(x)-1] in ['nextInt']):
            p[0] = p[1]
            p[0]['input'] = 'True'
            return
        else:
            currScope = ST.retScope()
            varSave = ST.variableSave(currScope)
            for i in varSave:
                TAC.emit('push', i, '', '')  # how array would be done
            arg = len(p[3])
            for i in p[3]:
                TAC.emit('push', i, '', '')
            newfuncname = p[1]['idVal'] + str(arg)
            if (newfuncname in function):
                TAC.emit('call', newfuncname, '', '')
            else:
                length = len(newfuncname)
                li = newfuncname[0:length-1]
                TAC.error('Error: function '+li+' not declared')
            rt = ST.getRType(newfuncname)
            tempvar = ST.getTemp()
            if (rt not in ['VOID']):
                TAC.emit('pop', tempvar, '', '')
            l = len(varSave)
            for i in range(1, l+1):
                TAC.emit('pop', varSave[l-i], '', '')
            p[0] = {
                'place': tempvar,
                'type': rt
            }
    else:
        x = p[1]['idVal'].split('.')
        if (x[len(x)-1] in ['nextInt']):
            p[0] = p[1]
            p[0]['input'] = 'True'
            return
        else:
            currScope = ST.retScope()
            varSave = ST.variableSave(currScope)
            for i in varSave:
                TAC.emit('push', i, '', '')  # how array would be done
            arg = 0
            newfuncname = p[1]['idVal']+str(arg)
            if (newfuncname in function):
                TAC.emit('call', newfuncname, '', '')
            else:
                length = len(newfuncname)
                li = newfuncname[0:length-1]
                TAC.error('Error: function '+li+' not declared')
            rt = ST.getRType(newfuncname)
            tempvar = ST.getTemp()
            if (rt not in ['VOID']):
                TAC.emit('pop', tempvar, '', '')
            l = len(varSave)
            for i in range(1, l+1):
                TAC.emit('pop', varSave[l-i], '', '')
            p[0] = {
                'place': tempvar,
                'type': rt
            }


def p_MethodAccess(p):
    ''' MethodAccess : ComplexPrimaryNoParenthesis
                | SpecialName
                | QualifiedName
    '''
    p[0] = p[1]


def p_SpecialName(p):
    '''SpecialName : KEYTHIS
    '''


def p_argList(p):
    '''argList : Expression
            | argList SEPCOMMA Expression
    '''
    if (len(p) == 2):
        p[0] = [p[1]['place']]
        return
    p[0] = p[1] + [p[3]['place']]


def p_NewAllocExp(p):
    '''NewAllocExp : PlainNewAllocExp
                    | QualifiedName SEPDOT PlainNewAllocExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    p[0] = p[3]


def p_PlainNewAllocExp(p):
    '''PlainNewAllocExp :  ArrayAllocExp
                        | ClassAllocExp
                        | ArrayAllocExp SEPLEFTPARAN SEPRIGHTPARAN
                        | ClassAllocExp SEPLEFTPARAN SEPRIGHTPARAN
                        | ArrayAllocExp SEPLEFTPARAN ArrayInit SEPRIGHTPARAN
                        | ClassAllocExp SEPLEFTPARAN FieldDeclarations SEPRIGHTPARAN
    '''
    if (len(p) == 2):
        p[0] = p[1]
    p[0] = p[1]


def p_ClassAllocExp(p):
    '''ClassAllocExp : KEYNEW TypeName SEPLEFTBRACE argList SEPRIGHTBRACE
                        | KEYNEW TypeName SEPLEFTBRACE SEPRIGHTBRACE
    '''
    p[0] = p[2]


def p_ArrayAllocExp(p):
    '''ArrayAllocExp : KEYNEW TypeName DimExprs Dims
                            | KEYNEW TypeName DimExprs
                            | KEYNEW TypeName Dims
    '''
    # only 2nd rule is done i.e 1D array
    place = 1
    for x in p[3]:
        place = place*int(x['place'])
    place = str(place)
    if (len(p) == 4):
        p[0] = {
            'type': p[2].upper(),
            'place': place,
            'isarray': True,
            'dimensions': [int(x['place']) for x in p[3]]
        }


def p_DimExprs(p):
    '''DimExprs : DimExpr
                | DimExprs DimExpr
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
        return
    else:
        p[0] = p[1] + [p[2]]


def p_DimExpr(p):
    '''DimExpr : SEPLEFTSQBR Expression SEPRIGHTSQBR
    '''
    if (p[2]['type'] == 'INT'):
        p[0] = p[2]
    else:
        TAC.error(
            "Error : Array declaration needs an integer size = "+p[2]['place'])


def p_Dims(p):
    '''Dims : OP_DIM
            | Dims OP_DIM
    '''
    if (len(p) == 2):
        p[0] = 1
        return
    else:
        p[0] = 1 + p[1]
        return


def p_PostfixExp(p):
    '''PostfixExp : PrimaryExp
                    | RealPostfixExp
    '''
    p[0] = p[1]


def p_RealPostfixExp(p):
    '''RealPostfixExp : PostfixExp OPINCREMENT
                    | PostfixExp OPDECREMENT
    '''
    if (p[1]['type'] == 'INT'):
        if (p[2][0] == '+'):
            TAC.emit(p[1]['place'], p[1]['place'], '1', '+')
        else:
            TAC.emit(p[1]['place'], p[1]['place'], '1', '-')
        p[0] = {
            'place': p[1]['place'],
            'type': 'INT'
        }
    else:
        TAC.error("Error: increment operator can be used only with integer")


def p_unaryExp(p):
    '''unaryExp : OPINCREMENT unaryExp
                | OPDECREMENT unaryExp
                | ArithmeticUnaryOp castExp
                | LogicalUnaryExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    if (p[1] == '++'):
        TAC.emit(p[2]['place'], p[2]['place'], '1', '+')
        p[0] = p[2]
    elif (p[1] == '--'):
        TAC.emit(p[2]['place'], p[2]['place'], '1', '-')
        p[0] = p[2]
    elif (p[1] == '-'):
        if ('novar' in p[2].keys()):
            tempvar = ST.getTemp()
            TAC.emit(tempvar, '0', p[2]['place'], '-')
            p[0] = p[2]
            p[0]['place'] = tempvar
        else:
            tempvar = ST.getTemp()
            TAC.emit(tempvar, '0', p[2]['place'], '-')
            p[0] = p[2]
            p[0]['place'] = tempvar
    elif (p[1] == '+'):
        if ('novar' in p[2].keys()):
            tempvar = ST.getTemp()
            TAC.emit(tempvar, '0', p[2]['place'], '+')
            p[0] = p[2]
            p[0]['place'] = tempvar
        else:
            tempvar = ST.getTemp()
            TAC.emit(tempvar, '0', p[2]['place'], '+')
            p[0] = p[2]
            p[0]['place'] = tempvar


def p_LogicalUnaryExp(p):
    '''LogicalUnaryExp : PostfixExp
                        | LogicalUnaryOp unaryExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_LogicalUnaryOp(p):
    '''LogicalUnaryOp : OPTILDE
                         | OPNOT
    '''
    p[0] = p[1]


def p_ArithmeticUnaryOp(p):
    '''ArithmeticUnaryOp : OPPLUS
                            | OPMINUS
    '''
    p[0] = p[1]


def p_castExp(p):
    ''' castExp : unaryExp
                | SEPLEFTBRACE PrimitiveTypeExp SEPRIGHTBRACE castExp
                | SEPLEFTBRACE ClassTypeExp SEPRIGHTBRACE castExp
                | SEPLEFTBRACE Expression SEPRIGHTBRACE LogicalUnaryExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_PrimitiveTypeExp(p):
    '''PrimitiveTypeExp : PrimitiveType
                    | PrimitiveType Dims
    '''


def p_ClassTypeExp(p):
    '''ClassTypeExp : QualifiedName Dims
    '''


def p_multiplyExp(p):
    '''multiplyExp : castExp
                    | multiplyExp OPMULTIPLY castExp
                    | multiplyExp OPDIVIDE castExp
                    | multiplyExp OPMOD castExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[2] == '*':
        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit(tempvar, p[1]['place'], p[3]['place'], p[2])
            p[0]['type'] = 'INT'
        else:
            TAC.error('Error: Type is not compatible' +
                      p[1]['place']+','+p[3]['place']+'.')
    elif p[2] == '/':
        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit(tempvar, p[1]['place'], p[3]['place'], p[2])
            p[0]['type'] = 'INT'
        else:
            TAC.error('Error: Type is not compatible' +
                      p[1]['place']+','+p[3]['place']+'.')
    elif p[2] == '%':
        if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit(tempvar, p[1]['place'], p[3]['place'], p[2])
            p[0]['type'] = 'INT'
        else:
            TAC.error('Error: Type is not compatible' +
                      p[1]['place']+','+p[3]['place']+'.')


def p_addExp(p):
    '''addExp : multiplyExp
                        | addExp OPPLUS multiplyExp
                        | addExp OPMINUS multiplyExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        p[3] = ResolveRHSArray(p[3])
        p[1] = ResolveRHSArray(p[1])
        TAC.emit(tempvar, p[1]['place'], p[3]['place'], p[2])
        p[0]['type'] = 'INT'
    else:
        TAC.error("Error: integer value is needed")


def p_shiftExp(p):
    '''shiftExp : addExp
                    | shiftExp OPLEFTSHIFT addExp
                    | shiftExp OPRIGHTSHIFT addExp
                    | shiftExp OPLOGICALSHIFT addExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_relation(p):
    '''relation : shiftExp
                        | relation OPLESSER shiftExp
                        | relation OPGREATER shiftExp
                        | relation OPLESSEQ shiftExp
                        | relation OPGREATEQ shiftExp
                        | relation OPINSTANCEOF TypeSpec
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    l1 = TAC.newLabel()
    l2 = TAC.newLabel()
    l3 = TAC.newLabel()
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        if (p[2] == '>'):
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit('ifgoto', p[1]['place'], 'g '+p[3]['place'], l2)
            TAC.emit('goto', l1, '', '')
            TAC.emit('label', l1, '', '')
            TAC.emit(tempvar, '0', '', '=')
            TAC.emit('goto', l3, '', '')
            TAC.emit('label', l2, '', '')
            TAC.emit(tempvar, '1', '', '=')
            TAC.emit('label', l3, '', '')
            p[0]['type'] = 'INT'
        elif (p[2] == '>='):
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit('ifgoto', p[1]['place'], 'ge '+p[3]['place'], l2)
            TAC.emit('goto', l1, '', '')
            TAC.emit('label', l1, '', '')
            TAC.emit(tempvar, '0', '', '=')
            TAC.emit('goto', l3, '', '')
            TAC.emit('label', l2, '', '')
            TAC.emit(tempvar, '1', '', '=')
            TAC.emit('label', l3, '', '')
            p[0]['type'] = 'INT'
        elif (p[2] == '<'):
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit('ifgoto', p[1]['place'], 'l '+p[3]['place'], l2)
            TAC.emit('goto', l1, '', '')
            TAC.emit('label', l1, '', '')
            TAC.emit(tempvar, '0', '', '=')
            TAC.emit('goto', l3, '', '')
            TAC.emit('label', l2, '', '')
            TAC.emit(tempvar, '1', '', '=')
            TAC.emit('label', l3, '', '')
            p[0]['type'] = 'INT'
        elif (p[2] == '<='):
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit('ifgoto', p[1]['place'], 'le '+p[3]['place'], l2)
            TAC.emit('goto', l1, '', '')
            TAC.emit('label', l1, '', '')
            TAC.emit(tempvar, '0', '', '=')
            TAC.emit('goto', l3, '', '')
            TAC.emit('label', l2, '', '')
            TAC.emit(tempvar, '1', '', '=')
            TAC.emit('label', l3, '', '')
            p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_eqExp(p):
    '''eqExp : relation
                        | eqExp OPCHECKEQ relation
                        | eqExp OPNOTEQ relation
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    l1 = TAC.newLabel()
    l2 = TAC.newLabel()
    l3 = TAC.newLabel()
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        if (p[2][0] == '='):
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit('ifgoto', p[1]['place'], 'eq '+p[3]['place'], l2)
            TAC.emit('goto', l1, '', '')
            TAC.emit('label', l1, '', '')
            TAC.emit(tempvar, '0', '', '=')
            TAC.emit('goto', l3, '', '')
            TAC.emit('label', l2, '', '')
            TAC.emit(tempvar, '1', '', '=')
            TAC.emit('label', l3, '', '')
            p[0]['type'] = 'INT'
        else:
            p[3] = ResolveRHSArray(p[3])
            p[1] = ResolveRHSArray(p[1])
            TAC.emit('ifgoto', p[1]['place'], 'eq '+p[3]['place'], l2)
            TAC.emit('goto', l1, '', '')
            TAC.emit('label', l1, '', '')
            TAC.emit(tempvar, '1', '', '=')
            TAC.emit('goto', l3, '', '')
            TAC.emit('label', l2, '', '')
            TAC.emit(tempvar, '0', '', '=')
            TAC.emit('label', l3, '', '')
            p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_andExp(p):
    '''andExp : eqExp
                    | andExp OPBINAND eqExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        p[3] = ResolveRHSArray(p[3])
        p[1] = ResolveRHSArray(p[1])
        TAC.emit(tempvar, p[1]['place'], p[3]['place'], 'and')
        p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_exOrExp(p):
    '''exOrExp : andExp
                    | exOrExp OPXOR andExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        p[3] = ResolveRHSArray(p[3])
        p[1] = ResolveRHSArray(p[1])
        TAC.emit(tempvar, p[1]['place'], p[3]['place'], 'xor')
        p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_inOrExp(p):
    '''inOrExp : exOrExp
                        | inOrExp OPBINOR exOrExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        p[3] = ResolveRHSArray(p[3])
        p[1] = ResolveRHSArray(p[1])
        TAC.emit(tempvar, p[1]['place'], p[3]['place'], 'or')
        p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_condAndExp(p):
    '''condAndExp : inOrExp
                            | condAndExp OPAND inOrExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        p[0] = p[1]
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        p[3] = ResolveRHSArray(p[3])
        p[1] = ResolveRHSArray(p[1])
        TAC.emit(tempvar, p[1]['place'], p[3]['place'], 'and')
        p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_condOrExp(p):
    '''condOrExp : condAndExp
                        | condOrExp OPOR condAndExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return
    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE'
    }
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        p[3] = ResolveRHSArray(p[3])
        p[1] = ResolveRHSArray(p[1])
        TAC.emit(tempvar, p[1]['place'], p[3]['place'], 'or')
        p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_condExp(p):
    ''' condExp : condOrExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return


def p_assignExp(p):
    '''assignExp : condExp
                        | unaryExp assigOp assignExp
    '''
    if (len(p) == 2):
        p[0] = p[1]
        return

    if (p[3] == 'Scanner'):
        p[0] = p[3]
        return

    if ('input' in p[3].keys() and p[3]['input']):
        dst = p[1]['place']
        if ('isArrayAccess' in p[1].keys() and p[1]['isArrayAccess']):
            dst = p[1]['place'] + "["+p[1]['index_place'] + "]"
        TAC.emit('input', dst, '', '')
        p[0] = {}
        return

    if (type(p[3]) != type({})):
        p[0] = p[3]
        return
    if ('isarray' in p[3].keys() and p[3]['isarray'] and p[2] == '='):
        TAC.emit('declare', p[1]['place'], p[3]['place'], p[3]['type'])
        ST.setDimension(p[1]['idVal'], p[3]['dimensions'])
        return

    tempvar = ST.getTemp()
    p[0] = {
        'place': tempvar,
        'type': 'UNDEFINED_TYPE',
        'isarray': False
    }
    if ('input' in p[3].keys() and p[3]['input']):
        p[0] = p[3]
        return
    if p[1]['type'] == 'UNDEFINED_TYPE' or p[3]['type'] == 'UNDEFINED_TYPE':
        return
    if p[1]['type'] == 'INT' and p[3]['type'] == 'INT':
        if (p[2][0] == '='):

            p[3] = ResolveRHSArray(p[3])

            dst = p[1]['place']
            if ('isArrayAccess' in p[1].keys() and p[1]['isArrayAccess']):
                dst = p[1]['place'] + "["+p[1]['index_place'] + "]"
            TAC.emit(dst, p[3]['place'], '', p[2])
            p[0] = p[1]
        else:
            p[3] = ResolveRHSArray(p[3])
            new1 = p[1].copy()
            new = ResolveRHSArray(p[1])
            p[1] = new1.copy()
            dst = p[1]['place']
            if ('isArrayAccess' in p[1].keys() and p[1]['isArrayAccess']):
                dst = p[1]['place'] + "["+p[1]['index_place'] + "]"
            TAC.emit(tempvar, new['place'], p[3]['place'], p[2][0])
            TAC.emit(dst, tempvar, '', p[2][1])
        p[0]['type'] = 'INT'
    else:
        TAC.error('Error: Type is not compatible' +
                  p[1]['place']+','+p[3]['place']+'.')


def p_assigOp(p):
    ''' assigOp : OPEQUAL
                        | OPMULTIPLYEQ
                        | OPDIVIDEEQ
                        | OPMODEQ
                        | OPPLUSEQ
                        | OPMINUSEQ
                        | OPLEFTSHIFTEQ
                        | OPRIGHTSHIFTEQ
                        | OPLOGICALSHIFTEQ
                        | OPBINANDEQ
                        | OPXOREQ
                        | OPBINOREQ
    '''
    p[0] = p[1]


def p_Expression(p):
    '''Expression : assignExp
    '''
    p[0] = p[1]


def p_ConstExp(p):
    '''ConstExp : condExp
    '''
    p[0] = p[1]


def p_error(p):
    if p == None:
        print(str(sys.argv[1])+" ::You missed something at the end")
    else:
        print(str(sys.argv[1])+" :: Syntax error in line no " + str(p.lineno))


ST = symTable()
TAC = threeAC()


# main function
def main():

    # build the parser
    yacc.yacc()

    # open the java test file
    java_file = open(sys.argv[1], 'r')
    data = java_file.read()
    data += "\n"
    java_file.close()

    # Parse the data
    yacc.parse(data)

    # dump 3AC to txt file
    TAC.dump3ACToTXT()


if __name__ == '__main__':
    main()
