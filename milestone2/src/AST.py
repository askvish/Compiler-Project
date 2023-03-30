from Lexer import Lexer
from Parser import Parser
import graphviz
import antlr4
import sys


count = 0


def mywalk(expr, graph, rules):
    global count
    # if (isinstance(expr,Parser.AddExpContext)):
    # graph.node(name = str(count), label = expr.op)
    # count+=1
    # node = str(count)
    # return node
    # if expr.op is not None:
    #     print(expr.op.text)
    # pass
    if (isinstance(expr, antlr4.tree.Tree.TerminalNode)):
        graph.node(name=str(count), label=expr.getText())
        node = str(count)
        count += 1
        return node

    childno = expr.getChildCount()
    t = expr.getRuleIndex()

    if childno == 1:
        for j in expr.getChildren():
            if (isinstance(j, antlr4.tree.Tree.TerminalNode)):
                node = str(count)
                graph.node(name=node, label=expr.getText() +
                           ' (' + rules[t] + ')')
                count += 1
            else:
                node = mywalk(j, graph, rules)
            return node

    node = str(count)
    graph.node(name=node, label=rules[t])
    count += 1
    child_list = list(expr.getChildren())
    startIdx = 0
    if (child_list[0].getText() == "for" or child_list[0].getText() == 'while' or child_list[0].getText() == 'if'):
        graph.node(name=node, label=child_list[0].getText())
        count += 1
        startIdx = 1
    elif type(expr) == Parser.AddExpContext or type(expr) == Parser.MultiplyExpContext or type(expr) == Parser.RelationContext or type(expr) == Parser.ShiftExpContext or type(expr) == Parser.CondOrExpContext or type(expr) == Parser.CondAndExpContext or type(expr) == Parser.InOrExpContext or type(expr) == Parser.AndExpContext or type(expr) == Parser.EqExpContext:
        graph.node(name=node, label=child_list[1].getText())
        count += 1
        nodel = mywalk(child_list[0], graph, rules)
        graph.edge(node, nodel)
        noder = mywalk(child_list[2], graph, rules)
        graph.edge(node, noder)
        return node
    elif type(expr) == Parser.VarDeclaratorContext:
        if len(child_list) == 3:
            graph.node(name=node, label=child_list[1].getText())
            count += 1
            nodel = mywalk(child_list[0], graph, rules)
            graph.edge(node, nodel)
            noder = mywalk(child_list[2], graph, rules)
            graph.edge(node, noder)
            return node
    for i in range(startIdx, len(child_list)):
        nodec = mywalk(child_list[i], graph, rules)
        graph.edge(node, nodec)

    return node


def main():
    lexer = Lexer(antlr4.StdinStream())
    stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(stream)
    rules = parser.ruleNames
    tree = parser.prog()
    graph = graphviz.Digraph(format='dot')
    mywalk(tree, graph, rules)

    graph.render(sys.argv[1])


if __name__ == '__main__':
    main()
